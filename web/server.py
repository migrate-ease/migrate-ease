#!/usr/bin/python3
"""
Copyright 2017-2025 Arm ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from flask import Flask, render_template, request, jsonify, url_for, redirect, send_file

import os
import subprocess
import threading
import json
import time
import tarfile
import zipfile
import uuid
import git
import shutil
import argparse
from werkzeug.utils import secure_filename
from threading import Thread
from datetime import datetime

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.abspath(app.root_path + '/uploads')
app.config['RESULT_FOLDER'] = os.path.abspath(app.root_path + '/results')
app.config['MAX_CONTENT_LENGTH'] = 128 * 1024 * 1024  # 128MB max file size
supported_scan_cats = ['cpp', 'docker', 'go', 'java', 'python', 'rust']

# Global variables to track job status
current_job = {
    'id': None,
    'status': None,
    'output': [],   # Console output
    'results': []   # Scan results for each category
}

# Ali cloud instances to march map
# This is used to map the instance type to the corresponding architecture
ali_instance_march_map = {
        "g8y": "armv8.6-a+sve2",
        "g6r": "armv8-a",
        "c8y": "armv8.6-a+sve2",
        "c6r": "armv8-a",
        "r8y": "armv8.6-a+sve2"
}

# Ensure upload and result directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    current_job['id'] = str(uuid.uuid4())
    print(f"this id: {current_job['id']}")
    current_job['status'] = None
    return render_template('index.html', job_status=current_job['status'])

def get_march(csp, instance):
    default_march = 'armv8-a'
    if csp.lower() == 'alicloud':
        return ali_instance_march_map.get(instance, default_march)
    return default_march

def scan_dir(prj_path, target_march, git_info= None, scan_cat='all'):
    scan_jobs = []
    env = os.environ.copy()
    if 'PYTHONPATH' not in os.environ:
        env['PYTHONPATH'] = os.path.abspath(app.root_path + '/../')

    if git_info:
        git_params = '--git-repo '+git_info['url']
        if git_info['branch']:
            git_params += ' --branch ' + git_info['branch']
    else:
        git_params = ''

    if scan_cat == 'all':
        # Scan all possible categories
        for this_cat in supported_scan_cats:
            if this_cat == 'cpp':
                cmdline = ['python3 '+ env['PYTHONPATH'] + '/' + this_cat + '/__main__.py ' + git_params + ' --output ' + app.config['RESULT_FOLDER'] + '/' + current_job['id'] + '_' + this_cat + '.json --warning-level L2 --march ' + target_march + ' .']

            else:
                cmdline = ['python3 '+ env['PYTHONPATH'] + '/' + this_cat + '/__main__.py ' + git_params + ' --output ' + app.config['RESULT_FOLDER'] + '/' + current_job['id'] + '_' + this_cat + '.json --march ' + target_march + ' .']
            s = ' '.join(cmdline)
            scan_jobs.append({'category':this_cat, 'cmd':cmdline})
    elif scan_cat in supported_scan_cats:
        if scan_cat == 'cpp':
            cmdline = ['python3 '+ env['PYTHONPATH'] + '/' + scan_cat + '/__main__.py ' + git_params + ' --output ' + app.config['RESULT_FOLDER'] + '/' + current_job['id'] + '_' + scan_cat + '.json --warning-level L2 --march ' + target_march + ' .']
        else:
            cmdline = ['python3 '+ env['PYTHONPATH'] + '/' + scan_cat + '/__main__.py ' + git_params + ' --output ' + app.config['RESULT_FOLDER'] + '/' + current_job['id'] + '_' + scan_cat + '.json --march ' + target_march + ' .']
        s = ' '.join(cmdline)
        scan_jobs.append({'category':scan_cat, 'cmd':cmdline})
    else:
        print(f'[ERROR] Wrong scan category: {scan_cat}')

    if len(scan_jobs) > 0:
        current_job['status'] = 'scanning'
        # Read output in real-time
        for this_job in scan_jobs:
            print(this_job['cmd'])
            process = subprocess.Popen(
                this_job['cmd'],
                env = env,
                cwd = prj_path,
                stdout = subprocess.PIPE,
                stderr = subprocess.STDOUT,
                universal_newlines = True,
                shell = True
            )
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    current_job['output'].append(output.strip())

            # Save result
            if process.returncode == 0:
                current_job['results'].append({'category':this_job['category'], 'status':'success', 'result':app.config['RESULT_FOLDER'] + '/' + current_job['id'] + '_' + this_job['category'] + '.json'})
            else:
                current_job['results'].append({'category':this_job['category'], 'status':'failed'})
        current_job['status'] = 'completed'
        shutil.rmtree(prj_path)
    else:
        current_job['status'] = 'failed'
        current_job['output'].append('No targets to scan')

# Process git repo
class CloneProgress(git.RemoteProgress):
    # See: https://gitpython.readthedocs.io/en/stable/reference.html#git.remote.RemoteProgress
    OP_CODES = [
        "BEGIN",
        "CHECKING_OUT",
        "COMPRESSING",
        "COUNTING",
        "END",
        "FINDING_SOURCES",
        "RECEIVING",
        "RESOLVING",
        "WRITING",
    ]
    OP_CODE_MAP = {
        getattr(git.RemoteProgress, _op_code): _op_code for _op_code in OP_CODES
    }
    def get_curr_op(self, op_code):
        op_code_masked = op_code & self.OP_MASK
        return self.OP_CODE_MAP.get(op_code_masked, "?").title()

    def update(self, op_code, cur_count, max_count=None, *args, **kwargs):
        if op_code & self.BEGIN:
            self.curr_op = self.get_curr_op(op_code)
            current_job['output'].append(f"{self.curr_op} ...")
        with app.app_context():
            if max_count is not None:
                status = f"{self.curr_op} ... {int(cur_count)}/{int(max_count)} objects"
                current_job['output'][-1] = status

def process_git(repo_url, march, repo_branch=None):
    repo_path = '/tmp/' + current_job['id']

    if not os.path.exists(repo_path):
        try:
            current_job['output'].insert(0, f'Cloning {repo_url} {repo_branch} ...')
            # set depth to 1 to reduce clone time
            if repo_branch:
                repo = git.Repo.clone_from(repo_url, repo_path, branch=repo_branch, depth=1, progress=CloneProgress())
            else:
                repo = git.Repo.clone_from(repo_url, repo_path, depth=1, progress=CloneProgress())
            current_job['output'].append("Successfully cloned")
            print(f"Successfully cloned {repo_branch} from {repo_url} to {repo_path}")
            # Run scanners
            scan_dir(repo_path, target_march=march, git_info={'url':repo_url, 'branch':repo_branch})
        except Exception as e:
            print(f"An error occurred: {e}")
            return jsonify({'status':'ERROR', 'message':'Clone failure: {e}'})
    else:
        print(f'[Warning] Specified dest [{repo_path}] already exisits. Skip it.')


# Process uploaded file
def process_file(filepath, march):
    extract_dir = os.path.join('/tmp/', current_job['id'])
    os.makedirs(extract_dir, exist_ok=True)

    try:
        # Extract archive
        if filepath.endswith('.zip'):
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)
        elif filepath.endswith('.tar'):
            with tarfile.open(filepath, 'r') as tar_ref:
                tar_ref.extractall(extract_dir)
        else:
            shutil.copy(filepath, extract_dir + '/' + os.path.basename(filepath))

        # Run scanners
        scan_dir(extract_dir, target_march=march)

    except Exception as e:
        current_job['status'] = 'failed'
        current_job['output'].append(str(e))

@app.route('/scan/git', methods=['POST'])
def scan_git():
    repo_url = request.form.get('git-repo')
    branch = request.form.get('git-branch')
    csp = request.form.get('csp')
    instance = request.form.get('instance')
    march = get_march(csp, instance)
    # Check if a job with this uid is already in progress
    if current_job['status'] and current_job['status'] != 'completed':
        return jsonify({'status':'ERROR', 'message':'A job is running'})

    if repo_url:
        # Initialize job
        current_job['status'] = 'fetching'
        current_job['output'] = []
        current_job['results'] = []

        # Start processing in background
        thread = threading.Thread(target=process_git, args=(repo_url, march, branch))
        thread.start()

        return jsonify({'status':current_job['status'].upper(), 'access_key':current_job['id']}), 200
    else:
        return jsonify({'status':'ERROR', 'message':'No git repo is given'})

@app.route('/scan/file', methods=['POST'])
def upload_file():
    if 'archive-file' not in request.files:
        return jsonify({'status':'ERROR', 'message': 'No file part'})

    # Check if a job with this uid is already in progress
    if current_job['status'] and current_job['status'] != 'completed':
        return jsonify({'status':'ERROR', 'message':'A job is running'})

    file = request.files['archive-file']
    csp = request.form.get('csp')
    instance = request.form.get('instance')
    march = get_march(csp, instance)
    if file:
        # Initialize job
        current_job['status'] = 'uploading'
        current_job['output'] = []
        current_job['results'] = []

        # Save file
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Start processing in background
        thread = threading.Thread(target=process_file, args=(filepath, march))
        thread.start()

        return jsonify({'status': current_job['status'].upper()})
    else:
        return jsonify({'status':'ERROR', 'message':'Invalid file'})

@app.route('/status')
def get_status():
    return jsonify({
        'status': current_job['status'].upper(),
        'output': current_job['output']
    })

@app.route('/result')
def show_result():
    if current_job['status'] != 'completed':
        return redirect(url_for('index'))

    # Read result file(s)
    results = []
    for this_result in current_job['results']:
        this_result_file = this_result['result']
        print(this_result_file)
        with open(this_result_file, 'r', encoding='utf-8-sig') as f:
            modified_time = os.path.getmtime(this_result_file)
            # Convert to a human-readable format
            modified_time_readable = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M:%S')
            json_data = json.load(f)
            march_map = {
                "armv8-a": "Armv8-a Generic",
                "armv8.6-a+sve2": "Arm Neoverse N2",
            }
            json_data['march'] = march_map.get(json_data['march'], "Unknow Architecture")
            results.append({'name':this_result['category'], 'result':json_data, 'modified_time':modified_time_readable})

    return render_template('result.html', results=results)

@app.route('/report')
def download_report():
    if current_job['status'] != 'completed':
        return redirect(url_for('index'))

    # Create a zip file
    zip_filename = app.config['RESULT_FOLDER'] + f"/report-{current_job['id']}.zip"
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for this_result in current_job['results']:
            cleaned_file_name = os.path.basename(this_result['result']).split('_', 1)[1]
            zipf.write(this_result['result'], cleaned_file_name)

    # Send the zip file
    return send_file(zip_filename, as_attachment=True, download_name="report.zip")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Migrate-ease Web UI server')
    parser.add_argument('--port', type=int, default=8080, help='Port to run the server on (default: 8080)')
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=True)

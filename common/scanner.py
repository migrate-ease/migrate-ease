import os
import re
import traceback

from common.error import Error


class BaseScanner:
    #  List of (hidden) subdirectories used by version control systems.
    VCS_SUBDIRECTORIES = ['.git', '.hg', '.svn', 'CVS']

    NON_EMPTY_LINE_RE = re.compile(r'\S')

    FILE_SUMMARY = {}

    def accepts_file(self, filename):
        """
        Overriden by subclasses to decide whether or not to accept a
        file.

        Args:
            filename (str): Filename under consideration.

        Returns:
            bool: True if the file with the given name is accepted by this
            scanner, else False.
        """
        return False

    def finalize_report(self, report):
        """
        Finalizes the report for this scanner.

        Args:
            report (Report): Report to finalize_report.
        """
        pass

    def has_scan_file_object(self):
        return hasattr(self, 'scan_file_object')

    def initialize_report(self, report):
        """
        Initialises the report for this scanner, which may include
        initializing scanner-specific fields in the Report.

        Args:
            report (Report): Report to initialize_report.
        """
        pass

    def scan_file(self, filename, report):
        """
        Scans the file with the given name for potential porting issues.

        Args:
            filename (str): Name of the file to scan.
            report (Report): Report to add issues to.
        """
        try:
            report.add_source_file(filename)
            self.scan_filename(filename, report)

            if self.has_scan_file_object():

                #  there could be bad soft links so we have to
                #  check before opening it.
                if os.path.exists(filename):

                    with open(filename, errors='ignore') as f:
                        try:
                            self.scan_file_object(filename, f, report)

                        except KeyboardInterrupt:
                            raise

                        except BaseException:
                            report.add_error(Error(description=str(traceback.format_exc()),
                                                   filename=filename))

        except KeyboardInterrupt:
            raise

        except BaseException:
            report.add_error(Error(description=str(traceback.format_exc()),
                                   filename=filename))

    def scan_filename(self, filename, report):
        """
        Overridden by subclasses to scan for potential porting issues based
        on the name of the file.

        Args:
            filename (str): Name of the file to scan.
            report (Report): Report to add issues to.
        """
        pass

    def scan_tree(self, root, report, progress_callback=None):
        """
        Scans the filesysem tree starting at root for potential porting issues.

        Args:
            root (str): The root of the filesystem tree to scan.
            report (Report): Report to add issues to.
            progress_callback (function): Optional callback called with file names.
        """
        for dirName, _, fileList in os.walk(root):

            fileList.sort()

            for fname in fileList:

                path = os.path.join(dirName, fname)
                if not self._is_vcs_directory(path) and self.accepts_file(path):

                    if progress_callback:
                        progress_callback(path)

                    self.scan_file(path, report)

    @staticmethod
    def _is_vcs_directory(path):
        """
        Returns:
            bool: True if the path contains a version control directory (e.g. .git), else False.
        """
        return any([('/%s/' % x) in path for x in BaseScanner.VCS_SUBDIRECTORIES])

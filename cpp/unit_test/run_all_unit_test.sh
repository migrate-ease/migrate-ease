# Steps to generate unit test coverage report:
# Run run_all_unit_test.sh
# Then use the coverage combine command to merge reports
# Use coverage report --omit="test_*.py" -m to view the report directly in the command line
# Use coverage html --omit="test_*.py" to generate an HTML report
# --omit="test_*.py" ignores the coverage of the test cases themselves, focusing only on the coverage of the functional modules.

[[ -d "advisor" ]] || ln -s ../advisor advisor
[[ -d "db" ]] || ln -s ../db db

for file in $(ls test*.py); do
    case "$file" in
        # Skip test for test_naive_cpp.py, because self.in_arch and self.in_non_arch are deprected.
        # Skip test for test_find_port.py because some functions used in the test are not available in the find_port class, such as find_port_dir, port_filenames, etc.
        #
        # Issues to be fixed later.
        # test_csv_issue_type_count_by_file_report.py fails because CsvIssueTypeCountByFileReport object has no attribute ISSUE_TYPES.
        # test_json_report.py fails because of Object of type IssueTypeConfig is not JSON serializable.
        "test_naive_cpp.py" | "test_find_port.py" | \
        "test_csv_issue_type_count_by_file_report.py" | "test_json_report.py" )
            echo "### Skip test for $file"
            continue
            ;;
    esac
    echo "### Do test for $file"
    coverage run -p --omit="test_*.py" "$file"
done
coverage combine
coverage html

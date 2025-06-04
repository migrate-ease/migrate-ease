#!/usr/bin/env bash
show_help() {
    echo "Usage: migrate_to_CSP.sh [OPTIONS] [SCAN_PATH]"
    echo "Migrate to ARM cloud instances with specified architecture."
    echo
    echo "Options:"
    echo "  -v, --vendor VENDOR   Specify the cloud vendor (e.g., aliCloud)."
    echo "  -i, --instance TYPE   Specify the instance type (e.g., g8y, c8y, r8y, g6r, c6r)."
    echo "  -h, --help            Show help message."
    echo
    echo "SCAN_PATH is the path to the code directory that needs to be scanned."
}

migrate_to_aliCloud() {
    local instance="$1"
    local scan_path="$2"
    declare -A instance_arch_map=(
        ["g8y"]="armv8.6-a+sve2"
        ["g6r"]="armv8-a"
        ["c8y"]="armv8.6-a+sve2"
        ["c6r"]="armv8-a"
        ["r8y"]="armv8.6-a+sve2"
    )
    local valid_instances=("${!instance_arch_map[@]}")
    local arch="${instance_arch_map[$instance]}"
    if [[ -z "$arch" ]]; then
        echo "Error: No architecture mapping found for instance '$instance'."
        echo "Supported instances are: ${valid_instances[*]}."
        return 1
    fi

    local valid_scanners=("cpp" "docker" "go" "js" "java" "python" "rust")

    echo "Run all scanners for instance '$instance' with architecture '$arch'."
    for s in "${valid_scanners[@]}"; do
        echo "Executing: python3 -m $s --march $arch --output migrate_to_${instance}_$s.json $scan_path"
        python3 -m "$s" --march "$arch" --output migrate_to_"$instance"_"$s".json "$scan_path"
    done
}

vendor=""
instance=""
scan_path=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        -v|--vendor)
            vendor="$2"
            shift 2
            ;;
        -i|--instance)
            instance="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        -*)
            echo "Unknown option: $1"
            exit 1
            ;;
        *)
            if [[ -z "$scan_path" ]]; then
                scan_path="$1"
            else
                echo "Unexpected argument: $1"
                exit 1
            fi
            shift
            ;;
    esac
done

if [[ -z "$instance" ]]; then
    echo "Error: Missing required option -i|-instance (instance type)."
    exit 1
fi

if [[ ! -d "$scan_path" ]]; then
    echo "Error: Scan path '$scan_path' does not exist or is not a directory."
    exit 1
fi

case "${vendor,,}" in
    "alicloud")
        migrate_to_aliCloud "$instance" "$scan_path"
        ;;
    *)
        echo "Error: Unsupported vendor '$vendor'. Only 'aliCloud' is supported."
        exit 1
        ;;
esac
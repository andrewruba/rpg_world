#!/bin/bash

# This script automates the process of activating a conda environment,
# running pycodestyle and pyflakes for linting and code checks.
# Usage:
# 1. Ensure the script is executable: chmod +x scripts/run_linter.sh
# 2. Run the script:
#    - To lint all Python files: ./scripts/run_linter.sh
#    - To lint specific files: ./scripts/run_linter.sh file1.py file2.py

# Activate the conda environment (if not already done by the script)
echo "Activating conda environment: rpg_world_env"
source $(conda info --base)/etc/profile.d/conda.sh
conda activate rpg_world_env

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate conda environment."
    exit 1
fi

# Check if pycodestyle and pyflakes are installed
if ! command -v pycodestyle &> /dev/null || ! command -v pyflakes &> /dev/null
then
    echo "Error: pycodestyle and/or pyflakes are not installed. Please install them."
    exit 1
fi

# Check if any arguments were provided
if [ $# -eq 0 ]; then
    # If no arguments, run linter on all Python files in the current directory and subdirectories
    echo "Running pycodestyle and pyflakes on all Python files in the current directory..."
    pycodestyle .
    pyflakes .
else
    # If arguments are provided, run linter on the specified files
    echo "Running pycodestyle and pyflakes on specified files: $@"
    pycodestyle "$@"
    pyflakes "$@"
fi

# Check if pycodestyle encountered any issues
if [ $? -ne 0 ]; then
    echo "pycodestyle found issues. Please fix them."
else
    echo "pycodestyle check passed with no issues."
fi

# Check if pyflakes encountered any issues
if [ $? -ne 0 ]; then
    echo "pyflakes found issues. Please fix them."
else
    echo "pyflakes check passed with no issues."
fi

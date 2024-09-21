#!/bin/bash

# This script automates the process of activating a conda environment,
# building the package, installing the generated wheel file, and running tests.
# Usage:
# 1. Ensure the script is executable: chmod +x scripts/test.sh
# 2. Run the script:
#    - To run all tests: ./scripts/test.sh
#    - To run specific tests: ./scripts/test.sh tests/test_file.py tests/another_test_file.py

# Run the build and install script
./scripts/build_and_install.sh

# Check if the build was successful
if [ $? -ne 0 ]; then
    echo "Build and install failed. Exiting."
    exit 1
fi

# Activate the environment (if not already done by the script)
echo "Activating conda environment: rpg_world_env"
source $(conda info --base)/etc/profile.d/conda.sh
conda activate rpg_world_env

# Check if activation was successful
if [ $? -ne 0 ]; then
    echo "Error: Failed to activate conda environment."
    exit 1
fi

# Check if any arguments were provided
if [ $# -eq 0 ]; then
    # If no arguments, run all tests in the tests/ folder
    echo "Running all tests in the tests/ folder..."
    pytest tests/
else
    # If arguments are provided, run the specified tests
    echo "Running specified test files: $@"
    pytest "$@"
fi

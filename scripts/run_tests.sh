#!/bin/bash

# This script automates the process of activating a conda environment,
# building the package, installing the generated wheel file, and running tests.
# Usage:
# 1. Ensure the script is executable: chmod +x scripts/run_tests.sh
# 2. Run the script: ./scripts/run_tests.sh

# Run the build and install script
./scripts/build_install.sh

# Activate the environment (if not already done by the script) and run tests
conda activate rpg_world_env
pytest tests/
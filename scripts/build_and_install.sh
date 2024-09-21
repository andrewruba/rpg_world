#!/bin/bash

# This script automates the process of activating a conda environment,
# building the package, and installing the generated wheel file.
# Usage:
# 1. Ensure the script is executable: chmod +x scripts/build_and_install.sh
# 2. Run the script: ./scripts/build_and_install.sh

# Define the conda environment and package name
CONDA_ENV_NAME="rpg_world_env"
PACKAGE_NAME="rpg_world"

# Step 1: Activate the conda environment
echo "Activating the conda environment: $CONDA_ENV_NAME"
source $(conda info --base)/etc/profile.d/conda.sh
conda activate $CONDA_ENV_NAME

if [ $? -ne 0 ]; then
    echo "Error: Failed to activate conda environment $CONDA_ENV_NAME."
    exit 1
fi

# Step 2: Build the package (sdist and bdist_wheel)
echo "Building the package..."
python setup.py sdist bdist_wheel

if [ $? -ne 0 ]; then
    echo "Error: Package build failed."
    exit 1
fi

# Step 3: Install the latest wheel file
echo "Installing the package..."
pip install dist/${PACKAGE_NAME}-*.whl --force-reinstall

if [ $? -ne 0 ]; then
    echo "Error: Failed to install the package."
    exit 1
fi

echo "Package built and installed successfully!"

#!/bin/bash

# Step 1: Build the package
echo "Building the package..."
python -m build

# Check if build was successful
if [ $? -ne 0 ]; then
    echo "Build failed, exiting."
    exit 1
fi

# Step 2: Create the virtual environment
echo "Creating the virtual environment..."
python -m venv .venv

# Step 3: Install the built package
echo "Installing the built package..."
source .venv/Scripts/activate
VERSION=$(awk -F'"' '/version =/ {print $2}' pyproject.toml)
pip install "./dist/xmi-$VERSION-py3-none-any.whl"

# Running tests
echo "Running tests..."
pytest after_install_tests/
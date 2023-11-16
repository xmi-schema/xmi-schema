#!/bin/bash

# Exit if any command fails
set -e

# Build the package
echo "Building the package..."
python -m build

# Create the virtual environment
echo "Creating the virtual environment..."
python -m venv .venv

# Activate the virtual environment and install the package
source .venv/bin/activate
echo "Activated Virtual environment"

echo "Current directory: $(pwd)"

# Extract the version from pyproject.toml and install the package

# Path to your pyproject.toml file
FILE_PATH="pyproject.toml"

# Variable to store the version
VERSION=""

# Read each line from the file
while IFS= read -r line; do
    echo "Reading line: $line"

    # Check if the line contains 'version ='
    if [[ $line == *"version ="* ]]; then
        # Extract the version number
        VERSION=$(echo $line | awk -F '"' '{print $2}')
        echo "Found version line: $VERSION"
        break
    fi
done < "$FILE_PATH"

if [ -z "$VERSION" ]; then
    echo "Version not found."
else
    echo "Extracted Version: $VERSION"

    # Install with pip
    pip install "dist/xmi-$VERSION-py3-none-any.whl"
fi

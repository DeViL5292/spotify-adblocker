#!/bin/bash

# Clone the repository
git clone https://github.com/yourusername/spotify-adblocker.git

# Change to the repository directory
cd spotify-adblocker

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the adblocker script
python adblocker.py

#!/bin/bash

# Check if the script is running in bash
if [ -z "$BASH_VERSION" ]; then
  echo "This script requires bash. Switching to bash..."
  exec bash "$0" "$@"
fi

# Install Python 3 and pip if not installed
echo "Installing Python 3 and pip..."
sudo apt-get install python3 python3-pip python3-venv -y

# Ensure python3 is used by default
echo "Using python3 and pip3 for installation..."
alias python=python3
alias pip=pip3

# Create a Python virtual environment in the home directory (no permission issues)
echo "Creating a Python virtual environment..."
python3 -m venv ~/venv

# Activate the virtual environment
echo "Activating the virtual environment..."
source ~/venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Install JADX
echo "Installing JADX..."
if ! command -v jadx &> /dev/null
then
    wget https://github.com/skylot/jadx/releases/download/v1.3.0/jadx-1.3.0-bin.zip -O /tmp/jadx.zip
    unzip /tmp/jadx.zip -d /opt/
    sudo ln -s /opt/jadx-1.3.0/bin/jadx /usr/local/bin/jadx
    echo "JADX installed successfully."
else
    echo "JADX is already installed."
fi

# Install Apktool
echo "Installing Apktool..."
if ! command -v apktool &> /dev/null
then
    wget https://github.com/iBotPeaches/Apktool/releases/download/v2.6.0/apktool_2.6.0.jar -O /opt/apktool.jar
    echo "java -jar /opt/apktool.jar" > /usr/local/bin/apktool
    chmod +x /usr/local/bin/apktool
    echo "Apktool installed successfully."
else
    echo "Apktool is already installed."
fi

# Install FlowDroid (Java required)
echo "Installing FlowDroid..."
if [ ! -f "/opt/flowdroid.jar" ]; then
    wget https://github.com/secure-software-engineering/FlowDroid/releases/download/v1.4/flowdroid-1.4.jar -O /opt/flowdroid.jar
    echo "FlowDroid installed successfully."
else
    echo "FlowDroid is already installed."
fi

# Install OWASP Dependency-Check
echo "Installing OWASP Dependency-Check..."
if ! command -v dependency-check &> /dev/null
then
    wget https://github.com/jeremylong/DependencyCheck/releases/download/v6.3.1/dependency-check-6.3.1-release.zip -O /tmp/dependency-check.zip
    unzip /tmp/dependency-check.zip -d /opt/
    sudo ln -s /opt/dependency-check/bin/dependency-check.sh /usr/local/bin/dependency-check
    echo "OWASP Dependency-Check installed successfully."
else
    echo "OWASP Dependency-Check is already installed."
fi

# Finished
echo "Setup complete! All dependencies have been installed."
echo "To activate the virtual environment, run: source ~/venv/bin/activate"

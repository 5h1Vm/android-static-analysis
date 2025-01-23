# Android Static Analysis Tool

This is a simple Python-based tool designed to perform static analysis on Android APK files. It uses a combination of tools such as Androguard, JADX, Apktool, FlowDroid, and OWASP Dependency-Check to analyze APKs for dangerous permissions, exported components, data flow, and more.

## Features

- **APK Decompilation:** Decompile APKs using JADX and Apktool.
- **Static Analysis:** Use Androguard for static analysis and permission checks.
- **Manifest Analysis:** Check for dangerous permissions and exported components.
- **Data Flow Analysis:** Analyze the APK using FlowDroid.
- **Dependency Check:** Identify vulnerabilities in third-party libraries using OWASP Dependency-Check.

## Requirements

- Python 3.x
- Java 8+ (for FlowDroid)
- `JADX`, `Apktool`, `FlowDroid`, and `OWASP Dependency-Check` (the script will install these)

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/5h1Vm/android-static-analysis
cd android-static-analysis
```

### 2. Run the Setup Script

The `setup.sh` script will install all the necessary dependencies and set up a Python virtual environment for the project.

```bash
chmod +x setup.sh
./setup.sh
```

This will:

- Install system dependencies for `JADX`, `Apktool`, `FlowDroid`, and `OWASP Dependency-Check`.
- Create and activate a Python virtual environment.
- Install the required Python packages (listed in `requirements.txt`).

### 3. Activate the Virtual Environment

After running the setup script, activate the virtual environment:

```bash
source ~/venv/bin/activate
```

You should see the terminal prompt change to indicate that the virtual environment is active (e.g., `(venv)`).

### 4. Running the Tool

Once the virtual environment is activated, run the tool by executing the following command:

```bash
python3 apk_analyzer.py
```

### 5. Using the Tool

- The tool will prompt you to enter the path to the APK file you want to analyze.
- It will ask for different analysis steps, such as decompiling the APK, performing static analysis, checking for dangerous permissions, etc.
- The tool will output the analysis results to the terminal.

## Directory Structure

```plaintext
├── apk_analyzer.py   # Main script
├── requirements.txt  # Python dependencies
├── output_code/      # Decompiled source code
├── output_resources/ # Decompiled resources
├── reports/          # JSON reports
└── flowdroid.jar     # FlowDroid (if applicable)
```

## Troubleshooting

- If you encounter any issues with installing dependencies, make sure you have the required system tools and libraries installed. You may need to install `build-essential` or other dependencies depending on your system.
---

## Acknowledgments
- [JADX](https://github.com/skylot/jadx)
- [Apktool](https://ibotpeaches.github.io/Apktool/)
- [Androguard](https://androguard.readthedocs.io)
- [FlowDroid](https://github.com/secure-software-engineering/FlowDroid)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)

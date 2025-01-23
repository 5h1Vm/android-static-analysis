# Android APK Static Analysis Tool

This tool helps analyze Android APK files for security issues, dangerous permissions, and vulnerabilities. It uses popular open-source tools to decompile APKs, perform static analysis, and more.

---

## Features
- **Decompile APK**: Extract source code and resources.
- **Static Analysis**: Detect dangerous permissions and exported components.
- **Data Flow Analysis**: Analyze data flow with FlowDroid.
- **Dependency Scanning**: Check for vulnerabilities in dependencies.

---

## Getting Started

### Prerequisites
Make sure you have the following tools installed:
- **Python 3.x**
- **JADX** (for decompiling APK)
- **Apktool** (for resource decompiling)
- **Java** (for FlowDroid)
- **OWASP Dependency-Check**

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/android-apk-static-analysis.git
   cd android-apk-static-analysis
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the tool:
```bash
python3 apk_analyzer.py
```

Follow the prompts to select which analyses to run (e.g., decompile APK, check for dangerous permissions, perform FlowDroid analysis).

---

## Directory Structure

```plaintext
├── apk_analyzer.py   # Main script
├── requirements.txt  # Python dependencies
├── output_code/      # Decompiled source code
├── output_resources/ # Decompiled resources
├── reports/          # JSON reports
└── flowdroid.jar     # FlowDroid (if applicable)
```

---

## Acknowledgments
- [JADX](https://github.com/skylot/jadx)
- [Apktool](https://ibotpeaches.github.io/Apktool/)
- [Androguard](https://androguard.readthedocs.io)
- [FlowDroid](https://github.com/secure-software-engineering/FlowDroid)
- [OWASP Dependency-Check](https://owasp.org/www-project-dependency-check/)

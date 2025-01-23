import os
import subprocess
import json
from androguard.misc import AnalyzeAPK
import xml.etree.ElementTree as ET

# Define dangerous permissions for checks
dangerous_permissions = ['android.permission.SEND_SMS', 'android.permission.INTERNET', 'android.permission.READ_SMS']

# Utility function for verbose output
def verbose_print(message, verbose):
    if verbose:
        print(f"[INFO]: {message}")

# Function to decompile APK using JADX
def decompile_apk(apk_path, output_dir, verbose=False):
    verbose_print(f"Decompiling APK: {apk_path} using JADX", verbose)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cmd = f'jadx -d {output_dir} {apk_path}'
    subprocess.run(cmd, shell=True)
    verbose_print(f"Decompiled APK output saved to {output_dir}", verbose)

# Function to decompile APK resources using Apktool

def decompile_resources(apk_path, output_dir, verbose=False):
    verbose_print(f"Decompiling APK resources: {apk_path} using Apktool", verbose)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    cmd = f'apktool -f d {apk_path} -o {output_dir}'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
    else:
        verbose_print(f"Resources decompiled to {output_dir}", verbose)
        # Check if AndroidManifest.xml exists
        manifest_path = os.path.join(output_dir, "AndroidManifest.xml")
        if not os.path.exists(manifest_path):
            print(f"Error: AndroidManifest.xml not found in {output_dir}")
        else:
            verbose_print(f"AndroidManifest.xml found in {output_dir}", verbose)


# def decompile_resources(apk_path, output_dir, verbose=False):
#     verbose_print(f"Decompiling APK resources: {apk_path} using Apktool", verbose)
#     if not os.path.exists(output_dir):
#         os.makedirs(output_dir)
#     cmd = f'apktool d {apk_path} -o {output_dir}'
#     subprocess.run(cmd, shell=True)
#     verbose_print(f"Resources decompiled to {output_dir}", verbose)

# Function to perform static analysis with Androguard
def androguard_analysis(apk_path, verbose=False):
    verbose_print(f"Performing static analysis on {apk_path} using Androguard", verbose)
    a, d, dx = AnalyzeAPK(apk_path)
    permissions_used = a.get_permissions()
    verbose_print(f"Permissions used in APK: {permissions_used}", verbose)

    # Dangerous permission check
    for perm in permissions_used:
        if perm in dangerous_permissions:
            verbose_print(f"Dangerous permission detected: {perm}", verbose)

# Function to parse and analyze AndroidManifest.xml
def analyze_manifest(manifest_file, verbose=False):
    verbose_print(f"Analyzing AndroidManifest.xml: {manifest_file}", verbose)
    tree = ET.parse(manifest_file)
    root = tree.getroot()

    # Check for dangerous permissions
    for elem in root.iter('uses-permission'):
        permission = elem.get('{http://schemas.android.com/apk/res/android}name')
        if permission in dangerous_permissions:
            verbose_print(f"Dangerous permission found in manifest: {permission}", verbose)

    # Check for exported components
    for elem in root.iter('activity'):
        exported = elem.get('{http://schemas.android.com/apk/res/android}exported')
        if exported == 'true':
            verbose_print(f"Exported activity found: {elem.get('{http://schemas.android.com/apk/res/android}name')}", verbose)

# Function to run FlowDroid for data flow analysis
def flowdroid_analysis(apk_path, flowdroid_jar, android_platforms, verbose=False):
    verbose_print(f"Running FlowDroid analysis on {apk_path}", verbose)
    try:
        cmd = f'java -jar {flowdroid_jar} -a {apk_path} -p {android_platforms} -s SourcesAndSinks.txt'
        subprocess.run(cmd, shell=True)
        verbose_print("FlowDroid analysis completed.", verbose)
    except Exception as e:
        print(f"[ERROR]: Failed to run FlowDroid. Details: {e}")


# Function to perform dependency check using OWASP Dependency-Check
def dependency_check(apk_path, verbose=False):
    verbose_print(f"Running OWASP Dependency-Check on {apk_path}", verbose)
    try:
        cmd = f'/opt/dependency-check/bin/dependency-check.sh --project android_project --scan {apk_path} --format JSON --out reports/'
        subprocess.run(cmd, shell=True)
        verbose_print("Dependency check completed and report saved in reports/ directory", verbose)
    except Exception as e:
        print(f"[ERROR]: Failed to run Dependency-Check. Details: {e}")


# Function to generate a report in JSON format
def generate_report(findings, output_file, verbose=False):
    verbose_print(f"Generating report and saving to {output_file}", verbose)
    with open(output_file, 'w') as f:
        json.dump(findings, f, indent=4)
    verbose_print("Report generation completed.", verbose)

# Function to gather user input
def get_user_input():
    print("Welcome to the Static Analysis Tool for Android!")
    apk_path = input("Enter the path to the APK file: ")
    verbose = input("Enable verbose mode? (yes/no): ").lower() == 'yes'
    
    print("\nChoose the analysis steps (type 'yes' or 'no'):")
    decompile_apk_choice = input("1. Decompile APK using JADX? (yes/no): ").lower() == 'yes'
    decompile_resources_choice = input("2. Decompile APK resources using Apktool? (yes/no): ").lower() == 'yes'
    static_analysis_choice = input("3. Perform static analysis using Androguard? (yes/no): ").lower() == 'yes'
    manifest_analysis_choice = input("4. Analyze AndroidManifest.xml? (yes/no): ").lower() == 'yes'
    flowdroid_choice = input("5. Perform data flow analysis using FlowDroid? (yes/no): ").lower() == 'yes'
    dependency_check_choice = input("6. Perform dependency check using OWASP? (yes/no): ").lower() == 'yes'
    
    return {
        "apk_path": apk_path,
        "verbose": verbose,
        "decompile_apk": decompile_apk_choice,
        "decompile_resources": decompile_resources_choice,
        "static_analysis": static_analysis_choice,
        "manifest_analysis": manifest_analysis_choice,
        "flowdroid": flowdroid_choice,
        "dependency_check": dependency_check_choice
    }

# Main function to run the tool
def main():
    user_input = get_user_input()
    
    apk_path = user_input['apk_path']
    verbose = user_input['verbose']
    
    if user_input['decompile_apk']:
        decompile_apk(apk_path, "output_code/", verbose)
    
    if user_input['decompile_resources']:
        decompile_resources(apk_path, "output_resources/", verbose)
    
    if user_input['static_analysis']:
        androguard_analysis(apk_path, verbose)
    
    if user_input['manifest_analysis']:
        analyze_manifest("output_resources/AndroidManifest.xml", verbose)
    
    if user_input['flowdroid']:
        flowdroid_jar = "flowdroid.jar"
        android_platforms = "/opt/android-sdk/platforms/"
        flowdroid_analysis(apk_path, flowdroid_jar, android_platforms, verbose)
    
    if user_input['dependency_check']:
        dependency_check(apk_path, verbose)

    print("\nAll selected analyses are complete.")

if __name__ == "__main__":
    main()

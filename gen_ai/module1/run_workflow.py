#!/usr/bin/env python3
"""
Workflow Runner - Runs the complete text to binary to decimal to BPE workflow
"""
import os
import subprocess
import sys

def run_command(command):
    """Run a command and print its output"""
    print(f"Running: {' '.join(command)}")
    result = subprocess.run(command, capture_output=True, text=True)
    
    print("STDOUT:")
    print(result.stdout)
    
    if result.stderr:
        print("STDERR:")
        print(result.stderr)
    
    print("-" * 50)
    return result.returncode == 0

def main():
    """Run the complete workflow"""
    # Define file paths
    input_text_file = "training_data/raw_text.txt"
    binary_file = "training_data/binary.txt"
    decimal_file = "training_data/numeric.txt"
    encoded_file = "training_data/encoding.txt"
    
    # Ensure we're in the right directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    
    print(f"Working directory: {os.getcwd()}")
    
    # Step 1: Convert text to binary
    print("\nSTEP 1: Converting text to binary")
    if not run_command([sys.executable, "binary_converter.py", input_text_file, binary_file]):
        print("Failed to convert text to binary. Exiting.")
        return
    
    # Check binary file content
    print("\nChecking binary file content:")
    with open(binary_file, 'r') as f:
        binary_content = f.read(200)  # Read first 200 chars for preview
        print(f"First 200 chars: {binary_content}...")
        print(f"Total length: {os.path.getsize(binary_file)} bytes")
    
    # Step 2: Convert binary to decimal
    print("\nSTEP 2: Converting binary to decimal")
    if not run_command([sys.executable, "binary_to_decimal.py", binary_file, decimal_file]):
        print("Failed to convert binary to decimal. Exiting.")
        return
    
    # Check decimal file content
    print("\nChecking decimal file content:")
    with open(decimal_file, 'r') as f:
        decimal_content = f.read(200)  # Read first 200 chars for preview
        print(f"First 200 chars: {decimal_content}...")
        print(f"Total length: {os.path.getsize(decimal_file)} bytes")
    
    # Step 3: Apply BPE encoding
    print("\nSTEP 3: Applying BPE encoding")
    if not run_command([sys.executable, "bpe_encoder.py", decimal_file, encoded_file, "--merges", "20"]):
        print("Failed to apply BPE encoding. Exiting.")
        return
    
    # Check encoded file content
    print("\nChecking encoded file content:")
    with open(encoded_file, 'r') as f:
        encoded_content = f.read(200)  # Read first 200 chars for preview
        print(f"First 200 chars: {encoded_content}...")
        print(f"Total length: {os.path.getsize(encoded_file)} bytes")
    
    print("\nWorkflow completed successfully!")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Binary to Decimal Converter - Converts binary representation to decimal values
"""
import argparse
import os
import re

def binary_to_decimal(binary_str):
    """
    Convert a space-separated string of binary values to decimal values.
    
    Args:
        binary_str (str): Space-separated binary values
        
    Returns:
        list: List of decimal values
    """
    decimal_values = []
    
    # Clean up input - remove any non-space, non-binary characters
    # This helps with newlines and other formatting
    cleaned_str = re.sub(r'[^01\s]', '', binary_str)
    
    # Split by whitespace (handles spaces, tabs, newlines)
    binary_values = re.split(r'\s+', cleaned_str.strip())
    
    # Filter out empty strings
    binary_values = [b for b in binary_values if b]
    
    print(f"Found {len(binary_values)} binary values to process")
    
    for binary in binary_values:
        # Ensure it's a valid binary number (only 0s and 1s)
        if re.match(r'^[01]+$', binary):
            try:
                # Convert binary to decimal
                decimal = int(binary, 2)
                decimal_values.append(decimal)
            except ValueError:
                print(f"Warning: Could not convert binary value: {binary}")
        else:
            print(f"Warning: Skipping invalid binary value: {binary}")
    
    return decimal_values

def process_file(input_file, output_file):
    """
    Process the input file containing binary values and write decimal values to output file
    
    Args:
        input_file (str): Path to the input file with binary values
        output_file (str): Path to the output file for decimal values
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return False
            
        # Read from input file
        with open(input_file, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
        
        print(f"Read {len(content)} characters from input file")
            
        # Convert to decimal
        decimal_values = binary_to_decimal(content)
        
        if not decimal_values:
            print("Error: No valid binary values were found in the input file.")
            print("Make sure the file contains binary values (only 0s and 1s).")
            return False
            
        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f_out:
            # Write each decimal value with a space separator
            for value in decimal_values:
                f_out.write(f"{value} ")
            
        print(f"Successfully converted binary values from '{input_file}' to decimal values.")
        print(f"Output saved to '{output_file}'.")
        print(f"Converted {len(decimal_values)} binary values.")
        return True
        
    except Exception as e:
        print(f"Error processing files: {str(e)}")
        return False

def main():
    """Main function to handle command line arguments and process files"""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert binary values to decimal values')
    parser.add_argument('input_file', help='Path to the input file with binary values')
    parser.add_argument('output_file', help='Path to the output file for decimal values')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process the files
    process_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()

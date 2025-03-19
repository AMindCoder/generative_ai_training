#!/usr/bin/env python3
"""
Binary Converter - Converts text to binary representation
"""
import argparse
import os

def text_to_binary(text):
    """
    Convert a string of text to its binary representation.
    Each character is converted to its ASCII value and then to binary.
    
    Args:
        text (str): The input text to convert
        
    Returns:
        str: Space-separated binary representation of each character
    """
    binary_result = []
    
    for char in text:
        # Get ASCII value of character
        ascii_value = ord(char)
        
        # Convert ASCII to binary (removing '0b' prefix that bin() adds)
        binary_value = bin(ascii_value)[2:]
        
        # Ensure 8-bit representation (standard ASCII)
        binary_value = binary_value.zfill(8)
        
        binary_result.append(binary_value)
    
    # Join all binary values with spaces
    return ' '.join(binary_result)

def process_file(input_file, output_file):
    """
    Process the input file and write binary representation to output file
    
    Args:
        input_file (str): Path to the input text file
        output_file (str): Path to the output file for binary representation
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return False
            
        # Read from input file
        with open(input_file, 'r', encoding='utf-8') as f_in:
            content = f_in.read()
            
        # Convert to binary
        binary_output = text_to_binary(content)
        
        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f_out:
            f_out.write(binary_output)
            
        print(f"Successfully converted '{input_file}' to binary representation.")
        print(f"Output saved to '{output_file}'.")
        return True
        
    except Exception as e:
        print(f"Error processing files: {str(e)}")
        return False

def main():
    """Main function to handle command line arguments and process files"""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Convert text file to binary representation')
    parser.add_argument('input_file', help='Path to the input text file')
    parser.add_argument('output_file', help='Path to the output file for binary representation')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process the files
    process_file(args.input_file, args.output_file)

if __name__ == "__main__":
    main()

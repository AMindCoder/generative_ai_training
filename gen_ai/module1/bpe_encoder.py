#!/usr/bin/env python3
"""
Byte Pair Encoding (BPE) Algorithm - Compresses decimal values using BPE
"""
import argparse
import os
import json
from collections import Counter, defaultdict

class BytePairEncoder:
    """
    Implements the Byte Pair Encoding algorithm for compression
    """
    def __init__(self, num_merges=10):
        """
        Initialize the BPE encoder
        
        Args:
            num_merges (int): Number of merge operations to perform
        """
        self.num_merges = num_merges
        self.vocab = {}  # Maps pairs to new symbols
        self.next_symbol = 256  # Start new symbols after ASCII range
        self.merges = []  # List of merges performed
    
    def get_stats(self, data):
        """
        Count frequency of adjacent pairs in the data
        
        Args:
            data (list): List of integers (decimal values)
            
        Returns:
            Counter: Frequencies of adjacent pairs
        """
        pairs = Counter()
        for i in range(len(data) - 1):
            pair = (data[i], data[i + 1])
            pairs[pair] += 1
        return pairs
    
    def merge_data(self, data, pair, new_symbol):
        """
        Replace all occurrences of pair with new_symbol in data
        
        Args:
            data (list): List of integers
            pair (tuple): Pair to replace (a, b)
            new_symbol (int): New symbol to use as replacement
            
        Returns:
            list: Updated data with pairs replaced
        """
        new_data = []
        i = 0
        while i < len(data):
            if i < len(data) - 1 and (data[i], data[i + 1]) == pair:
                new_data.append(new_symbol)
                i += 2
            else:
                new_data.append(data[i])
                i += 1
        return new_data
    
    def train(self, data):
        """
        Train the BPE model on the data
        
        Args:
            data (list): List of integers to compress
            
        Returns:
            list: Compressed data
        """
        # Make a copy of the data to work with
        working_data = data.copy()
        
        # Perform merges
        for _ in range(self.num_merges):
            # Get pair frequencies
            pairs = self.get_stats(working_data)
            if not pairs:
                break
                
            # Find most frequent pair
            most_frequent = max(pairs.items(), key=lambda x: x[1])[0]
            
            # Assign a new symbol to this pair
            self.vocab[most_frequent] = self.next_symbol
            
            # Record the merge
            self.merges.append((most_frequent, self.next_symbol))
            
            # Replace all occurrences of the pair
            working_data = self.merge_data(working_data, most_frequent, self.next_symbol)
            
            # Increment for next symbol
            self.next_symbol += 1
        
        return working_data
    
    def encode(self, data):
        """
        Encode data using the trained BPE model
        
        Args:
            data (list): List of integers to encode
            
        Returns:
            list: Encoded data
        """
        # Make a copy of the data to work with
        encoded_data = data.copy()
        
        # Apply all merges in order
        for pair, new_symbol in self.merges:
            encoded_data = self.merge_data(encoded_data, pair, new_symbol)
        
        return encoded_data
    
    def save_model(self, filename):
        """
        Save the BPE model to a file
        
        Args:
            filename (str): Path to save the model
        """
        model = {
            'vocab': {str(k): v for k, v in self.vocab.items()},
            'merges': [(list(pair), symbol) for pair, symbol in self.merges],
            'next_symbol': self.next_symbol
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(model, f, indent=2)
    
    def load_model(self, filename):
        """
        Load a BPE model from a file
        
        Args:
            filename (str): Path to the model file
        """
        with open(filename, 'r', encoding='utf-8') as f:
            model = json.load(f)
        
        self.vocab = {tuple(map(int, k.strip('()').split(', '))): v for k, v in model['vocab'].items()}
        self.merges = [(tuple(pair), symbol) for pair, symbol in model['merges']]
        self.next_symbol = model['next_symbol']

def process_file(input_file, output_file, model_file=None, num_merges=10):
    """
    Process the input file containing decimal values and write BPE encoded values to output file
    
    Args:
        input_file (str): Path to the input file with decimal values
        output_file (str): Path to the output file for BPE encoded values
        model_file (str, optional): Path to save/load the BPE model
        num_merges (int): Number of merge operations to perform
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: Input file '{input_file}' not found.")
            return False
            
        # Read decimal values from input file
        with open(input_file, 'r', encoding='utf-8') as f_in:
            content = f_in.read().strip()
        
        # Parse decimal values from space-separated string
        decimal_values = []
        for value in content.split():
            try:
                decimal_values.append(int(value))
            except ValueError:
                print(f"Warning: Skipping invalid decimal value: {value}")
        
        print(f"Read {len(decimal_values)} decimal values from input file")
        
        if not decimal_values:
            print("Error: No valid decimal values found in the input file.")
            return False
        
        # Create and train BPE encoder
        encoder = BytePairEncoder(num_merges=num_merges)
        
        # Train or load model
        if model_file and os.path.exists(model_file):
            print(f"Loading BPE model from {model_file}")
            encoder.load_model(model_file)
            encoded_data = encoder.encode(decimal_values)
        else:
            print(f"Training BPE model with {num_merges} merges")
            encoded_data = encoder.train(decimal_values)
            if model_file:
                encoder.save_model(model_file)
                print(f"Saved BPE model to {model_file}")
        
        # Write encoded data to output file
        with open(output_file, 'w', encoding='utf-8') as f_out:
            for value in encoded_data:
                f_out.write(f"{value} ")
        
        # Calculate compression ratio
        original_size = len(decimal_values)
        compressed_size = len(encoded_data)
        compression_ratio = (original_size - compressed_size) / original_size * 100 if original_size > 0 else 0
        
        print(f"Successfully encoded decimal values from '{input_file}' using BPE.")
        print(f"Output saved to '{output_file}'.")
        print(f"Original size: {original_size} values")
        print(f"Compressed size: {compressed_size} values")
        print(f"Compression ratio: {compression_ratio:.2f}%")
        
        return True
        
    except Exception as e:
        print(f"Error processing files: {str(e)}")
        return False

def main():
    """Main function to handle command line arguments and process files"""
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Compress decimal values using Byte Pair Encoding')
    parser.add_argument('input_file', help='Path to the input file with decimal values')
    parser.add_argument('output_file', help='Path to the output file for BPE encoded values')
    parser.add_argument('--model', help='Path to save/load the BPE model', default=None)
    parser.add_argument('--merges', type=int, help='Number of merge operations to perform', default=10)
    
    # Parse arguments
    args = parser.parse_args()
    
    # Process the files
    process_file(args.input_file, args.output_file, args.model, args.merges)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
#
# File: twospaces.py - change 4 space indentation to 2 spaces
# Usage: twospaces.py <inputFile> <outputFile>
#
import sys

def convert_indentation(input_file: str, output_file: str):
  try:
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
      for line in infile:
        new_line = line.replace("    ", "  ")
        outfile.write(new_line)
    print(f"Indentation converted successfully. Output saved to: {output_file}")
  except FileNotFoundError:
    print(f"Error: File '{input_file}' not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python spaces.py <input_file> <output_file>")
  else:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    convert_indentation(input_file, output_file)


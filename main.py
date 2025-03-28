#!/usr/bin/env python3
"""
BookBot - A simple tool for analyzing text files.
"""
from stats import get_num_words, get_number_of_characters, get_chars_by_frequency
import sys
from typing import Dict, List, Tuple

def get_book_text(file_path: str) -> str:
    """
    Read and return the contents of a text file.
    
    Args:
        file_path: Path to the text file to read
        
    Returns:
        The text content of the file
        
    Raises:
        FileNotFoundError: If the specified file doesn't exist
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def generate_report(book_path: str, text: str) -> None:
    """
    Generate and print a report with statistics about the text.
    
    Args:
        book_path: Path to the analyzed book (for reporting)
        text: The text content to analyze
    """
    # Get statistics
    num_words = get_num_words(text)
    character_counts = get_number_of_characters(text)
    sorted_characters = get_chars_by_frequency(character_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char, count in sorted_characters:
        if char.isalpha():  # Only print alphabetic characters
            print(f"The '{char}' character appears {count} times")
    
    print("============= END ===============")

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    generate_report(book_path, text)

if __name__ == "__main__":
    main()
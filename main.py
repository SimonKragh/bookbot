from stats import get_num_words, get_number_of_characters, get_chars_by_frequency
import sys 

def get_book_text(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    character_counts = get_number_of_characters(text)


    #Print the report 
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")

    sorted_characters = get_chars_by_frequency(character_counts)
    for char, count in sorted_characters:
        print(f"{char}: {count}")

    print("============= END ===============")

if __name__ == "__main__":
    main()

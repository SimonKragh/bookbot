from stats import get_num_words

def get_book_text(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

def main():
    num_words = get_num_words(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document ")


if __name__ == "__main__":
    main()

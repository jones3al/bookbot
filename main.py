import sys
from stats import get_book_text, count_words, count_each_character, sorted_character_counts

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    file_contents = get_book_text(book_path)
    print("----------- Word Count ----------")
    print(f"Found {count_words(file_contents)} total words.")
    print("------- Character Count --------")

    char_counts = count_each_character(file_contents)
    sorted_char_counts = sorted_character_counts(char_counts)
    for char, count in sorted_char_counts.items():
        print(f"{char}: {count}")
    print("============= END ===============")


main()

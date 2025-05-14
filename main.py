import sys
from curses.ascii import isalpha
from stats import count_words, count_char_freq, sorted_char_freq_dict


def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>`")
        sys.exit(1)

    # book_name = "frankenstein.txt"
    book_name = sys.argv[1]
    book_text = get_book_text(book_name)
    word_count = count_words(book_text)
    char_count = count_char_freq(book_text)
    char_count_sorted_dict = sorted_char_freq_dict(char_count)
    # print(f"{word_count} words found in the document")
    # print(char_count)
    print(f"""
============ BOOKBOT ============
Analyzing book found at books/{book_name}...
----------- Word Count ----------""")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in char_count_sorted_dict:
        if isalpha(i["char"]):
            print(f"{i['char']}: {i['num']}")


if __name__ == "__main__":
    main()

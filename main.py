
import sys

from stats import (
    get_num_words,
    chars_dict_to_sorted_list,
    get_chars_dict,
)


def main():
    
    if len(sys.argv) != 2:              # Validating the command line args
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)          # <-- actually load the text
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print_report(path, num_words, chars_sorted_list)

def get_book_text(path):        # Grabs the file and reads it
    with open(path) as f:
        return f.read()


def print_report(path, num_words, chars_sorted_list):  #Banner messages in output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:                      # For loop to order and sort the characters and numbers
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



  


main()
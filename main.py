import sys
from stats import get_word_count
from stats import find_char_frequency
from stats import char_dict_sorted


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    text = get_book_text(filepath)
    count = get_word_count(text)
    dict = find_char_frequency(text)
    sorted_list = char_dict_sorted(dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("---------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


def get_book_text(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print(f"Error: The file {filepath} does not exist.")
        return ""
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return ""


main()

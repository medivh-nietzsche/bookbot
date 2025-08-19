import sys
from stats import count_words
from stats import get_char_occurrences
from stats import sort_occurences_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
#    print(file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = get_char_occurrences(text)
    sorted_char_dict_list = sort_occurences_dict(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------") 
    for dict in sorted_char_dict_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
    

main()

"""def main():
    get_book_text("books/frankenstein.txt")

main()"""


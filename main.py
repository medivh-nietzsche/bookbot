from stats import count_words
from stats import get_char_occurrences
from stats import sort_occurences_dict

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
#    print(file_contents)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    char_dict = get_char_occurrences(text)
    sorted_char_dict_list = sort_occurences_dict(char_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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


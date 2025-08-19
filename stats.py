def count_words(text):
    words = text.split()
    return len(words)

def get_char_occurrences(text):
    lowered_text = text.lower()
    chars = list(lowered_text)
    char_occurrences = {}

    for char in chars:
        if char in char_occurrences:
            char_occurrences[char] += 1
        else:
            char_occurrences[char] = 1

    return char_occurrences

def sort_on(items):
        return items["num"]

def sort_occurences_dict(dict):
    char_dict_list = []
    for char in dict:
        char_dict_list.append({"char": char, "num": dict[char]})
    char_dict_list.sort(reverse=True, key=sort_on)
    return char_dict_list
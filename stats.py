def get_word_count(text):
    words = text.split()
    number_of_words = len(words)
    return number_of_words


def find_char_frequency(text):
    char_frequency = {}
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char = char.lower()  # Normalize to lowercase
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
    return char_frequency


def sort_on(dict):
    return dict["num"]


def char_dict_sorted(dictionary):
    new_list = []
    for char in dictionary:
        new_list.append({"char": char, "num": dictionary[char]})
    new_list.sort(reverse=True, key=sort_on)
    return new_list

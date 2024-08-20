from english_words import get_english_words_set
from itertools import permutations 

def find_anagrams_func(string_in, desired_number_of_words = 2):
    """
    This function will:
        Find all possible anagrams of a word that are english words
    This function takes arguments:
        string_in: a word that needs to have anagrams made from it.
        desired_number_of_words: how many words must be in the anagrams.
    returns:
        a list of lists of the possible desired number of words anagrams of the provided word
    """
    no_of_spaces = desired_number_of_words - 1
    word_to_be_split = string_in
    word_to_be_split += " " * no_of_spaces
    list_of_tuple_of_shuffled_chars = list(permutations(word_to_be_split))
    all_the_words = get_english_words_set(["gcide"], lower=True)
    checked_and_formatted = set()
    # if "gets" in all_the_words:
    #     print(True)
    for tuple_of_chars in list_of_tuple_of_shuffled_chars:
        my_string = "".join(tuple_of_chars)
        if desired_number_of_words == 1 and my_string in all_the_words:
            checked_and_formatted.add(tuple(my_string))
        else:
            little_strings = my_string.split(" ")
            all_valid_words = True
            for i in little_strings:
                if i not in all_the_words:
                    all_valid_words = False
            if all_valid_words:
                print(f"{tuple_of_chars}\n{my_string}\n{little_strings}\nvalid")
                checked_and_formatted.add(tuple(little_strings))
        
    checked_and_formatted = list(checked_and_formatted)
    print(checked_and_formatted)
    return checked_and_formatted



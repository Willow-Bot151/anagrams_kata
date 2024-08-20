import pytest 
from anagrams_of_string import find_anagrams_func

def test_func_takes_string():
    test_string_in = ""
    find_anagrams_func(test_string_in)

def test_func_returns_list_of_list_of_strings():
    test_string_in = "testing"
    assert isinstance(find_anagrams_func(test_string_in),list)
    assert isinstance(find_anagrams_func(test_string_in)[0],list)
    assert isinstance(find_anagrams_func(test_string_in)[0][0],str)

def test_func_returns_list_of_correct_num_of_words():
    test_string_in = "testing"
    desired_num_of_words_1 = 1
    desired_num_of_words_2 = 2
    for i in find_anagrams_func(test_string_in, desired_num_of_words_1):
        assert len(i) == desired_num_of_words_1
    for i in find_anagrams_func(test_string_in, desired_num_of_words_2):
        assert len(i) == desired_num_of_words_2

def test_func_small_word():
    test_string = "abcdef"
    assert find_anagrams_func(test_string,1) == 0

def test_func_returns_correct_words():
    test_string_in_1 = "testing"
    expected_1 = [
        ["gets", "tin"],
        ["gets", "nit"],
        ["gnit", "set"],
        ["nits", "get"],
        ["sing", "tet"],
        ["sting", "et"],       
        ["ting", "set"],
        ["tins", "get"]
    ]
    test_string_in_2 = "crocodile"
    expeced_2 = [
        ["coil", "coder"],
        ["coil", "cored"],
        ["core", "cold"],
        ["core", "clod"],
        ["doc", "croile"],
        ["doc", "relic"],
        ["dice", "color"],
        ["idol", "cerco"],
        ["lice", "codor"],
        ["cod", "recoil"],
        ["cold", "coire"],
        ["coir", "clode"],
        ["dire", "cloco"]
    ]
    for each_test_answer in expected_1:
        assert each_test_answer in find_anagrams_func(test_string_in_1)
    # assert expeced_2 in find_anagrams_func(test_string_in_2)
"""
    Problem 1. Given an array, find all contiguous sub-arrays that add up to a given number
"""
from typing import List

given_arr = [1, 7, 4, 3, 1, 2, 1, 5, 1]


def find_sum(givenarr : list, start: int, end: int):
    return sum(givenarr[start:end])


def find_indices_of_sum(givenarr: list, sum_to_find: int) -> set:

    start = 0
    end = 1
    indices_that_total = set()
    while end <= len(givenarr):
        sum_found = find_sum(givenarr, start, end)
        if sum_found == sum_to_find:
            indices_that_total.add((start, end))
            end += 1
        elif sum_found < sum_to_find:
            end += 1
        else:
            start += 1
    return indices_that_total


"""
    Problem 2. Given test string, find all sub_strings whose characters are in a given second string
"""
input_str = "fa4chba4c444cbadd2"
match_str = "abc"


def is_chars_in_string(char_str, test_sub_str):
    is_exists = True
    for single_char in char_str:
        if single_char not in test_sub_str:
            is_exists = False
            break
    return is_exists


def find_all_chars_in_string(test_str : str, char_str: str) -> List[str]:
    start = 0
    end = 1
    substring_list = list()
    while start <= (len(test_str) - len(char_str)) and end <= len(test_str):
        sub_str = test_str[start:end]
        print(sub_str)
        if is_chars_in_string(char_str, sub_str):
            substring_list.append(sub_str)
            start += 1
        else:
            end += 1
    return substring_list


"""
    Problem 3. Given test string, find shortest sub_strings whose characters are in a given second string
    For this we copy the previous problem
"""


def assign_shortest(shorter_str: str, shortest_str: str) -> str:

    return shorter_str if len(shorter_str) < len(shortest_str) else shortest_str


def find_shortest_substring_with_chars(test_str: str, char_str: str):
    start = 0
    end = 1
    shortest_string = test_str
    while start < len(test_str) - len(char_str) and end <= len(test_str):
        sub_str = test_str[start:end]
        print(sub_str)
        if is_chars_in_string(char_str, sub_str):
            shortest_string = assign_shortest(sub_str, shortest_string)
             # print("short string :", shortest_string)
            start += 1
        else:
            end += 1
    print("shortest_string", shortest_string)


if __name__ == '__main__':
    # print(find_indices_of_sum(given_arr, 7))
    print(find_all_chars_in_string(input_str, match_str))
    # find_shortest_substring_with_chars("asdfsubsdfssdcsbadfsd", match_str)




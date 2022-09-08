"""
Problem 1: Get all substrings in a string including empty string
"""
from typing import List


class Bitmasking:
    def __init__(self, in_string: str):
        self.in_str = in_string
        self.len_str = len(in_string)

    @classmethod
    def get_all_substrings(cls, in_str) -> List[str]:
        bitum = cls(in_str)
        substring_list = list()
        for mask in range(pow(2, bitum.len_str)):
            substring_list.append(bitum.get_substring_by_bitmask(mask))
        return substring_list

    def get_substring_by_bitmask(self, mask: int) -> str:
        substr = ""
        for k in range(self.len_str):
            if mask & (1 << k) != 0:
                substr += self.in_str[k]
        return substr


print(Bitmasking.get_all_substrings("abcd"))

"""
Provided a list of english monarch names with their regnal numbers, sort the list in such a way that the list is first
sorted by name then by regnal numbers
Ex: kings = ["Henry IV", "Charles II", "Victoria III", "Benjamin X", "Henry II", "charles I", "Harry I", "Victoria V", "Benjamin XL"]
Result = ["Benjamin X", "Benjamin XL", "Charles I", "Charles II", "Harry I", "Henry II", "Henry IV", "Victoria III", "Victoria V"]
"""
from typing import List

ROMAN_TO_NUMBER = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50
}

ROMAN_PRECEDENCE = {
    "I": ["V", "X"],
    "X": ["L"]
}


def get_number_from_roman(roman):
    result = 0
    for i in range(len(roman)):
        if i < len(roman)-1 and roman[i+1] in ROMAN_PRECEDENCE[roman[i]]:
            result -= ROMAN_TO_NUMBER[roman[i]]
        else:
            result += ROMAN_TO_NUMBER[roman[i]]
    return result


def sort_romans(roman_list):
    number_to_roman_dict = {}
    sorted_romans = []
    for roman in roman_list:
        number = get_number_from_roman(roman)
        number_to_roman_dict[number] = roman

    for number in sorted(number_to_roman_dict.keys()):
        sorted_romans.append(number_to_roman_dict[number])
    return sorted_romans


def sort_english_monarchs(monarchs: List[str]):
    king_dict = {}
    result = []
    for king in monarchs:
        name, regnal = king.split()
        if king_dict.get(name, None):
            king_dict[name].append(regnal)
        else:
            king_dict[name] = [regnal]

    for name in king_dict.keys():
        king_dict[name] = sort_romans(king_dict[name])

    for name in sorted(king_dict.keys()):
        for roman in king_dict[name]:
            result.append(f"{name} {roman}")
    return result


if __name__ == "__main__":
    monarchs = ["Henry IV", "Charles II", "Victoria III", "Benjamin X", "Henry II", "Charles I", "Harry I", "Victoria V", "Benjamin XL"]
    print(sort_english_monarchs(monarchs))

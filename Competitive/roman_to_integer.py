"""
 Simple problem to convert roman number to integer snf vice versa
"""

ROMAN_SYMBOLS = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

# Precedence can be checked even without this, i.e by using the dict above
SYMBOL_PRECEDENCE_DICT = {
    "I": 1,
    "V": 2,
    "X": 3,
    "L": 4,
    "C": 5,
    "D": 6,
    "M": 7
}

NEGATIVE_ROMANS = {
    "V": "I",
    "X": "I",
    "L": "X",
    "C": "X",
    "D": "C",
    "M": "C"

}

class Sol:
    def romanToInteger(self, s: str) -> int:
        total = 0
        for d_ind in range(len(s) - 1, -1, -1):
            digit = s[d_ind]
            if total and SYMBOL_PRECEDENCE_DICT[digit] < SYMBOL_PRECEDENCE_DICT[s[d_ind + 1]]:
                total -= ROMAN_SYMBOLS[digit]
            else:
                total += ROMAN_SYMBOLS[digit]
        return total

    def divide_by_largest(self, reversed_romans: [(str, int)], num: int) -> (str, int):
        last_rom_val = 1000000
        last_rom = ""
        return_rom = ""
        remaining_num = 0
        for rom, rom_val in reversed_romans:
            if num >= rom_val and num < last_rom_val:

                if str(num)[0] in ('9', '4'):
                    num_str = str(num)
                    return_rom = NEGATIVE_ROMANS[last_rom] + last_rom
                    num_str = num_str[1:]
                    if num_str:
                        remaining_num = int(num_str)
                    else:
                        remaining_num = 0
                else:
                    return_rom = rom
                    remaining_num = num - rom_val

            last_rom_val = rom_val
            last_rom = rom
        return return_rom, remaining_num

    def intToRoman(self, num: int) -> str:
        reversed_romans = [x for x in reversed(list(ROMAN_SYMBOLS.items()))]
        remaining_num = num
        final_roman = ""
        while True:
            roman, remaining_num = self.divide_by_largest(reversed_romans, remaining_num)
            final_roman += roman
            if not remaining_num:
                break
        return final_roman





sol = Sol()
print(sol.intToRoman(1994))


class Sol:
    def get_single_digit(self, digit: int) -> str:
        result = ""
        if digit == 1:
            result = "One"
        elif digit == 2:
            result = "Two"
        elif digit == 3:
            result = "Three"
        elif digit == 4:
            result = "Four"
        elif digit == 5:
            result = "Five"
        elif digit == 6:
            result = "Six"
        elif digit == 7:
            result = "Seven"
        elif digit == 8:
            result = "Eight"
        elif digit == 9:
            result = "Nine"
        return result

    def get_teens(self, digit: int) -> str:
        result = ""
        if digit == 0:
            result = "Ten"
        elif digit == 1:
            result = "Eleven"
        elif digit == 2:
            result = "Twelve"
        elif digit == 3:
            result = "Thirteen"
        elif digit == 4:
            result = "Fourteen"
        elif digit == 5:
            result = "Fifteen"
        elif digit == 6:
            result = "Sixteen"
        elif digit == 7:
            result = "Seventeen"
        elif digit == 8:
            result = "Eighteen"
        elif digit == 9:
            result = "Nineteen"
        return result

    def get_tens(self, digit: int) -> str:
        if digit == 2:
            result = "Twenty"
        elif digit == 3:
            result = "Thirty"
        elif digit == 4:
            result = "Forty"
        elif digit == 5:
            result = "Fifty"
        elif digit == 6:
            result = "Sixty"
        elif digit == 7:
            result = "Seventy"
        elif digit == 8:
            result = "Eighty"
        elif digit == 9:
            result = "Ninety"
        return result

    def get_readable_hundred_number(self, number: int) -> str:
        result = ""
        str_num = str(number)
        len_num = len(str_num)
        if len_num >= 2:
            if len_num == 3:
                if str_num[0] != "0":
                    result += self.get_single_digit(int(str_num[0]))
                    result += " Hundred"
            if str_num[-2] != "0":
                if str_num[-2] == "1":
                    result += " " + self.get_teens(int(str_num[-1]))
                else:
                    result += " " + self.get_tens(int(str_num[-2]))
                    result += " " + self.get_single_digit(int(str_num[-1]))
            else:
                result += " " + self.get_single_digit(int(str_num[-1]))
        else:
            result += self.get_single_digit(int(str_num[-1]))

        return result.strip()

    def get_third_place_names(self, count):
        result = ""
        if count == 1:
            result = "Thousand"
        elif count == 2:
            result = "Million"
        elif count == 3:
            result = "Billion"
        elif count == 4:
            result = "Trillion"
        return result

    def numberToWords(self, num: int) -> str:
        result = ""
        count = 0
        if num == 0:
            return "Zero"
        while num:
            divd_num = num / 1000
            last_str_divd = str(divd_num).split(".")[-1]
            while len(last_str_divd) < 3:
                last_str_divd += "0"
            word = self.get_readable_hundred_number(int(last_str_divd))
            last_place_value = ""
            if word:
                last_place_value = self.get_third_place_names(count)
            result = "{} {} {}".format(word, last_place_value, result).strip()
            count += 1
            num = int(num / 1000)

        return result.strip()

s = Sol()
print(s.numberToWords(10000260001))
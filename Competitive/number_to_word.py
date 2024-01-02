
SINGLE_DIGIT_WORDS = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six",  7: "Seven", 8: "Eight",
                      9: "Nine"}
TEEN_WORDS = {0: "Ten", 1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen", 6: "Sixteen",
              7: "Seventeen", 8: "Eighteen", 9: "Nineteen"}
TEN_WORDS = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"}

POLYILLION_NAMES = {1: "Thousand", 2: "Million", 3: "Billion", 4: "Trillion", 5: "Quadrillion"}


class Sol:
    def get_readable_hundred_number(self, number: int) -> str:
        result = ""
        str_num = str(number)
        len_num = len(str_num)
        if len_num >= 2:
            if len_num == 3:
                if str_num[0] != "0":
                    result += SINGLE_DIGIT_WORDS.get(int(str_num[0]), "")
                    result += " Hundred"
            if str_num[-2] != "0":
                if str_num[-2] == "1":
                    result += " " + TEEN_WORDS.get(int(str_num[-1]), "")
                else:
                    result += " " + TEN_WORDS.get(int(str_num[-2]), "")
                    result += " " + SINGLE_DIGIT_WORDS.get(int(str_num[-1]), "")
            else:
                result += " " + SINGLE_DIGIT_WORDS.get(int(str_num[-1]), "")
        else:
            result += SINGLE_DIGIT_WORDS.get(int(str_num[-1]), "")
        return result.strip()

    def numberToWords(self, num: int) -> str:
        result = ""
        count = 0
        if num == 0:
            return "Zero"
        while num:
            divn_num = num % 1000
            word = self.get_readable_hundred_number(divn_num)
            last_place_value = ""
            if word:
                last_place_value = POLYILLION_NAMES.get(count, "")
            result = "{} {} {}".format(word, last_place_value, result).strip()
            count += 1
            num = int(num / 1000)

        return result.strip()


s = Sol()
print(s.numberToWords(9999999))

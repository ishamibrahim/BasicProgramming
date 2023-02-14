"""
Given a string, get triple binary string of it. Take the conversion of word to string o binary characters


Ex : Input : "abc"
Step1: Convert to ASCII integers  97, 98, 99
Step2: Convert to 8 digit binary 01100001, 01100010, 01100011
Step3: Triple the binaries 000111111000000000000111, 000111111000000000111000, 000111111000000000111111
Step 4:  Join for Output : 000111111000000000000111000111111000000000111000000111111000000000111111


"""


class Sol:
    def get_binaries_of_integer(self, num: int):
        result = ""
        bin_num = 1
        for i in range(8):
            bin_num = 1 << i
            bin_exist = num & bin_num
            if bin_exist:
                result = "1" + result
            else:
                result = "0" + result
        return result

    def get_tripled_binary_characters(self, word):
        final_binary_list = []
        final_word = ''
        for letter in word:
            binary_string = self.get_binaries_of_integer(ord(letter))
            final_binary_list.append(binary_string)
        for bin_word in final_binary_list:
            final_word += "".join([bin_letter*3 for bin_letter in bin_word])
        return final_word


s = Sol()
print(s.get_tripled_binary_characters("abc"))

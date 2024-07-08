from typing import List
"""
    --medium--
    https://leetcode.com/problems/letter-case-permutation
    Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.
    Ex : 'a1b2'
        Output : ["a1b2","a1B2","A1b2","A1B2"] - in any order
"""

class Solution:

################### Solution 1 #######################################
    def get_cased_string(self, word, counter):
        result = ""
        for i in range(len(word)):
            if 1 << i & counter:
                result += word[i].upper()
            else:
                result += word [i].lower()
        return result

    def letterCasePermutation(self, s: str) -> list[str]:
        """
        The solution uses bit masking to get all the combinations
        Runtime: 9%
        Memory: 24%
        """
        output_set = {s}
        counter = 0
        word_bin_val = pow(2, len(s))
        while counter < word_bin_val:
            output_set.add(self.get_cased_string(s, counter))
            counter += 1
        return list(output_set)

######################### Solution 2 ##################################

    def change_case(self, ind, word, final_word, len_word, result_list):
        if ind < len_word:
            if word[ind].isalpha():
                self.change_case(ind+1, word, final_word + word[ind].lower(), len_word, result_list)
                self.change_case(ind+1, word, final_word + word[ind].upper(), len_word, result_list)
            else:
                self.change_case(ind+1, word, final_word + word[ind], len_word, result_list)
        else:
            result_list.append(final_word)



    def letterCasePermutation2(self, s: str) -> list[str]:
        """
        This approach uses recursion
        Runtime: 70%
        Memory : 28%
        """
        result_list = []
        len_word = len(s)

        self.change_case(0, s, "", len_word, result_list)
        return result_list


print(Solution().letterCasePermutation2("a1b2"))

import pdb
"""
    A recursive approach to check if a word can be broken in such a way that its sub words exist in a list of given
    words.
"""


class WordBreakProblem:
    WORD_LIST = ["i", "like", "want", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go",
                 "mango"]

    @staticmethod
    def is_word_in_list(word, word_list):
        return any(list_item.startswith(word) for list_item in word_list)

    @staticmethod
    def word_check(word: str, is_exists: bool, output_list:  list) -> bool:
        checker = ""
        if word == "":
            is_exists = True
        for i in range(len(word)):
            checker += word[i]
            print(" checker: ", checker)
            if checker in WordBreakProblem.WORD_LIST and checker not in output_list:
                output_list.append(checker)
                is_exists = WordBreakProblem.word_check(word[i+1:], is_exists, output_list)
            if not WordBreakProblem.is_word_in_list(checker, WordBreakProblem.WORD_LIST):
                break

        return is_exists


if __name__ == "__main__":
    input_word = "ilikemango"
    outputs = []
    is_word_there = WordBreakProblem.word_check(input_word, False, outputs)
    print(is_word_there)
    print(outputs)

import pdb
"""
    A recursive approach to check if a word can be broken in such a way that its sub words exist in a list of given
    words.
"""


class WordBreakProblem:
    WORD_LIST = ["like", "want", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go",
                 "mango"]

    @staticmethod
    def is_word_in_list(word, word_list):
        return any(list_item.startswith(word) for list_item in word_list)

    @staticmethod
    def word_check(word: str, is_exists: bool, output_list:  list) -> bool:
        new_is_exists = False
        checker = ""
        for i in range(len(word)):
            checker += word[i]
            print(" checker: ", checker)
            if checker in WordBreakProblem.WORD_LIST:
                output_list.append(checker)
                new_is_exists = True
            elif not WordBreakProblem.is_word_in_list(checker, WordBreakProblem.WORD_LIST):
                new_is_exists = WordBreakProblem.word_check(word[1:], is_exists, output_list)
                break

        return is_exists or new_is_exists


if __name__ == "__main__":
    input_word = "ilikemangoicecream"
    outputs = []
    is_word_there = WordBreakProblem.word_check(input_word, False, outputs)
    print(is_word_there)
    print(outputs)

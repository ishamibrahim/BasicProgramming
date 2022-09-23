import pdb
"""
    A recursive approach to check if a word can be broken in such a way that its sub words exist in a list of given
    words.
    
    This can also be solved by sliding window
"""


class WordBreakProblem:
    WORD_LIST = ["like", "want", "sam", "sung", "samsung", "mobile", "ice", "cream", "icecream", "man", "go",
                 "mango"]

    @staticmethod
    def is_word_in_list(word, word_list):
        return any(list_item.startswith(word) for list_item in word_list)

# ============== BELOW WITH RECURSION =============
    @staticmethod
    def word_check_recursion(word: str, output_list:  list):
        checker = ""
        for i in range(len(word)):
            checker += word[i]
            print(" checker: ", checker)
            if checker in WordBreakProblem.WORD_LIST:
                output_list.append(checker)
            elif not WordBreakProblem.is_word_in_list(checker, WordBreakProblem.WORD_LIST):
                WordBreakProblem.word_check_recursion(word[1:], output_list)
                break

        return

# ============== BELOW WITHOUT RECURSION =============

    @staticmethod
    def word_check_unit(word: str, output_list: list):
        checker = ""
        for i in range(len(word)):
            checker += word[i]
            print(" checker: ", checker)
            if checker in WordBreakProblem.WORD_LIST:
                output_list.append(checker)
            elif not WordBreakProblem.is_word_in_list(checker, WordBreakProblem.WORD_LIST):
                break
        return

    @staticmethod
    def word_check_no_recursion(word: str, output_list: list):
        for i in range(len(word)):
            WordBreakProblem.word_check_unit(word[i:], output_list)
        print(output_list)


if __name__ == "__main__":
    input_word = "ilikesamsung"
    outputs = []
    # WordBreakProblem.word_check_recursion(input_word, outputs)
    WordBreakProblem.word_check_no_recursion(input_word, outputs)
    print(outputs)

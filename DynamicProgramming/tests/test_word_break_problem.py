import unittest
from DynamicProgramming.word_break_problem import WordBreakProblem


class TestWordBreak(unittest.TestCase):
    def setUp(self) -> None:
        self.word_list = ["i", "like", "want", "sam", "sung",]

    def test_is_part_word_in_list(self):
        word = "s"
        self.assertTrue(WordBreakProblem.is_word_in_list(word, self.word_list))

    def test_is_full_word_in_list(self):
        word = "like"
        self.assertTrue(WordBreakProblem.is_word_in_list(word, self.word_list))

    def test_is_word_not_in_list(self):
        word = "liked"
        self.assertFalse(WordBreakProblem.is_word_in_list(word, self.word_list))


if __name__ == "__main__":
    unittest.main()
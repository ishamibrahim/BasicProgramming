"""
Interpreter design is used to generally represent a language and its grammar.
Link : https://www.udemy.com/course/python-design-patterns/learn/lecture/8206368

"""

class TerminalExpression(object):
    def __init__(self, word):
        self.word = word

    def interpret(self, text):
        text_words = text.split()

        if self.word in text_words:
            return True
        else:
            return False

class OrExpression(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, text):
        return self.left.interpret(text) or self.right.interpret(text)

class AndExpression(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, text):
        return self.left.interpret(text) and self.right.interpret(text)


noun = TerminalExpression("Wick")
verb = TerminalExpression("Kill")
adjective = TerminalExpression("Badass")
adverb = TerminalExpression("Bloodily")
conjunction = TerminalExpression("Nonetheless")
pronoun = TerminalExpression("He")

# Testing the grammar

grammar1 = OrExpression(noun, pronoun)
grammar2 = AndExpression(grammar1, verb)
grammar3 = OrExpression(grammar2, adverb)
grammar4 = AndExpression(adjective, grammar3)


if __name__ == '__main__':
    print(grammar4.interpret("Badass Wick not Kill Bloodily"))
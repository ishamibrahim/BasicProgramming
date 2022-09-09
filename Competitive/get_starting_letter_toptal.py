class Sol:
    """
        Given the precedence of letters by the pattern "A>B", meaning A comes before B,
        and a list of precedence patterns with unique letters
        Find the word using the precedence patterns.
    """

    def get_starting_letter(self, prec_list):
        starting_letter = ""
        for prec in prec_list:
            starting_letter = prec[0]
            temp = [x[2:] for x in prec_list]
            if starting_letter not in temp:
                break
        return starting_letter

    def find_word(self, prec_list):
        word_map = dict()
        for prec_word in prec_list:
            word_map[prec_word[0]] = prec_word[2]
        starting_letter = self.get_starting_letter(prec_list)
        final_word = ""
        next_letter = starting_letter
        while True:
            final_word += next_letter
            next_letter = word_map.get(next_letter, "")
            if next_letter == "":
                break
        return final_word


s = Sol()
print(s.find_word(["P>E", "E>R", "R>U"]))
print(s.find_word(["I>N", "A>I", "P>A", "S>P"]))
print(s.find_word(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]))
print(s.find_word(["I>F", "W>I", "S>W", "F>T"]))
print(s.find_word(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]))
print(s.find_word(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]))

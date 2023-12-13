"""
Azn interview question: Make flower patterns that are based on the number of  flower types
Ex1:
    flower_types = 1
    Pattern : A A
              A A
Ex2:
    flower_types = 3
    Pattern : C C C C C C
              C B B B B C
              C B A A B C
              C B A A B C
              C B B B B C
              C C C C C C

"""

class Sol:
    def get_pattern_for_flower(self, f_type: int, flower_type_count: int):
        element_char = ""
        count = 0

        for i in range(flower_type_count):
            if f_type == 0:
                char_decr = flower_type_count -1
            else:
                char_decr = flower_type_count - 1 - count
                count += 1 if count < f_type else 0

            element = chr(65+char_decr)
            element_char += element
        return element_char + element_char[::-1]

    def make_flower_matrix(self, flower_types: int):
        flower_pattern = []

        for f_type in range(flower_types):
            flower_pattern.append(self.get_pattern_for_flower(f_type, flower_types))
        return flower_pattern + flower_pattern[::-1]

s = Sol()
final_design = s.make_flower_matrix(4)


print("Final ")
for word in final_design:
    print(" ".join(word))

"""
Given a string consisting of '*' and '|', show how many '*'s are enclosed withing two '|'
in substring with starting index list and ending index list.
 Start and end index pairs are related on their respective positions
"""

class Sol:
    def number_of_items(self, ex_str, start_indices, end_indices):
        result_count_list = []
        index_len = len(start_indices)

        for ind in range(index_len):
            pattern = ex_str[start_indices[ind] - 1: end_indices[ind]]
            len_pattern = len(pattern)
            result_count = 0
            if len_pattern and pattern.count("|") > 1:
                start_index = pattern.index("|")
                end_index = len_pattern - pattern[::-1].index("|")
                print(pattern[start_index:end_index], start_index, end_index)
                result_count = pattern[start_index:end_index].count("*")
            result_count_list.append(result_count)
        return result_count_list

s = Sol()
print(s.number_of_items("*|*|*|", [1,1], [1, 6]))
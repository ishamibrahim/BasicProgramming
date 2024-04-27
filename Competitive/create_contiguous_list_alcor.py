"""
Given a list of multiple dimensions, create a contiguous array
Ex: imput : [1, 2, 3, (4, [5, 6]), (7, 8, [9])]
    output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
"""
from typing import List
def get_contiguous_list(in_list: List, out_list: List=[]):
    for item in in_list:
        if type(item) not in (list, tuple):
            out_list.append(item)
        else:
            get_contiguous_list(item, out_list)

in_list = [1, 2, 3, (4, [5, 6]), (7, 8, [9])]
outlist = []

get_contiguous_list(in_list, outlist)
print(outlist)

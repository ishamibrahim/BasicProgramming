"""
PRovided a list of string characters find all complete ombinatoins of string characters with
Ex: Given: [
            [a, b, c, d,...
            [1, 2, 3, 4, 5....
            ['A, B, C, D, ...
            ]
    Result = [a1A, a1B, a1C...
"""

def dfs(req_list, counter, combination, result):
    if counter < len(req_list):
        for letter in req_list[counter]:
            combination += letter
            dfs(req_list, counter+1, combination, result)
            combination = combination[:-1]
    else:
        result.append(combination)


def find_complete_combinations():
    counter = 0
    result = []
    req = [
            ["a", "b", "c", "d"],
            ["1", "2", "3", "4", "5"],
            ["A", "B", "C", "D"]
            ]
    dfs(req, counter, "",  result)
    return result

print(find_complete_combinations())

"""
    Given a list of string binary values, convert them to integer and find the type of progession
    If all the items are equal, then append "Stable" to the list
    If they are in ascending order, then append "Inproving", if descending then append "Degrading"
    If they are neither increasing or descreasing, then append "Unstable"
    Otherwise if the list elements are erroneous or has any unexpected values, Return "Invalid Output"
"""


def solution(states):
    len_states = len(states[0])
    result_arr = []
    unstable_states = False
    for arr in states:
        index = len_states - 1
        result_sum = 0
        for bit in arr:
            try:
                int_bit = int(bit)
            except Exception as e:
                result_arr = ["Invalid Input"]
                unstable_states = True
                break
            if int_bit > 1:
                result_arr = ["Invalid Input"]
                unstable_states = True
                break
            result_sum += int_bit * pow(2, index)
            index -= 1
        if unstable_states:
            break
        result_arr.append(result_sum)
    if not unstable_states:
        inc_sorted = sorted(result_arr)
        desc_sorted = sorted(result_arr, reverse=True)
        if len(set(result_arr)) == 1:
            result_arr.append("Stable")
        elif inc_sorted == result_arr:
            result_arr.append("Improving")
        elif desc_sorted == result_arr:
            result_arr.append("Degrading")
        else:
            result_arr.append("Unstable")

    return list(map(lambda x: str(x), result_arr))


print(solution([["1", "1", "0", "1", "1", "1"],
                ["0", "1", "1", "0", "0", "1"],
                ["0", "1", "0", "1", "0", "0"],
                ["0", "0", "1", "0", "1", "0"]]))

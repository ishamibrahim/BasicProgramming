import itertools
import pdb
import time
import random
"""
    The knapsack problem (0/1) 
    There are n items with each having a weight and value.  A knapsack 
"""

############################# Dynamic programmming ########################################
def knapsack(weights, values, result, i, c_remain):
    if c_remain > 0 and i < len(weights):
        temp1 = 0
        if weights[i] <= c_remain:
            temp1 = knapsack(weights, values, result+values[i], i+1, c_remain-weights[i])
        temp2 = knapsack(weights, values, result, i+1, c_remain)
        result = max(temp1, temp2)
    return result

############################# Dynamic programming with memoization ########################3
memoized_dict = {}

def knapsack_with_memoization(weights, values, result, i, c_remain):
    if c_remain > 0 and i < len(weights):
        if not memoized_dict.get((i, c_remain)):
            temp1 = 0
            if weights[i] <= c_remain:
                temp1 = knapsack_with_memoization(weights, values, result+values[i], i+1, c_remain-weights[i])
            temp2 = knapsack_with_memoization(weights, values, result, i+1, c_remain)
            result = max(temp1, temp2)

            memoized_dict[(i, c_remain)] = result
        else:
            result = memoized_dict[(i, c_remain)]
    return result


# knapsack2(weights, values,  capacity)

############################ Dynamic programming using 2D tables ##########################################

def get_optimal_combination(weights, values, start_ind, weight_ind, cap, result):
    value1 = value2 = result
    if start_ind < weight_ind and weights[start_ind] <= cap :
        value1 = get_optimal_combination(weights, values, start_ind+1, weight_ind, cap-weights[start_ind], result + values[start_ind])

        value2 = get_optimal_combination(weights, values, start_ind+1, weight_ind, cap, result)

    return max(value1, value2)



def find_optimal_value(weights, values, weights_ind, end_weight):
    result = get_optimal_combination(weights, values, 0, weights_ind, end_weight, 0)
    return result



def knapsack3(weights, values, capacity):
    """
    This solution creates a matrix of the length of capacity and fills it with values ccorresponding to the cumulated weights
    Check https://www.youtube.com/watch?v=nLmhmB6NzcM for reference
    """

    n = len(values)
    matrix = [[0] * (capacity + 1) for _ in itertools.repeat(None, n+1)]

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            optimal_val = find_optimal_value(weights, values, i, j)
            if optimal_val:
                matrix[i][j] = optimal_val
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    return matrix[n][capacity]  # the last item of the matrix

weights3 = [1,3,4,5]
values3 = [1,4,5,7]

print(knapsack3(weights3, values3, 7))

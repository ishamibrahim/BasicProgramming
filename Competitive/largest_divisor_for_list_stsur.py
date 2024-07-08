"""
    Given a list of numbers and a threshold value, find a number when divided from all the numbers in the list
    add up to the max value below the threshold
    take the closest upper value if dividend is a fraction. ex: 9/4 = 2.25 equals 3
    Ex:
        list = [1,3,7] threshold = 8
        if divisor = 1 ==> resulting list becomes [1, 3, 7] ==> sum = 11 > threshold
        if divisor = 2 ==> resulting list becomes [1, 2, 4] ==> sum = 7 < threshold
        Then result = 2

"""
import math
from typing import List


def largest_divisor_for_list(nums: List[int], threshold: int):
    divisor = 1
    while True:
        dividends = [math.ceil(num/divisor) for num in nums]
        if sum(dividends) <= threshold:
            break
        divisor += 1
    return divisor


if __name__ == "__main__":
    print(largest_divisor_for_list([1, 3, 7], 8))


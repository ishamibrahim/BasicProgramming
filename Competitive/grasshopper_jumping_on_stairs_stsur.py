"""
 Imagine there is a stair case with  first step starting from 1.
 A grashopper in the stairs can jump any number of steps up or down from any step. If the number
 of steps to jump is given in an array where negative numbers are for jumping downstairs, find
 the minimum step it has to be in so that it doesnt go below step 1. (out of the stair case).

 Ex : steps = [1, -4, -2, 3]
    ans: 6 ==> 6 +1 -4 -2 = 1 , Any starting point below 6 will result in value <= 0

"""
from typing import List


def find_minimum_starting_step(steps: (List[int])):
    """
        We consider the approach where we first find the sum and check the sum <= 1,
        if it is, we start with the step adding the sum
    """

    first_step = 1
    sum_steps = sum(steps)
    if sum_steps < 1:
        first_step = 1 + abs(sum_steps)
    while True:
        is_broken = False
        current_step = first_step
        for step in steps:
            current_step += step
            if current_step < 1:
                first_step += 1
                is_broken = True
                break
        if not is_broken:
            break
    return first_step


if __name__ == "__main__":
    stepsList = [-2, 5, -6, 1, 2, -4]
    print(find_minimum_starting_step(stepsList))

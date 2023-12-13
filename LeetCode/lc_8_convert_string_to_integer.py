import re

"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer 

Solution    -   54.7% in Runtime
            -   22.7% in Memory
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        result = re.search("^([\s]*[\-|\+]?[0-9]+)", s)
        if result:
            result = int(result.group(0).strip())
        else:
            result = 0

        greatest = pow(2, 31)
        if -greatest > result:
            result = -greatest
        elif result > greatest-1:
            result = greatest-1
        return result

print(Solution().myAtoi("  -42"))

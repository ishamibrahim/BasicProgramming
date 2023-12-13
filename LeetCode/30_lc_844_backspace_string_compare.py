from typing import List

"""
Given two strings, return true if both result in the same string.
The strings may have * that represent backspaces.

Ex : a = "*a*cbd**e", 
b = "ccc**ed*"
"""
class Solution:
    def get_resolved_str(self, a_string: str) -> List[str]:
        result_stack = []
        for i in range(len(a_string)):
            if a_string[i] == "#":
                result_stack.pop(-1) if result_stack else None
            else:
                result_stack.append(a_string[i])
        return result_stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        a_str = self.get_resolved_str(s)
        b_str = self.get_resolved_str(t)

        if a_str == b_str:
            return True
        else:
            return False


print(Solution().backspaceCompare("#a#cb#", "c"))

class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

    def __repr__(self):
        this = self
        result = ""
        while this !=None:
            result += "{}->".format(this.val)
            this = this.next
        return result


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"{self.start} - {self.end}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node {self.val} -> {self.left.val if self.left  else None} | {self.right.val if self.right else None}"

        


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


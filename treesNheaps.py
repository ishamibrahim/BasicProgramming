import pdb

#=====================BINARY search TREE=======================================
arr = [3, 97, 63, 55, 32, 56, 99, 22]


class Bnode:
    def __init__(self, val=None):
        self.value = val
        self.left = None
        self.right = None

    def __str__(self):
        return "value : {}".format(self.value)

    def __repr__(self):
        return "Object val : {}".format(self.value)


def create_binary_search_tree(linear_array):
    root = None
    curr_node = None
    for item in linear_array:
        node_item = Bnode(item)
        if not root:
            root = node_item
        while True:
            if not curr_node:
                curr_node = node_item
                break
            elif not curr_node.value:
                curr_node = node_item
                break
            elif item < curr_node.value:
                if not curr_node.left:
                    curr_node.left = node_item
                    break
                else:
                    curr_node = curr_node.left

            else:
                if not curr_node.right:
                    curr_node.right = node_item
                    break
                else:
                    curr_node = curr_node.right
        curr_node = root
    return root

# =================== PRE/IN/POST ORDER ==========================

arr = [3, 97, 63, 55, 32, 56, 99, 22]




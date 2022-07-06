import pdb

# =====================BINARY search TREE=======================================
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


# =================== BINARY SEARCH TREE ==========================

"""
Given a binary tree in the form of an array, check if its a binary search tree or not
"""
arr = [0, 10, 7, 12, 4, 9, 0, 0, 1, 5, 0, 0, 0, 0, 0, 0, ]


class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


last_parsed = -1


def input_items(node, i):
    if arr[i] != 0:
        node.data = arr[i]
    l = i * 2
    if l < len(arr):
        if arr[l] != 0:
            node.left = Node()
            input_items(node.left, l)
    r = (i * 2) + 1
    if l < len(arr):
        if arr[r] != 0:
            node.right = Node()
            input_items(node.right, r)


def check_binary_search_tree(root):
    result = "Yes"
    result = check_for_bst(root, result)
    return result


def check_for_bst(node, result):
    global last_parsed
    if node.left:
        result = check_for_bst(node.left, result)
    if node.data <= last_parsed:
        print("LAst parsed lesser")
        result = "No"

    print("{0}  {1}".format(last_parsed, node.data))
    last_parsed = node.data

    if node.right:
        result = check_for_bst(node.right, result)
    return result


c = Node()

input_items(c, 1)
print(check_binary_search_tree(c))

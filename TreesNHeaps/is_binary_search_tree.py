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





# =================== BINARY SEARCH TREE ==========================

"""
Given a binary tree in the form of an array, check if its a binary search tree or not
"""
new_arr = [0, 10, 7, 12, 4, 9, 0, 0, 1, 5, 0, 0, 0, 0, 0, 0 ]


class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None

    @staticmethod
    def print_tree(node):
        if node == None:
            return

        Node.print_tree(node.left)
        print(node.data)
        Node.print_tree(node.right)

def create_binary_search_tree(linear_array):
    root = None
    curr_node = None
    for item in linear_array:
        node_item = Node(item)
        if not item:
            continue
        if not root:
            root = node_item
            continue
        while True:
            if not curr_node:
                curr_node = node_item
                break
            elif item < curr_node.data:
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


def input_items(node, i, node_arr):
    if node_arr[i] != 0:
        node.data = node_arr[i]
    l = i * 2
    if l < len(node_arr):
        if node_arr[l] != 0:
            node.left = Node()
            input_items(node.left, l, node_arr)
    r = (i * 2) + 1
    if l < len(node_arr):
        if node_arr[r] != 0:
            node.right = Node()
            input_items(node.right, r, node_arr)


def check_binary_search_tree(root):
    result = "Yes"
    result = check_for_bst(root, result)
    return result

last_parsed = -1

def check_for_bst(node, result):
    global last_parsed
    if node.left:
        result = check_for_bst(node.left, result)
    if node.data <= last_parsed:
        print("Last parsed lesser")
        result = "No"

    print("{0} --> {1}".format(last_parsed, node.data))
    last_parsed = node.data
    if node.right:
        result = check_for_bst(node.right, result)
    return result


c = Node()

input_items(c, 1, new_arr)
# Node.print_tree(c)
# print(check_binary_search_tree(c))
btee = create_binary_search_tree(arr)
btee.print_tree(btee)

import pdb
INF = float("inf")
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
Given a binary tree in the form of a list, check if its a binary search tree or not
"""
bin_tree_list = [-1, 10, 7, 12, 4, 9, 0, 0, 1, 5, 0, 0, 0, 0, 0, 0]


class Node:
    def __init__(self, val=None):
        self.data = val
        self.left = None
        self.right = None
    def __str__(self):
        return "value : {}".format(self.data)

    def __repr__(self):
        return "Object val : {}".format(self.data)

    @staticmethod
    def print_tree(node):
        if node == None:
            return

        Node.print_tree(node.left)
        print(node.data)
        Node.print_tree(node.right)

class BinTree:
    def __init__(self):
        self.root_node = Node()

    def print_tree(self):
        self.root_node.print_tree(self.root_node)

    def create_binary_search_tree(self, linear_array):
        self.root_node = None
        curr_node = None
        for item in linear_array:
            node_item = Node(item)
            if not item:
                continue
            if not self.root_node:
                self.root_node = node_item
                curr_node = node_item
                continue
            while True:
                if item < curr_node.data:
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
            curr_node = self.root_node
        return self.root_node


    def create_bin_tree_from_list(self, node, i, tree_arr):
        if tree_arr[i] != 0:
            node.data = tree_arr[i]
        left = i * 2
        if left < len(tree_arr):
            if tree_arr[left]:
                node.left = Node()
                self.create_bin_tree_from_list(node.left, left, tree_arr)
        right = (i * 2) + 1
        if right < len(tree_arr):
            if tree_arr[right] :
                node.right = Node()
                self.create_bin_tree_from_list(node.right, right, tree_arr)


def check_binary_search_tree(root):
    result = "Yes"
    result, _ = check_for_bst(root, result, -INF)
    return result


def check_for_bst(node, result, last_parsed):
    if node.left:
        result, last_parsed = check_for_bst(node.left, result, last_parsed)
    if node.data <= last_parsed:
        print("Last parsed lesser")
        result = "No"
        return result

    print("{0} --> {1}".format(last_parsed, node.data))
    last_parsed = node.data
    if node.right:
        result, last_parsed = check_for_bst(node.right, result, last_parsed)
    return result, last_parsed


# Testing if an array in a binary serach tree
any_tree = BinTree()
any_tree.create_bin_tree_from_list(any_tree.root_node, 1, bin_tree_list)
any_tree.print_tree()
print(check_binary_search_tree(any_tree.root_node))


# Creating binary search tree
# bin_search_tee = create_binary_search_tree(arr)
# bin_search_tee.print_tree(bin_search_tee)

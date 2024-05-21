bin_tree_list = [-1, 5, 12, 13, 7, 0, 14, 2, 17, 23, 0 , 0, 7, 3, 8, 11]
from collections import deque
from is_binary_search_tree import BinTree, Node


def print_in_order_traversal(node: Node):
    if node.left:
        print_in_order_traversal(node.left)

    print(f"{node.data} ")
    if node.right:
        print_in_order_traversal(node.right)

def print_pre_order_traversal(node: Node):
    print(f"{node.data} ")
    if node.left:
        print_pre_order_traversal(node.left)
    if node.right:
        print_pre_order_traversal(node.right)

def print_post_order_traversal(node: Node):
    if node.left:
        print_post_order_traversal(node.left)
    if node.right:
        print_post_order_traversal(node.right)
    print(f"{node.data}")

def print_level_order_traversal( dq: deque):
    while dq:
        node = dq.popleft()
        if node.left:
            dq.append(node.left)
        if node.right:
            dq.append(node.right)
        print(node.data)





if __name__ == "__main__":
    any_tree = BinTree()
    any_tree.create_bin_tree_from_list(any_tree.root_node, 1, bin_tree_list)
    # print_in_order_traversal(any_tree.root_node)
    dq = deque()
    dq.append(any_tree.root_node)
    print_level_order_traversal(dq)

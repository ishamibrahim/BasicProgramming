
from typing import List


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(in_list: List) -> ListNode:
    old_item = None
    first_item = None
    for item in in_list:
        l_item = ListNode(item)
        if old_item:
            old_item.next = l_item
        if not first_item:
            first_item = l_item
        old_item = l_item

    return first_item


def reverse_linked_list_using_iteration(lin_list: ListNode):
    old_item = lin_list
    new_item = lin_list.next
    old_item.next = None
    if new_item:
        temp_item = new_item.next
        while temp_item:
            new_item.next = old_item
            old_item = new_item
            new_item = temp_item
            temp_item = temp_item.next
        new_item.next = old_item

        return new_item
    else:
        return old_item


def reverse_linked_list_using_recursion(in_list: ListNode):
    if in_list.next == None:
        return in_list

    new_head = reverse_linked_list_using_recursion(in_list.next)
    print(new_head.val)
    next_node = in_list.next
    next_node.next = in_list
    in_list.next = None
    return new_head


def print_linked_list(lin_list: ListNode):
    l_item = lin_list
    ll_str = ""
    while l_item:
        val = l_item.val
        ll_str += "{} -> ".format(val)
        l_item = l_item.next
    print(ll_str)


if __name__ == "__main__":
    mylist = ["a", "b", "c", "d"]
    l_list = create_linked_list(mylist)
    print_linked_list(l_list)
    rev_list = reverse_linked_list_using_iteration(l_list)
    print_linked_list(rev_list)
    l_list = create_linked_list(mylist)
    rev_list = reverse_linked_list_using_recursion(l_list)
    print_linked_list(rev_list)

"""
You are given a node del_node of a Singly Linked List where you have to delete a value of the given node 
from the linked list but you are not given the head of the list.

By deleting the node value, we do not mean removing it from memory. We mean:

    The value of the given node should not exist in the linked list.
    The number of nodes in the linked list should decrease by one.
    All the values before & after the del_node node should be in the same order.

Multiple nodes can have the same values as the del_node, but you must only remove the node whose pointer 
del_node is given to you.
It is guaranteed that there exists a node with a value equal to the del_node value and it will not be the 
last node of the linked list.

https://www.geeksforgeeks.org/problems/delete-without-head-pointer/1
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class DeleteNodeWithOutHead:
    # Function to delete a node without any reference to head pointer.
    """ T(c) -> O(1), S(c) -> O(1) """
    def deleteNode(self,del_node):
        # copy the data of next node to current node
        del_node.data = del_node.next.data
        # consider next node to delete, as we only need to delete value
        del_node.next = del_node.next.next


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    # print linked list
    print_linked_list(head)

    # delte node 4
    DeleteNodeWithOutHead().deleteNode(head.next.next.next)

    print_linked_list(head)

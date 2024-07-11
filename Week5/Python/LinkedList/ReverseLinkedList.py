"""
    Given head a linked list, the task is to reverse this list.

    The following is internal representation of every test case (two inputs).
    n : Size of the linked list
    value[] :  An array of values that represents values of nodes.

    https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Reverse_Linked_List:
    # Reverse linked list using stack by changing data
    """ T(c) -> O(n + n), S(c) -> O(n) """
    def reverseList(self, head):
        # using stack
        temp = head
        stack = []
        
        # push into stack
        while temp != None:
            stack.append(temp.data)
            temp = temp.next
            
        # pop from stack and replace node value in linked list
        temp = head
        while temp != None:
            temp.data = stack.pop()
            temp = temp.next
            
        return head


    # Function to reverse a linked list using 3 pointer
    """ T(c) -> O(n), S(c) -> O(1) """
    def reverseListBetter(self, head):
        prev_ptr = None
        curr_ptr = head
        next_ptr = head.next
        
        while curr_ptr != None:
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_ptr
            if next_ptr != None:
                next_ptr = next_ptr.next
            
        head = prev_ptr
        return head
    

    # Reverse linked list using recursion (will not work for more than 1000 nodes due to python's recursion limit)
    """ T(c) -> O(n), S(c) -> O(n) """
    def reverseListRecursive(self, head):
        # base case
        if head is None or head.next is None:
            return head
        
        # new head of reversed linked list    
        newhead = self.reverseListRecursive(head.next)
        
        next_ptr = head.next
        next_ptr.next = head
        head.next = None
        return newhead


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(2)
    head.next.next.next = Node(4)

    # Print the original linked list
    print("Original Linked List:", end=" ")
    print_linked_list(head)

    # Reverse the linked list
    # head = Reverse_Linked_List().reverseList(head)

    # head = Reverse_Linked_List().reverseListBetter(head)

    head = Reverse_Linked_List().reverseListRecursive(head)

    # Print the reversed linked list
    print("Reversed Linked List:", end=" ")
    print_linked_list(head)

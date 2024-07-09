"""
    Given head a linked list, the task is to reverse this list.

    The following is internal representation of every test case (two inputs).
    n : Size of the linked list
    value[] :  An array of values that represents values of nodes.

    https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1
"""


class Solution:
    #Function to reverse a linked list.
    """ T(c) -> O(n), S(c) -> O(1) """
    def reverseList(self, head):
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
            




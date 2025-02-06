"""
https://www.geeksforgeeks.org/problems/count-nodes-of-linked-list/0
"""

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        """T(c) -> O(N), S(c) -> O(1)"""

        count = 0
        curr = head

        while curr is not None:
            count += 1
            curr = curr.next
            
        return count
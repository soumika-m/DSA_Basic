"""
https://www.geeksforgeeks.org/problems/introduction-to-doubly-linked-list/1
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Solution:
    def constructDLL(self, arr):
        """ T(c) -> O(N), S(c) -> O(N) """
        head = Node(arr[0])
        
        curr = head
        for i in range(1, len(arr)):
            curr.next = Node(arr[i])
            curr.next.prev = curr
            curr = curr.next
            
        return head

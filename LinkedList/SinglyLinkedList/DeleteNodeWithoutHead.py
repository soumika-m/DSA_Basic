"""
https://leetcode.com/problems/delete-node-in-a-linked-list/description/
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """T(c) -> O(1), S(c) -> O(1)"""

        # modify node in-place.
        # we will replace current node value with next node
        node.val = node.next.val
        # delete next node
        node.next = node.next.next
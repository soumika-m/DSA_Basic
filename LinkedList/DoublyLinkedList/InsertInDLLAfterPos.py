"""
https://www.geeksforgeeks.org/problems/insert-a-node-in-doubly-linked-list/1
"""

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class Solution:
    #Function to insert a new node at given position in doubly linked list.
    def addNode(self, head, p, x):
        """ T(c) -> O(N), S(c) -> O(1) """
        curr = head

        # go till that position
        while p > 0:
            p = p - 1
            curr = curr.next
        
        # insert that node 
        new_node = Node(x)
        new_node.next = curr.next
        curr.next = new_node
        new_node.prev = curr

        # if not last node
        if new_node.next != None:
            new_node.next.prev = new_node
        
        return head

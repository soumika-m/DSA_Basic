"""
https://www.geeksforgeeks.org/problems/linked-list-insertion-1587115620/0
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        """T(c) -> O(N), S(c) -> O(1)"""

        # if head pointing to null
        if head == None:
            head = Node(x)
            return head
        
        curr = head
        while curr.next != None:
            curr = curr.next

        curr.next = Node(x)
        
        return head
    
    def printList(self, node):
        while node:
            print(node.data, end=" ")
            node = node.next
        print()

    
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    x = 6
    if arr:
        head = Node(arr[0])
        tail = head
        for num in arr[1:]:
            tail.next = Node(num)
            tail = tail.next

    obj = Solution()
    ans = obj.insertAtEnd(head, x)
    obj.printList(ans)
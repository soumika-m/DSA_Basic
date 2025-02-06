"""
https://www.geeksforgeeks.org/problems/introduction-to-linked-list/1
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def constructLL(self, arr):
        """T(c) -> O(N), S(c) -> O(N)"""

        head = None
        curr = None

        for elem in arr:
            # for first element
            if head == None:
                head = curr = Node(elem)

            # for all other elements
            else:
                curr.next = Node(elem)
                curr = curr.next

        return head


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    ob = Solution()
    res = ob.constructLL(arr)
    while res:
        print(res.data, end=' -> ')
        res = res.next
    print('NULL')
    
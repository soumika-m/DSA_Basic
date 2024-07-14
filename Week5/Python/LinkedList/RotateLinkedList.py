"""
    Given the head of a linked list, rotate the list to the right by k places.
    The number of nodes in the list is in the range [0, 500]
    0 <= k <= 2 * 109

    https://leetcode.com/problems/rotate-list/
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class RotateLinkedList:

    """ T(c) -> O(n + n) => O(2n) , S(c) -> O(1) """
    def rotateRight(self, head, k):
        # edge case -> linked list empty or zero rotation
        if head == None or k == 0:
            return head
        
        # calculate length of linked list
        length = 1
        tail = head
        while tail.next != None:
            length += 1
            tail = tail.next
            
        # if k is multiple of length, after rotation it will be same 
        if k % length == 0:
            return head
        
        # incase of larger value of k
        k = k % length
        
        # as after rotating, last node will point to previous head
        tail.next = head
        
        # this willbe last node after rotation
        diff = length - k
        
        # go to that node using temp
        temp = head
        cnt = 1
        while temp != None:
            if cnt == diff:
                break
            cnt += 1
            temp = temp.next
        
        # head will be next of temp node
        head = temp.next
        
        # temp will be last node
        temp.next = None
        
        return head
    

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

    # Print the original linked list
    print("Original Linked List:", end=" ")
    print_linked_list(head)

    head = RotateLinkedList().rotateRight(head, 2)
    print("Rotated Linked List:", end=" ")
    print_linked_list(head)


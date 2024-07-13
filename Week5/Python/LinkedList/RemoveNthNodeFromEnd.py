"""
    Given the head of a linked list, remove the nth node from the end of the list and return its head.
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

    https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class RemoveNthNodeFromEnd:
    """ T(c) -> O(length) + O(length-n) => O(2n) , S(c) -> O(1) """
    def removeNthFromEnd(self, head, n):
        length = 0
        # calculate length of linked list
        temp = head
        while temp != None:
            length += 1
            temp = temp.next
        
        # if we need to delete the first node
        if length == n:
            head = head.next
            return head
        
        # find after how many nodes that del_node is present
        diff = length - n
        
        temp = head
        while diff > 0:
            diff -= 1
            if diff == 0:
                break
            temp = temp.next
        
        
        # delete that node
        temp.next = temp.next.next
            
        return head
    

    """ T(c) -> O(length) , S(c) -> O(1) """
    def removeNthFromEndEfficient(self, head, n):
        # using fast and slow pointers and updating one with a delay of n steps.
        fast = head

        # move fast pointers to n node from starting
        for i in range(n):
            fast = fast.next
            
        # we need to delete first node if fast is null 
        if fast == None:
            head = head.next
            return head
        
        # slow pointer will point at previous node of del_node after iteration
        slow = head
        while fast.next != None:
            # move both fast and slow pointer
            slow = slow.next
            fast = fast.next
            
        # delete that node
        slow.next = slow.next.next
        
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
    head.next.next.next.next = Node(5)

    # print linked list
    print_linked_list(head)

    # head = RemoveNthNodeFromEnd().removeNthFromEnd(head, 2)
    # print_linked_list(head)

    head = RemoveNthNodeFromEnd().removeNthFromEndEfficient(head, 5)
    print_linked_list(head)

"""
    Given the head of a linked list, return the list after sorting it in ascending order.

    https://leetcode.com/problems/sort-list/
"""


class ListNode:
    def __init__(self, data, next_node=None):
        self.val = data
        self.next = next_node


class SortLinkedList:
    """ T(c) -> O(logn * (n/2 + n)) , S(c) -> O(1) """
    def sortList(self, head):
        
        # if no node or only one node present
        if head == None or head.next == None:
            return head
        
        # find middle
        middleNode = self.findMiddle(head)
        
        # break into 2 list
        leftHead = head
        rightHead = middleNode.next
        
        # make left list end null
        middleNode.next = None
        
        # left list
        leftHead = self.sortList(leftHead)
        # right list
        rightHead = self.sortList(rightHead)
        
        # merge both list
        return self.merge(leftHead, rightHead)
    
    
    def merge(self, head1, head2):
        t1 = head1
        t2 = head2
        
        # create an extra dumy Node
        dummyNode = ListNode(-1)
        temp = dummyNode
        
        while t1 != None and t2 != None:
            if t1.val < t2.val:
                temp.next = t1
                temp = t1
                t1 = t1.next
            else:
                temp.next = t2
                temp = t2
                t2 = t2.next
        
        # if nodes left in t1
        if t1 != None:
            temp.next = t1
        # if nodes left in t2
        else:
            temp.next = t2
            
        return dummyNode.next
                
        
    def findMiddle(self, head):
        slow = head
        fast = head.next
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        return slow


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()


if __name__ == '__main__':
    head1 = ListNode(4)
    head1.next = ListNode(3)
    head1.next.next = ListNode(2)
    head1.next.next.next = ListNode(1)

    # Print the original linked list
    print("Original Linked Lists:", end=" ")
    print_linked_list(head1)

    head = SortLinkedList().sortList(head1)
    print("Sorted Linked List:", end=" ")
    print_linked_list(head)

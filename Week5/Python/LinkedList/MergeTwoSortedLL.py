"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

https://leetcode.com/problems/merge-two-sorted-lists/
"""

class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


class MergeTwoSortedLinkedList:
    """ T(c) -> O(n1 + n2) , S(c) -> O(1) """
    def mergeTwoLists(self, list1, list2):
        t1 = list1
        t2 = list2
        
        # create a dummy node, which will be starting node
        dummyNode = ListNode(-1)
        temp = dummyNode
        
        # if node of both linked list are present
        while t1 != None and t2 != None:
            if t1.val < t2.val:
                temp.next = t1
                temp = t1
                t1 = t1.next
            else:
                temp.next = t2
                temp = t2
                t2 = t2.next
                
        # if first linked list is remaining
        if t1 != None:
            temp.next = t1
        # if second linked list is remaining    
        else:
            temp.next = t2
            
        return dummyNode.next
    

def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.val, end=" ")
        temp = temp.next
    print()


if __name__ == '__main__':
    head1 = ListNode(1)
    head1.next = ListNode(2)
    head1.next.next = ListNode(4)

    head2 = ListNode(1)
    head2.next = ListNode(3)
    head2.next.next = ListNode(4)

    # Print the original linked list
    print("Original Linked Lists:", end=" ")
    print_linked_list(head1)
    print_linked_list(head2)

    head = MergeTwoSortedLinkedList().mergeTwoLists(head1, head2)
    print("Merged Linked List:", end=" ")
    print_linked_list(head)
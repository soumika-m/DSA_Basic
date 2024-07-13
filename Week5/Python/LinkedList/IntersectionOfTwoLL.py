"""
    Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two 
    linked lists have no intersection at all, return null.

    https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Intersection_Of_Two_Linked_List:

    """ T(c) -> O(m+n) , S(c) -> O(n) """
    def getIntersectionNode(self, headA, headB):

        hashset = set()
        
        # insert nodes of linked list 1 in set
        temp1 = headA
        while temp1 != None:
            hashset.add(temp1)
            temp1 = temp1.next
        
        # travarse linked list 2 and check if node is already present in set, intersection point
        temp2 = headB
        while temp2 != None:
            if temp2 in hashset:
                return temp2
            
            temp2 = temp2.next
        
        # if no intersection point found, return None
        return None
    

    """ T(c) -> O(m) + O(n) + O(abs(m-n)) + O(min(m,n)) , S(c) -> O(1) """
    def getIntersectionNodeBetter(self, headA, headB):
        
        diff = self.getLengthDifference(headA, headB)
        # difference is negative, list 2 is bigger
        if diff < 0:
            while diff != 0:
                headB = headB.next
                diff = diff + 1
        
        # difference is positive, list 1 is bigger
        else:
            while diff != 0:
                headA = headA.next
                diff = diff - 1
        
        # iterate both linked list, and check for equal node
        while headA != None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        
        # if no intersection point present
        return None
   
    def getLengthDifference(self, head1, head2):
        len1 = 0
        len2 = 0
        
        # iterate both linked list, and calculate the length
        while head1 != None:
            len1 += 1
            head1 = head1.next
                
        while head2 != None:
            len2 += 1
            head2 = head2.next
        
        return len1 - len2


    """ T(c) -> O(m+n) , S(c) -> O(1) """
    def getIntersectionNodeOptimal(self, headA, headB):
        # if any of the linked list is empty
        if headA == None or headB == None:
            return None
        
        t1 = headA
        t2 = headB
        
        # iterate both linked list simultaneously
        while t1 != t2:
            t1 = t1.next
            t2 = t2.next
            
            # if both linked list node matches
            if t1 == t2:
                return t1
            
            # if t1 reached at null, move it to second linked list head
            if t1 == None:
                t1 = headB
            
            # if t2 reached at null, move it to first linked list head
            if t2 == None:
                t2 = headA
                
        return t1


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()


if __name__ == '__main__':
    head1 = Node(1)
    head1.next = Node(9)
    head1.next.next = Node(1)
    head1.next.next.next = Node(2)
    head1.next.next.next.next = Node(4)

    print("Linked list 1 :", end=" ")
    print_linked_list(head1)
    
    head2 = Node(3)
    head2.next = head1.next.next.next

    print("Linked list 2 :", end=" ")
    print_linked_list(head2)

    head = Intersection_Of_Two_Linked_List().getIntersectionNode(head1, head2)
    print("Intersection point :", head.data)

    head = Intersection_Of_Two_Linked_List().getIntersectionNodeBetter(head1, head2)
    print("Intersection point :", head.data)

    head = Intersection_Of_Two_Linked_List().getIntersectionNodeOptimal(head1, head2)
    print("Intersection point :", head.data)

"""
    Given two linked lists, your task is to complete the function makeUnion(), that returns the union list of two linked lists. 
    This union list should include all the distinct elements only and it should be sorted in ascending order.

    https://www.geeksforgeeks.org/problems/union-of-two-linked-list/1
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Union_Of_Two_LinkedList:
    """ T(c) -> O((n+m) * log(n+m)) , S(c) -> O(n+m) """
    def union(self, head1,head2):

        # create set to discard duplicates
        set_data = set()
        
        # add 1st linkedlist elements in set 
        temp1 = head1
        while temp1 != None:
            set_data.add(temp1.data)
            temp1 = temp1.next
        
        # add 2nd linkedlist elements in set   
        temp2 = head2
        while temp2 != None:
            set_data.add(temp2.data)
            temp2 = temp2.next
        
        # convert into list    
        list_data = list(set_data)
        # sort list in reverse order
        list_data.sort(reverse=True)
        
        # create new linked list and insert data from beginning
        head = None
        for d in list_data:
            temp = Node(d)
            if head == None:
                head = temp
            else:
                temp.next = head
                head = temp
        
        # return head of resultant linkedlist        
        return head


def print_linked_list(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print()



if __name__ == '__main__':
    head1 = Node(9)
    head1.next = Node(6)
    head1.next.next = Node(4)
    head1.next.next.next = Node(2)
    head1.next.next.next.next = Node(3)
    head1.next.next.next.next.next = Node(8)

    print("Linked list 1 :", end=" ")
    print_linked_list(head1)

    head2 = Node(1)
    head2.next = Node(2)
    head2.next.next = Node(8)
    head2.next.next.next = Node(6)
    head2.next.next.next.next = Node(2)

    print("Linked list 2 :", end=" ")
    print_linked_list(head2)

    head = Union_Of_Two_LinkedList().union(head1, head2)
    print("Linked list after union operation :", end = " ")
    print_linked_list(head)

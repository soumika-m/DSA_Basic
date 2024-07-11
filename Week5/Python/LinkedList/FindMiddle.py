"""
    Given head of a linked list, the task is to find the middle. For example, the middle of 1-> 2->3->4->5 is 3. If there are two 
    middle nodes (even count), return the second middle. For example, middle of 1->2->3->4->5->6 is 4.

    https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1
"""

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Find_Middle:
    #  Should return data of middle node. If linked list is empty, then  -1
    """ T(c) -> O(n + n/2), S(c) -> O(1) """
    def findMid(self, head):
        
        if head.next is None:
            return head.data
            
        count = 0
        curr = head
        # calculate length of linked list
        while curr != None:
            count += 1
            curr = curr.next
        
        mid = (count // 2) + 1
        curr = head

        # go to mid position by travarsing
        while curr != None:
            mid -= 1
            # if middle position is reached
            if mid == 0:
                break
            
            curr = curr.next
        
        # return the value stored in the middle node
        return curr.data

    
    """ T(c) -> O(n/2), S(c) -> O(1) """
    def findMidEfficient(self, head):

        # Using tortoiseHare method
        slow = head
        fast = head
        
        # for even nodes fast pointer will stop at null, for odd nodes fast pointer will stop at the last node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # return the value stored in the middle node
        return slow.data


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

    # Find the middle node
    middle_node = Find_Middle().findMid(head)

    # Display the value of the middle node
    print("The middle node value is:", middle_node)

    head.next.next.next.next.next = Node(6)

    # print linked list
    print_linked_list(head)

    # Find the middle node using efficient method
    middle_node = Find_Middle().findMidEfficient(head)

    # Display the value of the middle node
    print("The middle node value is:", middle_node)

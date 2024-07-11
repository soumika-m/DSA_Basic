"""
    Given the head of a singly linked list, the task is to check if the linked list has a loop. 
    A loop means that the last node of the linked list is connected back to a node in the same list.  
    So if the next of the last node is null. then there is no loop. We need to return true if there 
    is a loop, otherwise false.

    https://www.geeksforgeeks.org/problems/detect-loop-in-linked-list/1
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class Detect_Loop:

    # Function to check if the linked list has a loop.
    """ T(c) -> O(n), S(c) -> O(n) """
    def detectLoop(self, head):
        # using hashing
        temp = head
        
        node_set = set()
        
        while temp != None:
            # node is already present in hash table, hence loop exist
            if temp in node_set:
                return True
            
            # add node in hash table
            node_set.add(temp)
            temp = temp.next
        
        return False


    # Function to check if the linked list has a loop.
    """ T(c) -> O(n), S(c) -> O(1) """
    def detectLoopEfficient(self, head):
        # using slow and fast pointers
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
            # loop present
            if slow == fast:
                return True

        return False
        

if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    # Check if there is a loop
    # in the linked list
    if Detect_Loop().detectLoop(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")

    # Create a loop
    fifth.next = third

    if Detect_Loop().detectLoopEfficient(head):
        print("Loop detected in the linked list.")
    else:
        print("No loop detected in the linked list.")
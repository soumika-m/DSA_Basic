class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
def create_ll_from_array(head, arr):
    head = Node(arr[0])
    curr = head

    for i in range(1, len(arr)):
        temp  = Node(arr[i])
        curr.next = temp
        curr = temp

    print("Converted array into linked list successfully")
    return head

def print_ll(head):
    curr = head
    print("printing data--->")
    while curr is not None:
        print(curr.data , end = " ")
        curr = curr.next
    print()

def countLen(head):
    curr = head
    count = 0
    while curr is not None:
        count += 1
        curr = curr.next

    print("LL length = ", count)


def search(head, val):
    curr = head
    while curr is not None:
        if curr.data == val:
            print(f"{val} Found in LL")
            return
        curr = curr.next
    
    print(f"{val} Not found in LL")


def insert_begin(head, val):
    temp = Node(val)
    temp.next = head
    head = temp
    print(f"{val} Inserted at begin")
    return head


def insert_end(head, val):
    temp = Node(val)
    if head is None:
        head = temp
        return
    
    curr = head
    while curr.next != None:
        curr = curr.next

    curr.next = temp
    print(f"{val} Inserted at the end")


def delete_begin(head):
    if head is None:
        print("Nothing to delete")
        return
    
    val = head.data
    head = head.next
    print(f"{val} deleted from begin ")
    return head


def delete_end(head):
    # no node present
    if head is None:
        print("Nothing to delete")
        return
    
    # only one node present
    if head.next is None:
        print(f"{head.data} deleted from ll end")
        head = None
        return

    curr = head
    while curr.next.next is not None:
        curr = curr.next

    val = curr.data
    curr.next = None
    print(f"{val} deleted from end")


def main():
    arr = [2,3,4] 
    head = None
    head = create_ll_from_array(head, arr)
    print_ll(head)
    head = insert_begin(head, 5)
    insert_end(head, 6)
    countLen(head)
    print_ll(head)
    head = delete_begin(head)
    delete_end(head)
    print_ll(head)
    search(head, 3)

main()
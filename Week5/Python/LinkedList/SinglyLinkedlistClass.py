class Node:
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def create_ll_from_array(self, arr):
        self.head = Node(arr[0])
        curr = self.head

        for i in range(1, len(arr)):
            temp  = Node(arr[i])
            curr.next = temp
            curr = temp

        print("Converted array into linked list successfully")

    
    def print_ll(self):
        curr = self.head
        print("printing data--->")
        while curr is not None:
            print(curr.data , end = " ")
            curr = curr.next
        print()


    def count_len(self):
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next

        print("LL length = ", count)
        return count


    def search(self, val):
        curr = self.head
        while curr is not None:
            if curr.data == val:
                print(f"{val} Found in LL")
                return
            curr = curr.next
        
        print(f"{val} Not found in LL")


    def insert_begin(self, val):
        temp = Node(val)
        temp.next = self.head
        self.head = temp
        print(f"{val} Inserted at begin")


    def insert_end(self, val):
        temp = Node(val)
        # no element present
        if self.head is None:
            self.head = temp
            return
        
        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = temp
        print(f"{val} Inserted at the end")


    def insert_middle(self, val):
        n = self.count_len()

        # no node present
        if n == 0:
            temp = Node(val)
            self.head = temp
            print(f"{val} inserted at the middle")
            return

        n = n//2

        count = 1
        curr = self.head
        while count != n:
            count += 1
            curr = curr.next

        temp = Node(val)
        temp.next = curr.next
        curr.next = temp
        print(f"{val} inserted at the middle")


    def insert_pos(self, val, k):
        # no node present
        if self.head is None:
            # insert begin
            if k == 1:
                self.head = temp
                print(f"{val} element inserted successfully in {k} position")
                return
            
            print(f"{k} is not valid position to insert")
            return
        
        temp = Node(val)
        
        # insert begin
        if k == 1:
            temp.next = self.head
            self.head = temp
            print(f"{val} element inserted successfully in {k} position")
            return
        
        # insert at positions
        count = 0
        curr = self.head
        while curr != None:
            count += 1
            if count == k-1:
                temp.next = curr.next
                curr.next = temp
                print(f"{val} element inserted successfully in {k} position")
                return

            curr = curr.next

        print(f"{k} is not valid position to insert")
        return


    def delete_begin(self):
        if self.head is None:
            print("Nothing to delete")
            return
        
        val = self.head.data
        self.head = self.head.next
        print(f"{val} deleted from begin")


    def delete_end(self):
        # no node present
        if self.head is None:
            print("Nothing to delete")
            return
        
        # only one node present
        if self.head.next is None:
            print(f"{self.head.data} deleted from ll end")
            self.head = None
            return

        curr = self.head
        while curr.next.next is not None:
            curr = curr.next

        val = curr.data
        curr.next = None
        print(f"{val} deleted from end")


    def delete_middle(self):
        n = self.count_len()

        # no node present
        if n == 0:
            print("Nothing to delete")
            return
        
        n = n//2
        
        # one node present
        if n == 1:
            self.head = self.head.next
            print(f"Node deleted from middle from {n+1}th position")
            return
        
        count = 1
        curr = self.head
        while count != n:
            count += 1
            curr = curr.next

        curr.next = curr.next.next
        print(f"Node deleted from middle from {n+1}th position")


    def delete_pos(self, k):
        # no element present
        if self.head is None:
            return
        
        # only one element present
        if self.head.next is None:
            if k == 1:
                self.head = self.head.next
                print(f"{k}th element deleted successfully")
                return
            
            print(f"{k} is not valid position to delete")
            return

        # element added in begin   
        if k == 1:
            self.head = self.head.next
            print(f"{k}th element deleted successfully")
            return
        
        count = 0
        curr = self.head
        while curr != None:
            count += 1
            if count == k-1:
                if curr.next.next is not None:
                    curr.next = curr.next.next
                else:
                    curr.next = None

                print(f"{k}th element deleted successfully")
                return

            curr = curr.next
        
        print(f"{k} is not valid position to delete")


def main():
    arr = [2,3,4]
    ll = SinglyLinkedList()  
    ll.create_ll_from_array(arr)
    ll.print_ll()
    ll.insert_begin(5)
    ll.insert_end(6)
    ll.count_len()
    # ll.print_ll()
    ll.delete_begin()
    ll.delete_end()
    # ll.print_ll()
    ll.search(3)
    ll.insert_pos(5,1)
    # ll.print_ll()
    ll.insert_pos(1,5)
    ll.print_ll()
    ll.delete_pos(1)
    ll.print_ll()
    ll.delete_pos(4)
    ll.print_ll()
    ll.insert_pos(6, -1)
    # ll.print_ll()
    ll.insert_middle(5)
    ll.print_ll()
    ll.insert_middle(6)
    ll.print_ll()
    ll.delete_middle()
    ll.print_ll()
    ll.delete_middle()
    ll.print_ll()

main()
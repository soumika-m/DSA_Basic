"""
    Given a stack, the task is to sort it such that the top of the stack has the greatest element.
    https://www.geeksforgeeks.org/problems/sort-a-stack/1
"""

class SortStack:
    """ T(c) -> O(n^2) , S(c) -> O(n) """
    def Sorted(self, s):
        top = len(s) - 1
        # if no element present in stack
        if top == -1:
            return
        
        # remove top element
        temp = s.pop()
        # sort stack
        self.Sorted(s)
        # push temp in correct place
        self.insert(s, temp)
        
    def insert(self, s, temp):
        top = len(s) - 1
        
        # if no element present, or top element is smaller
        if top == -1 or s[top] <= temp:
            s.append(temp)
            return
        
        # pop element
        popped_elem = s.pop()
        # insert temp
        self.insert(s, temp)
        # append popped element
        s.append(popped_elem)


if __name__ == "__main__":
    stack = [11, 2, 32, 3, 41]
    print(stack)
    SortStack().Sorted(stack)
    # print(stack)
    for e in range(len(stack)):
        print(stack.pop(), end=" ")
    print()

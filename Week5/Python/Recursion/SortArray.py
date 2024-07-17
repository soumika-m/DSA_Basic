""" 
    Sort an array using recursion
    T(c) -> O(n^2) , S(c) -> O(n)
"""

def sort(arr, n):
    if n == 1:
        return
    
    temp = arr[n-1]
    sort(arr, n-1)
    insert(arr, n-1, temp)


def insert(arr, n, temp):
    if n == 0 or arr[n-1] <= temp:
        arr[n] = temp
        return
    
    # shift element to right
    arr[n] = arr[n-1]
    insert(arr, n-1, temp)
    

if __name__ == "__main__":
    arr = [4,2,3,1]
    print(arr)
    sort(arr, len(arr))
    print(arr)
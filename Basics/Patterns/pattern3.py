"""
if N = 6,

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

"""

def pattern3(N):
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(j, end=" ")

        print()

pattern3(6)

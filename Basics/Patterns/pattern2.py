"""
if N = 6,

* 
* * 
* * *
* * * *
* * * * *
* * * * * *

"""

def pattern2(N):
    for i in range(1, N+1):
        for _ in range(i):
            print("*", end=" ")

        print()

pattern2(6)

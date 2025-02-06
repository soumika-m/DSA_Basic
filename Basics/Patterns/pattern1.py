"""
https://takeuforward.org/strivers-a2z-dsa-course/must-do-pattern-problems-before-starting-dsa/

if N = 6,

* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *
* * * * * *

"""

def pattern1(N):
    for _ in range(N):
        for _ in range(N):
            print("*", end=" ")
        print()

pattern1(6)

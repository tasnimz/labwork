import sys

def staircase(n):
    for i in range(1,n+1):
        print(" "*(n-1)+ "#"*i)

if __name__ == '__main__':

    n = 4

    staircase(n)

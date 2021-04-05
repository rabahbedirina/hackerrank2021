#! /bin/python3
def solve():






    return None





n=int(input())
for _ in range(n):
    # arr=input().split() # list string and integer
    arr = list(map(int, input().split())) # only integer or string 
    result=solve(arr)
    print(result)

#! /bin/python3
def solve(arr):
    return len(set(arr))


n=int(input())
arr=[]
for _ in range(n):
    arr.append(str(input()))

result=solve(arr)

print(result)

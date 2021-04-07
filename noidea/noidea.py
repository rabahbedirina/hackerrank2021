#! /bin/python3
def solve(n,m,arr,a,b):
    ha=sum([(i in a)-(i in b) for i in arr])
    return ha


n,m=map(int,input().split())
arr = list(map(int, input().split())) # only integer or string 

# arr=input().split() # list string and integer
a = set(map(int, input().split())) # only integer or string 
b = set(map(int, input().split())) # only integer or string 
result=solve(n,m,arr,a,b)
print(result)
# result =10
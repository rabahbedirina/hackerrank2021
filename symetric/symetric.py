#! /bin/python3
def solve(n,arr1,m,arr2):
    uni=arr1.union(arr2)
    inter=arr1.intersection(arr2)
    diff=uni.difference(inter)
    for i in sorted(diff):
        print(i)
    



n=int(input())
arr1 = set(map(int, input().split())) # only integer or string 
m=int(input())
arr2 = set(map(int, input().split())) # only integer or string 
solve(n,arr1,m,arr2)
    

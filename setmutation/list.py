def solve(arr1,task,arr2) :
    
    action=task[0]
    if action=="update":
        arr1.update(arr2)
    elif action=="intersection_update":
        arr1.intersection_update(arr2)
    elif action=="difference_update":
        arr1.difference_update(arr2)
    elif action=="symmetric_difference_update":
        arr1.symmetric_difference_update(arr2)    
        
    return print(arr1)


n=int(input())
arr1=set(map(int,input().split()))
m=int(input())

for _ in range(m):
    task=input().split()
    arr2=set(map(int,input().split()))
    solve(arr1,task,arr2)

print(sum(arr1))
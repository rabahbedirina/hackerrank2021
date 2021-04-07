#! /bin/python3
def merge_the_tools(string, k):
    n=len(string)
    for i in range(0,n,k):
        arr=[]
        for x in string[i:i+k] :
            if x not in arr:
                arr.append(x)
        
        print("".join(arr))



t=int(input())
for _ in range(t):

    if __name__ == '__main__':
        string, k = input(), int(input())
        merge_the_tools(string, k)
def average(array):
    average=sum(set(arr))/len(set(arr))

    return average


# input
input1=10
input2="161 182 161 154 176 170 167 171 170 174"
# Expected Output
output1=169.37

if __name__ == '__main__':
    n = int(input1)
    arr = list(map(int, input2.split()))
    result = average(arr)
    print(result)
    
    assert result==output1
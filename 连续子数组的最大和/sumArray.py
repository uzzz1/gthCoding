def sumArr(arr):
    for i in range(1,len(arr)):
        arr[i] += max(arr[i-1],0)
    return max(arr)

print(sumArr([-2,1,-3,4,-1,2,1,-5,4]))
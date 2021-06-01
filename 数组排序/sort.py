#快速排序
def sortf(arr):
    if len(arr) <= 1:
        return arr
    else :
        standard = arr[0]
        left = [i for i in arr[1:] if i <= standard]
        right = [i for i in arr[1:] if i > standard]
        return sortf(left) + [standard] + sortf(right)

test = [5,3,7,9,2,1,8,5,2]
print(sortf(test))
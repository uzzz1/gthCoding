#方法一：这是典型的解决楼梯问题的计算方法，但是需注意，这种方法在计算n=90时效率极低
def solution1(n):
    if n == 1 or n == 0:
        return 1
    else :
        return solution1(n-1) + solution1(n-2)

#方法二
def solution2(n):
    i = 1
    j = 1
    for k in range(n):
        i,j = j,j+i
    return i

if __name__ == "__main__":
    n = 10
    #n = 20
    #n = 90
    print(solution1(n))
    print(solution2(n))


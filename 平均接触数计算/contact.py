import numpy as np
import os
import time
def readin(name):                                            ###读入格点信息，可以直接用，前提是文件中需要全部是数字字符
    f = np.loadtxt(name,dtype=int)
    return f

def period(arr,peri,limit0,limit1):                          ###周期性边界条件函数，输入参数：数组，周期，下限，上限
    index = (arr > limit1)
    arr[index] = arr[index] - peri
    index = (arr < limit0)
    arr[index] = arr[index] + peri
    return arr

def neibor():                                                ###规定近邻，采用18近邻
    nearPool = np.array([[i,j,k] for i in range(-1,2) for j in range(-1,2) for k in range(-1,2) if 0<i**2+j**2+k**2<3])
    nearList = np.array([pointInf[:,:3] + i for i in nearPool]).reshape(-1,3)
    for i in range(3):
        nearList[:,i][nearList[:,i] == -1] = ln[i] - 1
        nearList[:,i][nearList[:,i] == ln[i]] = 0
    nna = (nearList[:,0]*ly*lz+nearList[:,1]*lz+nearList[:,2]).reshape((-1,18))
    return nna

def numCount(nna):                                           ###计算每一种格点周围的近邻
    count = np.zeros((kindn-1,kindn-1),dtype=float)
    for i in range(1,kindn):
        index = (pointInf[:,3] == i)
        neiInd = nna[index]
        n = len(neiInd)
        countList = pointInf[neiInd]
        for j in countList:
            for k in range(1,kindn-1):
                numInd = (j[:,3] == k)
                tem = j[numInd]
                count[i-1][k-1] += len(tem)
        count[i-1] = count[i-1]/n
    return count

def pathFind(f1):                                            ###路径寻找，以便于计算这一文件所在文件夹下所有的平均接触数
    ls = []
    pathNow = os.getcwd()
    for root,_,files in os.walk(pathNow):
        if f1 in files :
            ls.append(root)
    return ls

def cal(f1,filen):
    global pointInf
    pointInf = readin(f1)
    nna = neibor()
    count = numCount(nna)
    np.savetxt(filen,count)
    # with open(filen,'w') as f:
    #     f.write('naa = {}\n'.format(count[0][0]))
    #     f.write('nab = {}\n'.format(count[0][1]))
    #     f.write('nao = {}\n'.format(count[0][2]))
    #     f.write('naw = {}\n'.format(count[0][3]))
    #     f.write('nas = {}\n'.format(count[0][3]+count[0][2]))
    #     f.write('nba = {}\n'.format(count[1][0]))
    #     f.write('nbb = {}\n'.format(count[1][1]))
    #     f.write('nbo = {}\n'.format(count[1][2]))
    #     f.write('nbw = {}\n'.format(count[1][3]))
    #     f.write('nbs = {}\n'.format(count[1][3]+count[1][2]))
    #     f.write('nwa = {}\n'.format(count[3][0]))
    #     f.write('nwb = {}\n'.format(count[3][1]))
    #     f.write('nwo = {}\n'.format(count[3][2]))
    #     f.write('nww = {}\n'.format(count[3][3]))
    #     f.write('noa = {}\n'.format(count[2][0]))
    #     f.write('nob = {}\n'.format(count[2][1]))
    #     f.write('now = {}\n'.format(count[2][3]))
    #     f.write('noo = {}\n'.format(count[2][2]))

def main():
    f1 = 'e5.txt'               #格点信息文件
    filen = 'data.txt'          #输出数据文件
    ls = pathFind(f1)
    for i in ls :
        f2 = os.path.join(i,f1)
        f3 = os.path.join(i,filen)
        cal(f2,f3)

if __name__ == "__main__":
    start = time.time()
    kindn = 5                   #组分数目
    lx = 60                     #
    ly = 60                     #
    lz = 60                     #盒子边长
    ln = [lx,ly,lz]
    llx = lx/2
    lly = ly/2
    llz = lz/2
    ntot = lx*ly*lz
    main()
    print(time.time() - start)

import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from sklearn.cluster import DBSCAN
from mpl_toolkits.mplot3d import Axes3D

def Rcal(atom1,atom2) :                                      ###优化完成
    atoma = atom1[:3]
    atomb = atom2[:3]
    rr0 = atoma - atomb
    for i in range(3):
        if abs(rr0[i]) > llh :
            rr0[i] = abs(rr0[i]) - ll
    return np.sqrt(sum(rr0**2))

def dataCluster():
    fig = plt.figure()
    ax = Axes3D(fig)
    C3 = DBSCAN(eps,minPts,metric=Rcal).fit(X)
    labels = C3.labels_
    nCluster = len(set(labels)) - (1 if -1 in labels else 0 )
    for i in range(nCluster):
        x0 = X[np.where(labels == i)]
        ax.scatter(x0[:,0],x0[:,1],x0[:,2],marker = 'o',label = 'label'+str(i))
    plt.legend(loc = 2)
    plt.show()
    return nCluster,labels

def massCenter(data):
    ### 1.判断同一个团里是否有周期性近邻
    ### 2.更改周期性近邻的格点坐标
    ### 3.计算更改后的质心
    perx = 0
    pery = 0
    perz = 0
    data0 = data[:,:3]
    indexx = (data0[:,0] == 0)
    tempx = data0[indexx]
    tempx[:,0] += 59
    for t in tempx:
        if t in data0:
            perx = 1                ###x方向需要周期性
            break
    indexy = (data0[:,1] == 0)
    tempy = data0[indexy]
    tempy[:,1] += 59
    for t in tempy:
        if t in data0:
            pery = 1
            break
    indexz = (data0[:,2] == 0)
    tempz = data0[indexz]
    tempz[:,2] += 59
    for t in tempz:
        if t in data0:
            perz = 1
            break
    if perx == 1:
        index = np.where(data0[:,0] < 20)
        data0[index] += [60,0,0]
    if pery == 1:
        index = np.where(data0[:,1] < 20)
        data0[index] += [0,60,0]
    if perz == 1:
        index = np.where(data0[:,2] < 20)
        data0[index] += [0,0,60]
    num = len(data)
    sumX = sum(data0[:,0])
    sumY = sum(data0[:,1])
    sumZ = sum(data0[:,2])
    x0 = int(sumX/num + 0.5)
    y0 = int(sumY/num + 0.5)
    z0 = int(sumZ/num + 0.5)
    mc = [x0,y0,z0]
    # for i in range(3):
    #     if mc[i] < 0:
    #         mc[i] += ll
    #     elif mc[i] > 60:
    #         mc[i] -= ll
    mc = np.array(mc)
    return mc

def dataDeal(labels,nCluster):
    eb = []                     #存的是非球形因子
    eList = []                  #存三个方向的特征值
    Alist = []                  #存有多少个A单体
    wlist = []                  #存有多少个水溶剂
    k = []                      #存相对各向异性
    for i in range(nCluster):
        S0 = np.zeros([3,3],int)
        index0 = (labels == i)
        cluster = X[index0]
        clusterIcha = ABunits[index0]
        mc = massCenter(cluster)
        temp = cluster - mc
        # index = (temp > llh)
        # temp[index] = temp[index] - ll
        # index = (temp < -llh)
        # temp[index] = temp[index] + ll   #根据需要自行判断是否需要进行周期性边界条件
        for j in range(3):
            for k in range(3):
                S0[j][k] = np.sum(temp[:,j]*temp[:,k])
        MS = Matrix(S0/len(cluster))
        _,D = MS.diagonalize()
        diaD = np.diagonal(D)
        eList.append(diaD)
        diaD = np.sort(diaD)
        tot = sum(diaD)
        g = (diaD[2] - 0.5*(diaD[1]+diaD[0]))/tot
        c = (diaD[1] - diaD[0])/tot
        k2 = g**2 + 3/4*(c**2)
        k.append(k2)
        indexA = (clusterIcha[:,3] == 1)
        na = len(clusterIcha[indexA])
        indexW = (clusterIcha[:,3] == 4)
        nw = len(clusterIcha[indexW])
        Alist.append(na)
        wlist.append(nw)
        eb.append(g)
    return eList,Alist,wlist,eb,k



def main():
    nCluster,labels = dataCluster()                           #1.聚类
    etot,alist,wlist,eb,k = dataDeal(labels,nCluster)
    print(etot,alist,wlist,eb,k)
    np.savetxt('dialog.txt',etot,fmt="%.3f",delimiter=',')
    np.savetxt('Alist.txt',alist,fmt="%d",delimiter=',')
    np.savetxt('wlist.txt',wlist,fmt="%d",delimiter=',')
    np.savetxt('eb.txt',eb,fmt="%.4f",delimiter=',')
    np.savetxt('k.txt',k,fmt="%.4f",delimiter=',')


if __name__ == "__main__":
    ll = 60
    llh = ll/2
    atomList = np.loadtxt('e5.txt',dtype=int)
    index = (atomList[:,3] != 3)
    ABunits = atomList[index]
    # index = (ABunits[:,3] != 4)
    # ABunits = ABunits[index]
    X = ABunits[:,:3]
    eps = 1.5
    minPts = 15
    main()
    
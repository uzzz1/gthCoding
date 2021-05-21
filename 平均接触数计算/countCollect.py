import numpy as np
import os
import re
def readIn(fileName):
    return np.loadtxt(fileName,dtype=float)

def fileSearch(fileName):
    pathList = []
    path = os.getcwd()
    for root,_,files in os.walk(path):
        if fileName in files:
            pathList.append(os.path.join(root,fileName))
    return pathList

def strMatch(fileName,strName):
    f = open(fileName)
    content = f.readlines()
    for i in content:
        if strName in i :
            a = i[6:]
    return a

def dirMatch(pathList):
    pathNew = []
    nameList = ['cw.05','cw.10','cw.20','cw.30','cw.40','cw.50','cw.60','cw.70','cw.80','cw.90','cw.95']
    for i in nameList:
        for j in pathList:
            if re.search(i,j) != None:
                pathNew.append(j)
                continue
    return pathNew

def main():
    pathList = fileSearch(fileName)
    pathNew = dirMatch(pathList)
    f2 = open(fileName2,'w+')
    linName = ['0.05','0.10','0.20','0.30','0.40','0.50','0.60','0.70','0.80','0.90','0.95']
    count = 0
    for i in pathNew:
        data = readIn(i)
        s = linName[count]
        for j in data.reshape(1,-1)[0]:
            s = s + '   ' + str(j)
        f2.writelines(s)
        f2.write('\n')
        count += 1
    f2.close()
    print(pathNew)
    

if __name__ == "__main__":
    fileName = 'data.txt'
    fileName2 = 'contact_number.txt'
    main()
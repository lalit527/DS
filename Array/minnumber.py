def checkDupVal(data, min):
    tmpIndx = min
    for i in range(len(data)-1, min, -1):
        #print(i)
        if(data[i] == data[min]):
            tmpIndx = i
            break
    return tmpIndx

      

def getMinIndex(data, index):
    min = index
    for i in range(index+1, len(data)):
        if(data[i] < data[min]):
            min = i
    min = checkDupVal(data, min)        
    return min

def swap(data, minIndx, curIndx):
    tmp = data[minIndx]
    data[minIndx] = data[curIndx]
    data[curIndx] = tmp

def getMinNum(data):
    curIndx = 0
    while curIndx < len(data):
        if(data[curIndx] > 0):
            minIndx = getMinIndex(data, curIndx)
            if(minIndx > curIndx):
                swap(data, minIndx, curIndx)
                #break;
        curIndx += 1

num = [8,2,2,9,6,9,6,9]
getMinNum(num)
print(num)
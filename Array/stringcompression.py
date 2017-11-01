def comStrFun(data):
    if len(data) == 0:
        return ''
    count = 1
    l = len(data)
    i = 1
    r = ''
    while i < l:
        if data[i] == data[i-1]:
            count += 1
        else:
            r =  r + data[i-1] + str(count)
            count = 1
        i += 1

    r =  r + data[i-1] + str(count)
    return r
        
data = 'AAAAABBBBCCCC'
comStr = comStrFun(data)
print(comStr)

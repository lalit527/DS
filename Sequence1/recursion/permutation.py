def permutation(data, s, e):
    if s == e:
        print(data)
    for i in range(s, e):
        
        data[s], data[i] = data[i], data[s]
        # print('1', data, s, e, i)
        permutation(data, s+1, e)
        data[s], data[i] = data[s], data[i]
        # print('2', data, s, e, i)

permutation(['A', 'B', 'C'], 0, 3)



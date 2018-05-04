def flipZero(arr, m):
    n = len(arr)
    wl = wr = 0
    bestL = bestWindow = 0
    zeroCount = 0
    while wr < n:
        if zeroCount <= m:
            if arr[wr] == 0:
                zeroCount += 1
        if zeroCount > m:
            break
            if arr[wl] == 0:
                zeroCount += 1
            wl += 1
        
        if wr - wl > bestWindow:
            bestWindow = wr - wl
            bestL = wl
        wr += 1
    print(bestL, wl, wr, bestWindow) 


arr = [1, 0, 1, 1, 1, 0, 0, 1, 1, 0]
flipZero(arr, 2)
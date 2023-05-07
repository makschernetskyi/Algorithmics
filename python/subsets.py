def getSubsets(arr):
    l = len(arr)
    subsets = [[] for i in range(2**l)]
    for i, e in enumerate(arr):
        for j in range(2**i):
            subsets[2**i+j] = subsets[j]+[e]

    return subsets
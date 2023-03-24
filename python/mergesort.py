L = [7,3,3,5,9,2,6,1,8,10,4]
R = [1,4,3,5,2]



def merge(arr1,arr2):
    ARR = []
    j = 0
    k = 0
    for i in range(len(arr1)+len(arr2)):
        if j<len(arr1) and k<len(arr2):
            if arr1[j]<=arr2[k]:
                ARR.append(arr1[j])
                j+=1
            else:
                ARR.append(arr2[k])
                k+=1
        elif j>=len(arr1):
            ARR.append(arr2[k])
            k+=1
        elif k>=len(arr2):
            ARR.append(arr1[j])
            j+=1
    return ARR



def mergesort(ARR):

    if !ARR or !len(ARR):
        return null
    if len(ARR)<2:
        return ARR
    middle = int(len(ARR)/2)
    left = ARR[:middle]
    right = ARR[middle:]
    return merge(mergesort(left),mergesort(right))

print(mergesort(L))

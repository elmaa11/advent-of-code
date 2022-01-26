def getThreeEntries (arr, total):
    numEl = len(arr)
    
    for i in range(numEl):
        for j in range(i + 1, numEl):
            for k in range(j + 1, numEl):
                if int(arr[i]) + int(arr[j]) + int(arr[k]) == total:
                    return [arr[i], arr[j], arr[k]]
    
    return [0, 0]

def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for x in f:
        arr.append(x)
        
    return arr
    
arr = getThreeEntries(readTxt("input.txt"), 2020)
print(arr, int(arr[0]) * int(arr[1]) * int(arr[2]))
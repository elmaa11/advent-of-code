

def getTwoEntries (arr, total):
    numEl = len(arr)
    
    for i in range(numEl):
        for j in range(i + 1, numEl):
            if int(arr[i]) + int(arr[j]) == total:
                return [arr[i], arr[j]]
    
    return [0, 0]

def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for x in f:
        arr.append(x)
        
    return arr
    
arr = getTwoEntries(readTxt("input.txt"), 2020)
print(arr, int(arr[0]) * int(arr[1]))
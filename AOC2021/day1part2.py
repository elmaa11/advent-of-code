

def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for x in f:
        arr.append(int(x))
        
    return arr


def countIncreases(arr):
    numIncreases = 0
    numEl = len(arr)
    
    for i in range(3, numEl):
        if arr[i] > arr[i - 3]:
            numIncreases += 1
            
    return numIncreases
    
    
print(countIncreases(readTxt("input.txt")))


def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for line in f:
        temp = []
        line = line.strip()
        for i in line:
            temp.append(int(i))
        
        arr.append(temp)
    return arr

def getConsuption(arr):
    epsilon = 0b0
    gamma = 0b0
    
    numRows = len(arr)
    numCols = len(arr[0])
    
    for j in range(numCols):
        gammaCommon = 0         # counts zeros
        for i in range(numRows):            
            if arr[i][j] == 0:
                gammaCommon += 1
        
        gamma *= 0b10
        epsilon *= 0b10
        
        if gammaCommon < numRows / 2:   # there are more ones
            gamma += 0b1
        else: 
            epsilon += 0b1
    
    
    return epsilon * gamma

print(getConsuption(readTxt("inputBinary.txt")))
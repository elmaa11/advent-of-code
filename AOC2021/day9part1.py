def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for line in f:
        line = line.strip()
        temp = []
        for i in line:
            temp.append(int(i))
        arr.append(temp)
        
    return arr

def sumTotalRisk(arr):
    return sum(arr) + len(arr)

def getRisk(arr):
    lowPoints = []
    numCols = len(arr[0])
    numRows = len(arr)
    
        
    for i in range(numRows):
        for j in range(numCols):
            temp = arr[i][j]
            
            if i == 0 and j == 0:
                if temp < arr[i + 1][j] and temp < arr[i][j + 1]:
                    lowPoints.append(temp)
            elif i == 0 and j != numCols - 1:
                if temp < arr[i][j + 1] and temp < arr[i + 1][j] and temp < arr[i][j - 1]:
                    lowPoints.append(temp)
            elif i == 0 and j == numCols - 1:
                 if temp < arr[i + 1][j] and temp < arr[i][j - 1]:
                    lowPoints.append(temp)            
            elif i != 0 and i != numRows - 1 and j == 0 :
                if temp < arr[i + 1][j] and temp < arr[i][j + 1] and temp < arr[i - 1][j]:
                    lowPoints.append(temp)
            elif i != 0 and i != numRows - 1 and j == numCols - 1:
                if temp < arr[i + 1][j] and temp < arr[i][j - 1] and temp < arr[i - 1][j]:
                    lowPoints.append(temp)                    
            elif i == numRows - 1 and j == 0:
                if temp < arr[i - 1][j] and temp < arr[i][j + 1]:
                    lowPoints.append(temp)                    
            elif i == numRows - 1 and j != 0 and j != numCols - 1:
                if temp < arr[i - 1][j] and temp < arr[i][j + 1] and temp < arr[i][j - 1]:
                    lowPoints.append(temp)
            elif i == numRows - 1 and  j == numCols - 1:
                if temp < arr[i - 1][j] and temp < arr[i][j - 1]:
                    lowPoints.append(temp)                      
            else:
                if temp < arr[i - 1][j] and temp < arr[i + 1][j] and temp < arr[i][j - 1] and temp < arr[i][j + 1]:
                    lowPoints.append(temp)
    
    return lowPoints

print(sumTotalRisk(getRisk(readTxt("inputSmokeBasin.txt"))))
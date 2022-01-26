def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for line in f:
        line = line.strip()
        temp = []
        for i in line:
            temp.append([int(i), False])
        arr.append(temp)
        
    return arr

def getRisk(arr):
    lowPoints = []
    numCols = len(arr[0])
    numRows = len(arr)
    
        
    for i in range(numRows):
        for j in range(numCols):
            temp = arr[i][j][0]
            temp_arr = []
            temp_arr.append(temp)
            temp_arr.append(i)
            temp_arr.append(j)
            
            if i == 0 and j == 0:
                if temp < arr[i + 1][j][0] and temp < arr[i][j + 1][0]:
                    lowPoints.append(temp_arr)
            elif i == 0 and j != numCols - 1:
                if temp < arr[i][j + 1][0] and temp < arr[i + 1][j][0] and temp < arr[i][j - 1][0]:
                    lowPoints.append(temp_arr)
            elif i == 0 and j == numCols - 1:
                 if temp < arr[i + 1][j][0] and temp < arr[i][j - 1][0]:
                    lowPoints.append(temp_arr)            
            elif i != 0 and i != numRows - 1 and j == 0 :
                if temp < arr[i + 1][j][0] and temp < arr[i][j + 1][0] and temp < arr[i - 1][j][0]:
                    lowPoints.append(temp_arr)
            elif i != 0 and i != numRows - 1 and j == numCols - 1:
                if temp < arr[i + 1][j][0] and temp < arr[i][j - 1][0] and temp < arr[i - 1][j][0]:
                    lowPoints.append(temp_arr)                    
            elif i == numRows - 1 and j == 0:
                if temp < arr[i - 1][j][0] and temp < arr[i][j + 1][0]:
                    lowPoints.append(temp_arr)                    
            elif i == numRows - 1 and j != 0 and j != numCols - 1:
                if temp < arr[i - 1][j][0] and temp < arr[i][j + 1][0] and temp < arr[i][j - 1][0]:
                    lowPoints.append(temp_arr)
            elif i == numRows - 1 and  j == numCols - 1:
                if temp < arr[i - 1][j][0] and temp < arr[i][j - 1][0]:
                    lowPoints.append(temp_arr)                      
            else:
                if temp < arr[i - 1][j][0] and temp < arr[i + 1][j][0] and temp < arr[i][j - 1][0] and temp < arr[i][j + 1][0]:
                    lowPoints.append(temp_arr)
    
    #print(lowPoints)
    return lowPoints


def goLeft(arr, numRows, numCols, i, j, size):
    if arr[i][j][1] == False:
        arr[i][j][1] = True
        if arr[i][j][0] < 9:
            size += 1
            if j > 0:
                size = goLeft(arr, numRows, numCols, i, j - 1, size)
            if i > 0:
               size = goUp(arr, numRows, numCols, i - 1, j, size)
            if i < numRows - 1:
               size = goDown(arr, numRows, numCols, i + 1, j, size)
        
    return size

def goRight(arr, numRows, numCols, i, j, size):
    if arr[i][j][1] == False:
        arr[i][j][1] = True
        if arr[i][j][0] < 9:
            size += 1
            if j < numCols - 1:
                size = goRight(arr, numRows, numCols, i, j + 1, size)
            if i > 0:
               size = goUp(arr, numRows, numCols, i - 1, j, size)
            if i < numRows - 1:
               size = goDown(arr, numRows, numCols, i + 1, j, size)
            
    return size


def goUp(arr, numRows, numCols, i, j, size):
    if arr[i][j][1] == False:
        arr[i][j][1] = True
        if arr[i][j][0] < 9:
           size += 1
           if j > 0:
                size = goLeft(arr, numRows, numCols, i, j - 1, size)
           if j < numCols - 1:
               size = goRight(arr, numRows, numCols, i, j + 1, size)
           if i > 0:
               size = goUp(arr, numRows, numCols, i - 1, j, size)
           
    return size

def goDown(arr, numRows, numCols, i, j, size):
    if arr[i][j][1] == False:
        arr[i][j][1] = True
        if arr[i][j][0] < 9:
           size += 1
           if j > 0:
                size = goLeft(arr, numRows, numCols, i, j - 1, size)
           if j < numCols - 1:
               size = goRight(arr, numRows, numCols, i, j + 1, size)
           if i < numRows - 1:
               size = goDown(arr, numRows, numCols, i + 1, j, size)
           
    return size


def recSize(arr, numRows, numCols, i, j, size):
    if arr[i][j][1] == False:
        arr[i][j][1] = True
        if arr[i][j][0] < 9:
            size += 1
            if j > 0:
                size = goLeft(arr, numRows, numCols, i, j - 1, size)
            if j < numCols - 1:
                size = goRight(arr, numRows, numCols, i, j + 1, size)
            if i < numRows - 1:
               size = goDown(arr, numRows, numCols, i + 1, j, size)
            if i > 0:
               size = goUp(arr, numRows, numCols, i - 1, j, size)
            
    return size
    

def getTotalRisk(lowPoints, arr, numRows, numCols):
    
    numBasins = len(lowPoints)
    basinsSizes = []
    
    for i in range(numBasins):
        basinsSizes.append(recSize(arr, numRows, numCols, lowPoints[i][1], lowPoints[i][2], 0))
        
    basinsSizes.sort(reverse=True)
    
    
    return basinsSizes[0] * basinsSizes[1] * basinsSizes[2]


arr = readTxt("inputSmokeBasin.txt")
print(getTotalRisk(getRisk(arr), arr, len(arr), len(arr[0])))
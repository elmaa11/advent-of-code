def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for line in f:
        arr.append(line.replace("\n", ""))
    return arr

def countTrees(arr): 
    numTrees = 0
    rows = len(arr)
    cols = len(arr[0])
    
    for i in range(rows):
        if i * 3 >= cols: break
        if arr[i][i * 3] == "#":
            numTrees += 1
           
    return numTrees

def countTrees2(arr):   
    numTrees = 0
    rows = len(arr)
    cols = len(arr[0])
    
    for i in range(rows):
        j = i * 3
        if j >= cols: 
            j = j % cols
        if arr[i][j] == "#":
            numTrees += 1
           
    return numTrees

print(countTrees2(readTxt("inputTobogan.txt")))
def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for line in f:
        arr.append(line.split(" "))
    return arr

def getFinalPosition(arr):
    horizontal = 0
    depth = 0
    numEl = len(arr)
    
    for i in range(numEl):
        if arr[i][0] == "forward":
            horizontal += int(arr[i][1])
        elif arr[i][0] == "down":
            depth -= int(arr[i][1])
        else: depth += int(arr[i][1])
        
        
    return [horizontal, depth]

x = getFinalPosition(readTxt("inputDive.txt"))
print(x[0] * x[1])
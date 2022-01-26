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
    aim = 0
    
    for i in range(numEl):
        x = int(arr[i][1])
        if arr[i][0] == "forward":
            horizontal += x
            depth += aim * x
        elif arr[i][0] == "down":
            aim += x
        else: aim -= x
        
    return [horizontal, depth]

x = getFinalPosition(readTxt("inputDive.txt"))
print(x[0] * x[1])
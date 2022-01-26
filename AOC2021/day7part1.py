
import statistics

def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    arr = f.read().split(",");
    
    arr2 = []
    
    for i in arr:
        arr2.append(int(i))
    
    return arr2


def getMinFuel(arr):
    middle = statistics.median(arr)
    m = round(middle)
    fuel = 0
    
    print(middle)
    for i in arr:
        fuel += abs(m - i)
    
    print(fuel)
    
    return fuel

getMinFuel(readTxt("inputWhale.txt"))

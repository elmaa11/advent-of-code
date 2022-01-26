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
    middle = statistics.mean(arr)
    m = round(middle - 0.5)
    fuel = 0
    #m = 497
    print(middle, m)
    for i in arr:
        a_n = abs(m - i)
        if a_n != 0:
            fuel += (a_n * (1 + a_n)) / 2
    
    print(fuel)
    
    return fuel

def getMinFuel2(arr):
    middle = statistics.pstdev(arr)
    m = round(middle)
    fuel = 0
    arr.sort()
    print(middle)
    for i in arr:
        fuel += abs(m - i)
    
    print(fuel)
    
    return fuel

getMinFuel(readTxt("inputWhale.txt"))

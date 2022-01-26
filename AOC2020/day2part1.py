
import copy

def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for line in f:
        
        line2 = copy.copy(line)
        line2 = line2.replace("-", " ")
        line2 = line2.replace(":", "")
        arr.append(line2)
        
    return arr



def checkupPass(minEl, maxEl, el, password):
    countChar = 0
    numEl = len(password)
    
    for i in range(numEl):
        if password[i] == el:
            countChar += 1
    
    if countChar >= int(minEl) and countChar <= int(maxEl):
        return True
    
    return False

def countValidPass(arr):
    numEl = len(arr)
    numValPass = 0
    
    for i in range(numEl):
        minEl, maxEl, el, password = arr[i].strip().split(" ")
        if checkupPass(minEl, maxEl, el, password):
            numValPass += 1

    return numValPass    

print(countValidPass(readTxt("input.txt")))
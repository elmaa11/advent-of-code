
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



def checkupPass(firstPosition, secondPosition, el, password):    
    return (password[int(firstPosition) - 1] == el) ^ (password[int(secondPosition) -1] == el)

def countValidPass(arr):
    numEl = len(arr)
    numValPass = 0
    
    for i in range(numEl):
        firstPosition, secondPosition, el, password = arr[i].strip().split(" ")
        if checkupPass(firstPosition, secondPosition, el, password):
            numValPass += 1

    return numValPass    

print(countValidPass(readTxt("input.txt")))
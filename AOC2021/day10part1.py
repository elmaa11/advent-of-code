def readTxt (fileName):
    f = open(fileName, "r")
    arr = []
    
    for line in f:
        temp = []
        line = line.strip()
        for i in line:
            temp.append(i)
        
        arr.append(temp)
    return arr

def getFault(argument):
    switcher = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    
    return switcher.get(argument, 0)


def getSyntaxScore(arr):
    score = 0
    numRows = len(arr)
    
    for i in range(numRows):
        numCols = len(arr[i])
        stack = []
        for j in range(numCols):
            temp = arr[i][j]
            
            if stack:
                last = stack[-1]
                if last == '(' and temp == ')' or last == '[' and temp == ']' or last == '{' and temp == '}' or last == '<' and temp == '>':
                    stack.pop()
                else:
                    score_temp = getFault(temp)
                    stack.append(temp)
                    if score_temp:
                        score += score_temp
                        break
                
            else:
                stack.append(temp)
                
    
    
    return score

print(getSyntaxScore(readTxt("inputSyntax2.txt")))
import copy

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

def getPoint(argument):
    switcher = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    return switcher.get(argument, 0)

def getOpposite(argument):
    switcher = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    return switcher.get(argument, 0)


def getUnclosedLines(arr):
    score = 0
    numRows = len(arr)
    
    unclosedLines = []
    
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
            if j == numCols - 1:
                unclosedLines.append(stack)
    
    print(len(unclosedLines))
    return unclosedLines

def cleanLine(line):
    numEl = len(line)
    line2 = copy.copy(line)
    i = numEl - 1
    
    last = line2[i]
    preLast = line2[i - 1]
    
    while i > 0:
        last = line2[i]
        preLast = line2[i - 1]
        
        while (last == ')' and preLast == '(') or (last == ']' and preLast == '[') or (last == '}' and preLast == '{') or (last == '>' and preLast == '<'):
            line2 = line2[:i] + line2[i + 1:]
            line2 = line2[:i - 1] + line2[i:]
            
            i -= 1
            if i == len(line2):
                i -= 1
            if i <= 0:
                break
            last = line2[i]
            preLast = line2[i - 1]
        
        i -= 1
    
    
    return line2

def addClosures(line):
    closures = []
    for i in line:
        closures.append(getOpposite(i))
    closures.reverse()
    
    return closures

def getScore(line):
    score = 0
    numEl = len(line)
    
    for i in range(numEl):
        score *= 5
        score += getPoint(line[i])
    
    return score

def getTotalScore(lines):
    scores = []
    numEl = len(lines)
    
    for i in range(numEl):
        scores.append(getScore(lines[i]))

    scores.sort()    
    print(scores[int(numEl / 2) ])
    return scores


def fixUnclosedLines(arr):
    addedLines = []
    numRows = len(arr)
    
    for i in range(numRows):
        numCols = len(arr[i])
        addition = []
        line = arr[i]
        
        line = cleanLine(line)
        
                       
         
        addedLines.append(addition)
                
        
    
    
    return addedLines

def total():
    unclosedLines = getUnclosedLines(readTxt("inputSyntax2.txt"))
    numEl = len(unclosedLines)
    closures = []
    
    for i in range(numEl):
        closures.append(addClosures(cleanLine(unclosedLines[i])))
        
    
    return getTotalScore(closures)

total()


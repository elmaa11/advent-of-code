
def readTxt (fileName):  ##read data
    f = open(fileName, "r")
    arr = []
    
    for line in f:
        line = line.strip()
        a = line.split(' -> ')
        arr.append(a)
        
        
    f.close()
    return arr[0], arr[2:]

def getRule(argument):
    switcher = {
        'CH': 'B',
        'HH': 'N',
        'CB': 'H',
        'NH': 'C',
        'HB': 'C',
        'HC': 'B',
        'HN': 'C',
        'NN': 'C',
        'BH': 'H',
        'NC': 'B',
        'NB': 'B',
        'BN': 'B',
        'BB': 'N',
        'BC': 'B',
        'CC': 'N',
        'CN': 'C',
    }
    
    return switcher.get(argument, '0')

def Convert(lst):
    res_dct = {lst[i][0]: lst[i][1] for i in range(len(lst))}
    return res_dct


def growPolymer(babyPolymer, rules, n):
    new_rules = Convert(rules)
    
    
    for i in range(n):
        numEl = len(babyPolymer)
        k = 0
        while k < numEl - 1:
            babyPolymer = babyPolymer[:k + 1] + new_rules.get(babyPolymer[k:k + 2]) + babyPolymer[k + 1:]
            k += 2
            numEl = len(babyPolymer)
            
    
    occurings = {}
    numEl = len(babyPolymer)
    for i in range(numEl):
        if  babyPolymer[i] not in occurings:
            occurings[babyPolymer[i]] = 1
        else:
            occurings[babyPolymer[i]] += 1
    
    values = occurings.items()
    print(values)
    
    return
    
a,b = readTxt("inputPolymerization.txt")
growPolymer(a[0], b, 10)

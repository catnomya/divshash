import math

string = 'HelLo123'
hashMap = [
    [[' ','$'], ['%','%.']],
    [['a', 'b'], ['l', 'L']],
    [['c', 'd'], ['x', 'X']],
    [['e', 'f'], ['j', 'J']],
    [['g', 'h'], ['y', 'Y']],
    [['i', 'j'], ['a', 'A']],
    [['k', 'l'], ['o', 'O']],
    [['m', 'n'], ['u', 'U']],
    [['o', 'p'], ['q', 'Q']],
    [['r', 's'], ['s', 'S']],
    [['t', 'u'], ['t', 'T']],
    [['v', 'w'], ['g', 'G']],
    [['x', 'y'], ['d', 'D']],
    [['z', 'z'], ['z', 'Z']],

    [['A', 'B'], ['l.', 'L.']],
    [['C', 'D'], ['x.', 'X.']],
    [['E', 'F'], ['j.', 'J.']],
    [['G', 'H'], ['y.', 'Y.']],
    [['I', 'J'], ['a.', 'A.']],
    [['K', 'L'], ['o.', 'O.']],
    [['M', 'N'], ['u.', 'U.']],
    [['O', 'T'], ['q.', 'Q.']],
    [['R', 'S'], ['s.', 'S.']],
    [['T', 'U'], ['t.', 'T.']],
    [['V', 'W'], ['g.', 'G.']],
    [['X', 'Y'], ['d.', 'D.']],
    [['Z', 'Z'], ['z.', 'Z.']],
    [['P', 'Q'], ['6' , '4' ]],


    [['1', '2'], ['f', 'F']],
    [['3', '4'], ['m.','M']],
    [['5', '6'], ['n', 'N']],
    [['7', '8'], ['v', 'V']],
    [['9', '0'], ['1', '0']],
]

# IDENTITY HASH START ############################################################################

def HashString(string):
    if len(string)<8:
        while(len(string)<8):
            string+='.'
    hash=[] # IDENTITY HASH INIT
    vowelCounter = 0 # TO GET THE 2ND DIGIT OF IDENTITY HASH
    numberCounter=0
    capitalCounter=0
    normalCounter=0
    symbolCounter = 0
    symbols=[]
    vowels=[]
    for i in range(len(string)):
        hash.append(0) # TO FILL THE IDENTITY HASH

        if string[i:i+1].lower() in ['a','e','i','o','u']:
            if string[i:i+1] in ['A','B','C','D','E','F','G','H','I','J','K',
                            'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                capitalCounter+=1
            vowelCounter+=1 # TO GET THE NUMBER OF VOWELS IN IDENTITY HASH
            normalCounter+=1


        elif string[i:i+1].lower() in ['1','2','3','4','5','6','7','8','9','0']:
            numberCounter+=1


        elif string[i:i+1] in ['A','B','C','D','E','F','G','H','I','J','K',
                            'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
            capitalCounter+=1
            normalCounter+=1


        elif string[i:i+1] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                            'p','q','r','s','t','u','v','w','x','y','z']:
            normalCounter+=1


        else:
            symbolCounter+=1
            symbols.append(string[i:i+1])

    hash[0]=str(math.floor(len(string)/2)) # GET THE HASH SIZE
    hash[len(hash)-1]=str(math.ceil(len(string)/2)) # GET THE HASH SIZE
    hash[1]=str(vowelCounter) # GET THE 2ND DIGIT OF IDENTITY HASH
    hash[2]=str(numberCounter)
    hash[3]=str(capitalCounter)
    hash[4]=str(normalCounter)
    hash[5]=str(symbolCounter)

    # CLEANING THE HASH 
    #REMOVING ALL 0'S FROM THE LIST
    hashcopy = hash.copy()  # Make a copy of the hash list
    for i in range(len(hashcopy) - 1, -1, -1):
        if hashcopy[i] == 0:
            del hashcopy[i]  # Delete elements from the copy
    hash = hashcopy.copy()

    finalHash = ''.join(hash)
    loopBinary = []
    lengthOfEachLoopBinary = []

    for i in range(len(finalHash)):
        loopBinary.append(bin(int(finalHash[i:i+1]))[2:])
        lengthOfEachLoopBinary.append(len(bin(int(finalHash[i:i+1]))[2:]))

    hashSeq2 = '' # TO GET THE 2ND SEQUENCE OF THE HASH
    for i in range(len(lengthOfEachLoopBinary)):
        hashSeq2+=str(lengthOfEachLoopBinary[i])
    hashSeq2=bin(int(hashSeq2))[2:]

    loopBinary=f"{''.join(loopBinary)}.{hashSeq2}"

    hash = loopBinary
    hash+='_'

    hashSeq3 = []
    for i in range(len(string)):
        for x in range(len(hashMap)):
            for y in range(2):
                if string[i:i+1]==hashMap[x][0][y]:
                    hashSeq3.append(hashMap[x][1][y])


    hash+=''.join(hashSeq3)
    return hash
####################################################################################################




########################       DEHASHING  ##########################################################
def DehashString(hash):
    componentInitial = hash.split('_')
    component=componentInitial[0].split('.')
    component.append(componentInitial[1])


    def dec(binary_str):
        decimal = 0
        power = len(binary_str) - 1 
        for digit in binary_str:
            if digit == '1':
                decimal += 2 ** power
            power -= 1
        return decimal


    component0Seperations = []
    for i in range(len(str(dec(component[1])))):
        component0Seperations.append(str(dec(component[1]))[i:i+1])

    componentXSeperations = []
    for i in range(len(component0Seperations)):
        componentXSeperations.append(int(component0Seperations[i]))

    breaker = component[0]
    split_lengths = componentXSeperations

    componentX = []

    start_index = 0
    for length in split_lengths:
        substring = breaker[start_index:start_index + length]
        componentX.append(substring)
        start_index += length


    ##### TILL HERE, ALL THIS DOES IS SEPERATES THE VALUES OF COMPONENTX ACCRODING TO COMPONENT Y
    ##### NOW, WE CONVERT THE BINARY STRING TO DECIMAL

    finalComponentXList = []
    for i in range(len(componentX)):
        finalComponentXList.append(dec(componentX[i])) 

    # NOW, WE TURN THEM INTO A READABLE FORMAT

    componentX=''
    for i in range(len(finalComponentXList)):
        componentX+=str(finalComponentXList[i])

    root = component[2]
    rootSeperated = []
    for i in range(len(root)):
        if root[i:i+1]=='.':
            rootSeperated.append(root[i-1:i+1])
        elif root[i:i+1].endswith('.')==False and root[i+1:i+2]!='.':
            rootSeperated.append(root[i:i+1])

    opt = ''


    for i in range(len(rootSeperated)):
        for x in range(len(hashMap)):
            for y in range(2):
                if rootSeperated[i]==hashMap[x][1][y]:
                    opt+=hashMap[x][0][y]
                    # print('Found',hashMap[x][0][y])
    return opt


def HashWithFile(directory):
    file = open(directory, 'r')
    lines = file.readlines()
    hashed = []
    for i in range(len(lines)):
        hashed.append(HashString(lines[i]))
        
    return '\n'.join(hashed)

def WriteHashToFile(message,directory):
    file=open(directory,'w')
    file.write(HashString(message))
    file.close()

def DehashWithFile(directory):
    file=open(directory,'r')
    hashes = file.readlines()
    dehashed = []
    for i in range(len(hashes)):
        dehashed.append(DehashString(hashes[i]))
    
    return '\n'.join(dehashed)

class ComponentX:
    def __init__(self, string, mode='d'):
        capitalCount = 0
        vowelCount = 0
        numberCount = 0
        normalCount = 0
        symbolCount = 0
        returnString = []
        while len(returnString)<7:
            returnString.append(0)
        returnString[0]=str(math.floor(len(string)/2))
        returnString[len(returnString)-1]=str(math.ceil(len(string)/2))
        for i in range(len(string)):
            if string[i:i+1] in ['a','e','i','o','u']: # VOWEL COUNTER
                vowelCount+=1
            elif string[i:i+1] in ['1','2','3','4','5','6','7','8','9','0']: # Number counter
                numberCount+=1
            elif string[i:i+1] in ['A','B','C','D','E','F','G','H','I','J','K',
                            'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
                capitalCount+=1
                normalCount+=1
            elif string[i:i+1] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o',
                            'p','q','r','s','t','u','v','w','x','y','z']:
                normalCount+=1
            else:
                symbolCount+=1
        returnString[1]=str(vowelCount)
        returnString[2]=str(numberCount)
        returnString[3]=str(capitalCount)
        returnString[4]=str(normalCount)
        returnString[5]=str(symbolCount)
        
        returnStringCopy = returnString.copy()
        for i in range(len(returnStringCopy)):
            if returnStringCopy[i]==0:
                returnString.pop(i)
        self.hashKey = ''.join(returnString)
        self.hashBin = str(bin(int(self.hashKey)))[2:]

class ComponentZ:
    def __init__(self, stri):
        root = stri.split('_')[1]
        self.element = root
        self.string = stri
        rootSeperated = []
        outputList = []
        for i in range(len(root)):
            if root[i:i+1]=='.':
                rootSeperated.append(root[i-1:i+1])
            elif root[i:i+1].endswith('.')==False and root[i+1:i+2]!='.':
                rootSeperated.append(root[i:i+1])
        for i in range(len(rootSeperated)):
            for x in range(len(hashMap)):
                for y in range(2):
                    if rootSeperated[i]==hashMap[x][1][y]:
                        outputList.append(hashMap[x][0][y])
        self.dehashed = ''.join(outputList)
        

####################################################################################################

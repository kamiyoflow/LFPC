import re
initialStates = []
terminalStates = []
edges = []
states = []
alphabets = []
Input = open("nfa.txt")
lines = Input.readlines()

Input.close()

i = 0
while i < len(lines):
    txt = lines[i]
    txt = re.sub("\n", "", txt)
    txt = re.sub(" ", "", txt)
    lines[i] = txt
    i = i+1
initialStates = lines[0].split(",")
terminalStates = lines[1].split(",")



i = 2
j = 0
while i < len(lines):
    edge = lines[i].split(",")
    edges.append(edge)
    i = i + 1
    j = j + 1



i = 0
while i < len(edges):
    if not(edges[i][0] in states):
        states.append(edges[i][0])
    if not(edges[i][1] in states):
        states.append(edges[i][1])
    if not(edges[i][2] in alphabets):
        alphabets.append(edges[i][2])
    i = i + 1
i = 0

def printAutomata():

    i = 0
    print("states: ")
    while(i < len(states)):
        if(states[i] in initialStates) and (states[i] in terminalStates):
            print(">",states[i],"<")
        if(states[i] in initialStates) and not(states[i] in terminalStates):
            print(">",states[i])
        if not(states[i] in initialStates) and (states[i] in terminalStates):
            print(states[i],"<")
        if not(states[i] in initialStates) and not(states[i] in terminalStates):
            print(states[i])
        i = i + 1

    print("edges: ")
    i = 0
    while i < len(edges):
        print(edges[i][0], ":",edges[i][2], "-> ", edges[i][1])
        i = i + 1

    print("Alphabets: ")
    i = 0
    while i < len(alphabets):
        print(alphabets[i])
        i = i + 1

                

getheredStates = []
newEdges = []


def getheringStates(s, L):
    L.append(s)
    i = 0
    while i < len(edges):
        if(edges[i][0] == s) and (edges[i][2] == "$"):
            if not( edges[i][1] in L):
                getheringStates(edges[i][1], L)
        i = i + 1
    return L
    
i = 0
while i< len(states):

    l = getheringStates(states[i], [])
    getheredStates.append(l)
    i = i + 1




newInitialState = []
i = 0
while i < len(states):
    if(states[i] in initialStates):
        for s in getheredStates[i]:
            if not(s in newInitialState):
                newInitialState.append(s)
    i = i + 1


def getGetherdStateFromFirstState(state):
    for s in getheredStates:
        if s[0] == state:
            returned = s
    return returned
            
def conc(l1,l2):
    for item in l2:
        if not(item in l1):
            l1.append(item)
    return l1

def match(l1, l2):
        b = True
        if not(len(l1) == len(l2)):
                b = False
        else:
                for item in l1:
                        if not(item in l2):
                                b = False
                for item in l2:
                        if not(item in l1):
                                b = False
        return b
def exist(L, i):
        a = newEdges[i][0]
        b = match(L, a)
        if(b == True):
            return True
        else:
                j = i + 1
                if j < len(newEdges):
                        return exist(L, j)
                else:
                        return False
                        

    

def createNewAdge(alpha, gState):
 
    
    L = []
    for s1 in gState:
        i = 0
        while i < len(edges):
            if (s1 == edges[i][0] and edges[i][2] == alpha):
        
                if not(edges[i][1] in L):
                    Gstate = getGetherdStateFromFirstState(edges[i][1])
                    L = conc(L, Gstate)
            i = i + 1
    if L == []: return
    ne = [gState , L, alpha]
    newEdges.append(ne)

    isAlreadySource = exist(L, 0)
    if isAlreadySource == False:
        for A in alphabets:
            if not(A == "$"): createNewAdge(A, L)

for L in alphabets:
    if not(L == "$"): createNewAdge(L, newInitialState)

def alreadyInThisList(L, item):
    B = False
    for I in L:
        if(match(I, item) == True):
            B = True
    return B
newStates = []
Help = []
for edge1 in newEdges:
    Help.append(edge1[0])
    Help.append(edge1[1])


for n2 in Help:
    if(alreadyInThisList(newStates, n2) == False):
        newStates.append(n2)
        

newInitialStates = []
for item1 in newStates:
    for item2 in initialStates:
        if item2 in item1 and not(item1 in newInitialStates):
            newInitialStates.append(item1)
newTerminalStates = []
for item1 in newStates:
    for item2 in terminalStates:
        if item2 in item1 and not(item1 in newTerminalStates):
            newTerminalStates.append(item1)



setToChar = []
i = 1
for item in newStates:
    L = [item, i]
    setToChar.append(L)
    i = i+1
def summerizedStateName(L):
    for item in setToChar:
        if match(item[0], L) == True:

            return str(item[1]-1)





f = open("dfa.txt", "w")

f.write("new states: ")
for item in setToChar:
    index = item[1]
    f.write("q")
    f.write(str(index-1))
    f.write(" ")

f.write("\ninitial states: ")
f.write("q1")
f.write(" ")

f.write("\nterminal states: ")
for item in setToChar:
    if(item[0] in newTerminalStates):
        index = item[1]
        f.write("q")
        f.write(str(index-1))
        f.write(" ")
f.write("\nnew edges: \n")
for item in newEdges:
        f.write("\n")
        From = str(summerizedStateName(item[0]))
        f.write("q"+From)
        f.write(" , ")
        to = str(summerizedStateName(item[1]))
        f.write("q"+to)
        f.write(" , "+str(item[2]))
f.close()

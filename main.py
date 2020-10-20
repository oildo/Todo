from Category import *

def readTdl(directory):

    # count the number of lines
    nbrLines = 0
    with open(directory, 'r') as f:
        for line in f:
            nbrLines += 1

    
    tdl = open(directory, "r")
    out = []

    line = ""
    for i in range(nbrLines):
        # get the line
        line = tdl.readline()
        line = line.replace("\n", "")

        if line[0] == ".":
            line = line.replace(".", "")
            out.append(Category(line))
        else:
            out[-1].addTask(line)

    tdl.close()
    return out

def writeTdl(directory):
    #TODO
    pass

def printTasks(todoList, printCategories=True):
    print("")
    for categorie in todoList:
        if printCategories:
            print(f"\n{categorie.getName()}")
        for task in categorie.getTasks():
            print(f"-> {task}")
        if printCategories:
            print("----")

#-------------------------------------------

a = readTdl("DATA/main.tdl")

printTasks(a)
printTasks(a, False)
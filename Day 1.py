import os
path = "D:/Users/Jakob und Vio/Sciebo/Uni/Advent of Code"
os.chdir(path)

used = set()

def ptwo(changes, curr):
    for change in changes:
        curr += change
        argu = curr
        if curr not in used:
            used.add(curr)
        else:
            print(curr)
            return(curr)
    ptwo(changes, argu)
        
with open("input.txt", "r") as f:
    changes = []
    for line in f:
        changes.append(int(line))
    #print(list(line))
    #print(changes)
    print(sum(changes))
    ptwo(changes, 0)
    

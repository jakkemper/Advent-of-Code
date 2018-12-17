import os
#Insert the path to your Advent of Code folder here
#Put the input in the folder as input.txt
path = ""
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
    

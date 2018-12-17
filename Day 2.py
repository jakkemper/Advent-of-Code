import os
#Insert your path
path = ""
os.chdir(path)

with open("input2.txt", "r") as f:
    #Input öffnen und in Liste umwandeln
    changes = []
    for line in f:
        changes.append(str(line)[:-1])
    #print(len(changes))
    #Teil 1
    #Variablen vorbereiten
    #test = changes[0]
    threecount = 0
    twocount = 0
    for word in changes:
        if len(set(changes)) == len(changes):
            #Zuerst Check, ob überhaupt doppelte Buchstaben
            #print("####################STOP###############")
            #print(word)
            occ = dict()
            for letter in word:
                #Iterieren über jeden Buchstaben im Wort
                #occ = dict()
                counter = 0
                for counting in range(len(word)):
                    #Nochmaliges Iterieren über jeden Buchstaben
                    #Wenn Buchstabe = dem gesuchten Buchstaben: Zähler erhöhen
                    if word[counting] == letter:
                        counter += 1
                #Schreiben des Zählergebnisses in ein dictionary
                occ[letter] = counter
            #Errechnen der gezählten dreifachen und doppelten
            if 3 in occ.values():
                threecount += 1
            if 2 in occ.values():
                twocount += 1
    #multiplizieren
    print(threecount*twocount)
    #Teil 2
    snippets = []
    occ = dict()
    for word in changes:
        for index in range(len(word)):
            #Für jeden Buchstaben jedes Wortes: Erzeugen eines Snippets aus diesem Wort
            #mit einem Leerzeichen statt des Buchstaben
            firstlist = word[:index]
            secondlist = word[index+1:]
            snippet = firstlist+" "+secondlist
            #Hinzufügen der snippets zu einer Liste
            snippets.append(snippet)
    for snippet in snippets:
        counter = 0
        #Zählen, wie häufig ein Snippet in der Liste vorkommt
        for x in range(len(snippets)):
            if snippets[x] == snippet:
                counter +=1
        #Füllen eines Dictionaries mit dem Zählwert für alle Snippets
        occ[snippet] = counter
    #Finden desjenigen Snippets, das mehr als einmal gezählt wurde und Ausgabe dieses
    for key, value in occ.items():
        if value > 1:
            print(key.replace(" ", ""))
            

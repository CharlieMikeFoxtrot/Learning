
tableData = [['apples', 'oranges', 'cherries', 'banana'],
 ['Alice', 'Bob', 'Carol', 'David'],
 ['dogs', 'cats', 'moose', 'goose']]
#Starting table daat

def printTable(table): #define function printTable
    colWidth = [0] *len(tableData) #initialize columWidth with one 0 for each list in TableData
    for w in range(len(table)): #for each list
        for x in range(len(table[w])): #for each string in list
            if len(table[w][x])> colWidth[w]: #if string length is larger than colum width
                colWidth[w] = len(table[w][x]) #set new colum width to string length
            
    for i in range(len(table[0])): #For each string in the list 0 (ASSUME ALL LISTS ARE SAME LENGTH)
        for n in range(len(table)): #for each list in table
            print(table[n][i].rjust(colWidth[n]), end = ' ') #table[list's in dict] [table list len] print right justified
            #go through N which is eash list, printing the [i] index of each list
        print('')# once row is finished printing enter a new line
            
            
printTable(tableData) #Test printTable function
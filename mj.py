def print_honeycomb(rows,cols):
    print(" ___ "+"    ___ " * (cols-4))
    for r in range(rows*2):
        if r % 2 ==0:
            print("/   \\___" +"/   \\___"  * (cols-4))
        else:
            print("\\___/"+"   \\___/" * (cols-4))

rows = int(input("ENTER THE NUMBER OF ROWS"))
cols = int(input("ENTER THE NUMBER OF cols"))

print_honeycomb(rows,cols)



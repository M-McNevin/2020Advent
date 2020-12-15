with open('AdventDay3.txt') as x:
    mappa= x.read().splitlines()

print(len(mappa))
xpos=0
ypos=0
counter=0

for item in mappa:
    print(xpos,ypos,item[xpos], counter)
    if (mappa[ypos][xpos] == '#'):
        counter+=1
        xpos+=1
        ypos+=2
        if xpos >= 31:
            xpos = 0
        
        
    else:
        xpos+=1
        ypos+=2
        if xpos >=31:
            xpos= 0
        if ypos >= 322:
            print(counter)
            break


    
print(counter)

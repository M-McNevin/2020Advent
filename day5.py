import math
with open("AdventDay5.txt") as f:
    data=f.readlines()

upper_limit=127
lower_limit=0
print(upper_limit - ((upper_limit-lower_limit)/2))

new_list=[]

# data=['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']

for line in data:
    lower_limit=0
    upper_limit=127
    
    #lower
    lower=0
    #upper
    upper=7

    for letter in line:
        if letter == "F":
            upper_limit= math.floor(upper_limit - (upper_limit-lower_limit)/2)
            lower_limit=lower_limit
            # print(letter + ':' + str(lower_limit) + ':' + str(upper_limit))    
        elif letter == 'B':
            lower_limit=math.ceil(((upper_limit-lower_limit)/2) + lower_limit)
            upper_limit=upper_limit
            # print(letter + ':' + str(lower_limit) + ':' + str(upper_limit))
        
        elif letter == 'L':
            upper= math.floor(upper - (upper-lower)/2)
            lower=lower
            # print(letter + ':' + str(lower) + ':' + str(upper))  
        elif letter == 'R':
            lower=math.ceil(((upper-lower)/2) + lower)
            upper=upper
            # print(letter + ':' + str(lower) + ':' + str(upper))
        else:
            continue


    seat=((upper_limit*8)+ (upper))
    new_list.append(seat)
    # print(line + ':' + str(lower_limit) + ':' + str(upper_limit) + ':' + str(upper) + ':' + str(lower))

new_list=sorted(new_list)
print(new_list)

for i in range(len(new_list)-1):
    if new_list[i] + 1 != new_list[i+1]:
        print(new_list[i]+1)
        
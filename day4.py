with open("AdventDay4.txt") as x:
    data=x.read().split('\n\n')




new_list=[]

for line in data:
    line=line.split()
    new_list.append(line)

counter=0

for line in new_list:
    pass_check=0
    for item in line: 
        
        if 'byr' in item and len(item) > 4:
            print(item)
            pass_check+=1
        elif 'iyr' in item and len(item) > 4:
            print(item)
            pass_check+=1
        elif 'eyr' in item and len(item) > 4:
            print(item)
            pass_check+=1
        elif 'hgt' in item and len(item) > 4:
            print(item)
            pass_check+=1
        elif 'ecl' in item and len(item) > 4:
            print(item)
            pass_check+=1          
        elif 'pid' in item and len(item) > 4:
            print(item)
            pass_check+=1
        elif 'hcl' in item and len(item) > 4:
            print(item)
            pass_check+=1
        else:
            print(item)
    print(line, pass_check)
    if pass_check >= 7:
        counter+=1
    print(counter)
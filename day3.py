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

count_2=0
final_pass=[]

for line in first_pass:
    pass_check=0
    for item in line:
        check=item[4:]
        if 'byr' in item:
            if int(check) >= 1920 and int(check) <=2002:
                pass_check+=1
            else:
                print("failed " + item)
        elif 'iyr' in item:
            if int(check) >= 2010 and int(check) <=2020:
                pass_check+=1
            else:
                print("failed " + item)
        elif 'eyr' in item:
            if int(check) >= 2020 and int(check) <=2030:
                pass_check+=1
            else:
                print("failed " + item)
        elif 'hcl' in item:
            if check[0] == '#' and len(check[1:])==6:
                hcl_ok=[]
                for i in check[1:]:
                    if i in ('abcdefghijklmnopqrstuvwxyz0123456789'):
                        hcl_ok.append(i)
                if len(hcl_ok)==6:
                    pass_check+=1
            else:
                print("failed " + item)
        elif 'ecl' in item:
            if check == 'amb' or check == 'blu' or check == 'brn' or check == 'gry'or check == 'grn' or check == 'hzl' or check == 'oth':
                pass_check+=1   
            else:
                print("failed " + item)       
        elif 'pid' in item:
            if len(check) == 9:
                pass_check+=1
            else:
                print("failed " + item)
        elif 'hgt' in item:
            if str(check[-2:])== 'in' and (int(check[0:-2]) >= 59 and int(check[0:-2]) <= 76):
                pass_check+=1
            elif str(check[-2:])== 'cm' and (int(check[0:-2]) >= 150 and int(check[0:-2]) <= 193):
                pass_check+=1
            else:
                print("failed " + item)
        else:
            print("failed " + item)
    print(line, pass_check)
    if pass_check >= 7:
        count_2 +=1
        final_pass.append(line)
    print(count_2)

with open("AdventDay2.txt") as a:
    txt_file = a.read().splitlines()
    
    txt_list=[]

for line in txt_file:

    txt_list.append(line.replace(':',"").split(" "))

print(len(txt_list))

ok_passwords=[]

for i in range(len(txt_list)):
    min_max = txt_list[i][0].split('-')
    if (txt_list[i][2].count(txt_list[i][1]) >=  int(min_max[0])) and (txt_list[i][2].count(txt_list[i][1]) <=  int(min_max[1])):
        ok_passwords.append(txt_list[i][2])

print(len(ok_passwords))

new_ok_passwords = []

for i in range(len(txt_list)):

    min_max = txt_list[i][0].split('-')


    count=0
    if txt_list[i][2][int(min_max[0])-1] == txt_list[i][1]:
        count+=1    
    if txt_list[i][2][int(min_max[1])-1] == txt_list[i][1]:
        count+=1 
    if count > 0 and count < 2:
        new_ok_passwords.append(txt_list[i][2])

        
print(len(new_ok_passwords))
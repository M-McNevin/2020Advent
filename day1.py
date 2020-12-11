with open("data/num.txt") as f:
    txt_file = f.read().splitlines()


new_list = []

for i in txt_file:
    new_list.append(int(i))


    for num in new_list:
        diff = 2020 - int(num)
        new_list.append(diff)


    for i in range(len(new_list)):
        if str(new_list[i]) in new_list:
            print(new_list[i])



# empt_list=[]

# for i in range(len(new_list)):
#     for j in range(len(new_list)):
#         for k in range(len(new_list)):
#             if new_list[i] + new_list[j] + new_list[k] == 2020:
#                 print(new_list[i],new_list[j],new_list[k])
#                 break
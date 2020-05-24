string = input()
con = string.upper()
d = {}
count = 0
index = 0
value = 0

for i in range(len(con)):
    if (con[i] in d) == False:
        d[con[i]] = 1
        #print("this loop is if {}".format(con[i]))
    else:
        d[con[i]] += 1
        #print("this loop is else {}".format(con[i]))

#for k,v in enumerate(d):
for i in range(len(list(d.values()))):
    if value < list(d.values())[i]:
        value = list(d.values())[i]
    else:
        pass

for k,v in enumerate(d):
    if value == list(d.items())[k][1]:
        count += 1
        index = k
    else:
        pass

if count > 1:
    print('?')
else:
     print(list(d.items())[index][0])
    



#print(d)
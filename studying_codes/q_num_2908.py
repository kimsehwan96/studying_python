#for general situation.. 
a ,b = map(int,(input().split(' ')))
tmp_a = []
tmp_b = []
c = list(str(a))
d = list(str(b))
for x in range(3):
    tmp_a.append(c.pop())
    tmp_b.append(d.pop())



def returning_num(length,list_tmp):
    num = 0
    for x in range(length):
        od = pow(10,length -(1+x))
        num += int(list_tmp[x])*od

    return num

r_a=returning_num(len(tmp_a),tmp_a)
r_b=returning_num(len(tmp_b),tmp_b)

if r_a > r_b:
    print(r_a)
else:
    print(r_b)


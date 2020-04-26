

def min_max(d:list):
    d.sort()
    print(d[0],d[-1],sep=' , ')

l = [3,1,5,4]

print("list is {}".format(l))
print("this is min & max {}".format(min_max(l)))
print("after list {}".format(l)) # 원본 리스트가 변형되었다. 이럴 떄 필요한게 바로 리스트 복사.

def min_max_2(d:list):
    d = list(d) # d에 원본 리스트를 복사한다. (d라는 인자로 리스트를 받은것이지, 원본 객체를 변형하는 것은 아님.)
    d.sort()
    print(d[0],d[-1],sep=' , ')
    

c = [3,1,5,4]
print("list c is {}".format(c))
print("this is min & max {}".format(min_max_2(c)))
print("after list {}".format(c)) # 복사한 리스트 객체를 sorting했기 때문에 원본 리스트는 sort 되지 않는다. 리스트 복사 technic.

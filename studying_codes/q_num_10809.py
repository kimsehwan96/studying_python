alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
         'o','p','q','r','s','t','u','v','w','x','y','z']

word = str(input())
list_find = []

for x in range(len(alpha)):
    if alpha[x] in word == False:
        list_find.append(-1)
    else:
        list_find.append(word.find(alpha[x]))




for x in range(len(alpha)):
    print(list_find[x], end=' ')

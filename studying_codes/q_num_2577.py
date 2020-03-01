A = int(input())
B = int(input())
C = int(input())
list_repeat=[]
list_repeat.clear()

product_sum = A*B*C
list_product = str(product_sum)

for x in range(10):
    b = list_product.count(str(x))
    print(b)








num = int(input())
sum = 1

def factorial(num):

    if num == 1:

        return

    global sum
    sum = sum * num
    num -= 1
    factorial(num)

if num == 0:
    sum = 1
    print(sum)

else:
    factorial(num)
    print(sum)

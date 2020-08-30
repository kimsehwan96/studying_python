if __name__ == "__main__":

    testArr1 = [1,2,3,4,5,6,7,8,9,10]
    testArr2 = [2,4,6,8,10,12,14,16,18,20]

    outArr1 = list(map(lambda x: 'OK' if x % 2 == 0 else x, testArr1))
    print('Lambda Example1 : ', outArr1)

    outArr2 = list(map(lambda x: 'First' if x == 1 else 'Second' if x == 2 else x * x, testArr1))
    print('Lambda Example2 : ', outArr2)

    outArr3 = list(map(lambda x, y: x + y, testArr1, testArr2))
    print('Lambda Example3 :', outArr3)
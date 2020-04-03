


class Account:
    num_account = 0

    def __init__(self, name):
        self.name = name
        Account.num_account += 1

    def __del__(self):
        Account.num_account -= 1


kim = Account('kim')
lee = Account('lee')

print(kim.name)


print(kim.num_account)
print(lee.num_account)

#하나의 인스턴스가 생길 때 마다 클래스 변수의 값을 증가시켰다.


class dog:
    
    # 내부에서 어떤 처리를 해야 할 변수들을 모두 self로 만들어야 하는데 코딩하면서 추가를 하는게 맞는듯
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
#self를 붙이는 이유는, self를 붙여야 내부 변수이고, self를 안붙이면 외부 변수라고 판단하는 듯?
    def barking(self):
        print('my name is {} and age is {}'.format(self.name,self.age))


        # 외부에서 인자를 받아서 내부 값을 변형 하는 경우가 많을 것...... (self,(notself)변수) 를 인자로 받자
    def age_change(self,change_age):
        self.age = change_age
        print('my age is changed{}'.format(self.age))



#객체 상속해보기


#생성자(__init__)에서 부여하는 클래스 생성시 필요한 인자들이 똑같다면 init 불필요
#부모 클래스의 메소드를 모두 상속하고, 자식 클래스에서는 메소드를 추가 가능 
class bigger_dog(dog):
    #초기 속성 똑같이 쓸 경우 init 불필요?

    def ident(self):
        print('I am a bigger dog name : {}, age : {}'.format(self.name,self.age))

    def run(self,speed):
        print('i am running in speed {}'.format(speed))







d = dog('hi',5)
print(d)

d.barking()

d.age_change(25)

bigdog = bigger_dog('mac',35)

bigdog.barking()
bigdog.ident()
bigdog.run(1245)

print('-------------------------------------')


class Pets:
    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs


class Dog:
    
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    def description(self):
        return self.name, self.age
    
    def speak(self, sound):
        return "%s sayas %s" % (self.name, sound)

    def eat(self):
        self.is_hungry = False


class RussellTerrier(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

class Bulldog(Dog):
    def run(self, speed):
        return "%s runs %s" % (self.name, speed)

my_dogs = [ 
    Bulldog('tom',6),
    RussellTerrier('fit',4),
    Dog('hi',2)
]


my_pets = Pets(my_dogs)


print(my_pets.dogs)


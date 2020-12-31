# 파이썬 함수 식 및 람다(lambda)


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)

print(val1, val2 ,val3)

def args_func(*args):
    print(args)

args_func('kim')
args_func('kim', 'park')


## kwargs

def kwargs_func(**kwargs):
    # print(kwargs)
    for k,v in kwargs.items():
        print(k,v)

kwargs_func(name1='kim', name2='park') # {'name1': 'kim', 'name2': 'park'} 


def example_mul(arg1, arg2, *args, **kwargs): # arg1, arg2는 무조건 입력을 받아야 하는 인자 뒤 *args, **kwargs는 가변인자
    print(arg1, arg2, args, kwargs)


example_mul(10, 20)
example_mul(10, 20, 200, 500, 'hello',  key1='hello', key2=5)

# 중첩 함수(클로저)
def nested_func(num):
    def func_in_func(num):
        print(num)
    print("in func")
    func_in_func(num * 1000)

nested_func(2)


# 예제 6
# 타입 명시 -> 강제는 없음
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return [y1, y2, y3]

print(func_mul3(5.0)) # 동작은 한다.
# 타입 강제하고 싶다면 인자의 타입을 체크한다.

# 이렇게 인자 타입을 강제하는 방법도 있다.
def func_mul4(x : int) -> list:
    if (type(x) != int):
        print("type error")
        return
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300

    return [y1, y2, y3]


func_mul4(5.0)


# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스 할당
# 람다 즉시 실행 (heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당

def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10
print(var_func) # <function mul_10 at 0x7ff960070b00> <- 함수가 사용되지 않았지만 함수 객체가 생성되었다.

print(var_func(10))

lambda_mul_10 = lambda x: x * 10 # x 이건 인자, 인풋 : x * 10 이건 리턴

print(lambda_mul_10(10))

print(lambda_mul_10) # 역시 할당은 되어있다. 가독성 측명에서 사용해야 할듯

def func_final(x, y, func): # x, y , 함수를 받겠다.
    print(x * y * func(10))

func_final(1, 10, lambda_mul_10)

print(func_final(10, 10, lambda x : x * 1000))
# 인자로 함수를 받을 경우에 간단한 함수라면 이렇게 람다식을 활용하는 것도 하나의 방법이 된다!

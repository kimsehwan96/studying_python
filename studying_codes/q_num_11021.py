test_case_num = int(input())


for x in range(test_case_num):
    a, b = map(int, input().split())
    c = a+b
    case_num = x+1
    print("Case #%d: %d" %(case_num,c))

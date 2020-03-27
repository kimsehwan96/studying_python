test_case = int(input())

for n in range(test_case):
    repeats, strings = map(str, input().split())


    for x in range(len(strings)):
        for re in range(int(repeats)):
            if re != int(repeats) -1:
                print((strings[x]), end ="")
            else:
                if x == len(strings) -1:
                    print("\n")
                else:
                    pass
                
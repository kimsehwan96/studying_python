def finding_direct(ary: list):
    as_ary = [ x+1 for x in range(8) ]
    ds_ary = list(as_ary)
    ds_ary.reverse()
    if ary == as_ary:
        print("ascending")
    elif ary == ds_ary:
        print("descending")
    else:
        print("mixed")

if __name__ == "__main__":
    ary = list(map(int, input().split(' ')))
    finding_direct(ary)
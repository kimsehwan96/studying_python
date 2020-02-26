hour, min = map(int,input().split())

if hour == 0:
    if min-45>0:
        print("%d %d" %(hour, min-45))
    elif min-45 == 0:
        print("0 0")
    else:
        print("23 %d" %(min+15))
else:
    if min - 45 > 0:
        print("%d %d" %(hour, min-45))
    elif min - 45 == 0:
        print("%d 0" %(hour))
    else:
        print("%d %d" %(hour-1, min+15))

zero_floor = [ x+1 for x in range(15) ]

def make_table():
    table = {}
    table[1] = zero_floor
    for floor in range(15):
        if floor == 0:
            table[floor] = zero_floor
        else:
            lower_floor = table.get(floor-1)
            current_floor = []
            stack = 0
            for value in lower_floor:
                stack += value
                current_floor.append(stack)
            table[floor] = current_floor
    return table

if __name__ == "__main__":
    table = make_table() #dict
    #print(table)
    testNum = int(input())
    for idx in range(testNum):
        result = None 
        k = int(input())
        n = int(input())
        result = table.get(k)[n-1]
        print(result)
        

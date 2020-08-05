def find_room(H, K, N):
    room_number = N // H 
    room_floor = N % H
    if room_floor == 0:
        room_floor = H

    if N % H == 0:
        room_number -= 1
    return '{}'.format(room_floor*100 + (room_number+1))

if __name__ == "__main__":
    testNum = int(input())
    result = []
    for i in range(testNum):
        H, K, W = map(int, input().split(' '))
        result.append(find_room(H,K,W))
    for i in range(testNum):
        print(result[i])
        

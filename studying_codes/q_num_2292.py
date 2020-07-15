#1 <- 1  
#[2 - 7](개수 6개 6 <- count *1 <- rng ) <- 2   
#[8 - 19](개수 12개 6*2) <- 3
#[20 - 37](개수 18개 6*3) <- 4개 지나야 함
#[38 - 61] (개수 24개 6*4) <- 5개

#num = int(input())


def cal_minum_root(n):
    a=1
    b=6
    c=1
    if n == 1:
        return 1
    else:
        while True:
            c += b #7, 19, 37, 61 .. 
            a += 1
            #print(c)
            if n <= c:
                return a
            else:
                b = 6*a    
if __name__ == "__main__":
    num = int(input())
    result = cal_minum_root(num)
    print(result)

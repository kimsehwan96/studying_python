def find_depth(n): #몇번째 대각선에 있는지 체크해야 함.
   line = 1 #줄수 n -> 몇번째인지.
   while n > line:
      n -= line # n = n - line
      line += 1 # line = line + 1

   return line, n
def print_answer(args): #line, n
   line, n = args
   if line % 2 == 0:
      a = n
      b = line - n + 1
   else:
      a = line -n + 1
      b = n
   print(a, '/', b, sep='')
#짝수번째 줋 -> 분자는 오름, 분모는 내림 홀수번째 줄 -> 분자는 내림, 분모는 오름
if __name__ == "__main__":
   num = int(input())

   if num == 1:
      print("1/1")
   else:
      print_answer(find_depth(num))

from array import array


def solution(N):

   first = 1
   second = 2

   answer = 0
   i = 2

   if N == 1 : 
      return first
   elif N == 2 :
      return second

   while(i<N):
      i += 1
      answer = first + second
      first = second
      second = answer

   print(answer)

solution(6)
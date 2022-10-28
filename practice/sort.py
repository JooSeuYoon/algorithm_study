import sys

def f1() :
   n = int(sys.stdin.readline())

   stud = []

   for i in range(n):
      line = sys.stdin.readline().split(" ")
      stud.append([line[0],int(line[1])])

   array = sorted(stud, key = lambda stud: stud[1], reverse=True)

   print(array)

def f2() :
   n, k = map(int, sys.stdin.readline().split(" "))
   arrA = list(map(int, sys.stdin.readline().split(" ")))
   arrB = list(map(int, sys.stdin.readline().split(" ")))

   arrA = sorted(arrA)
   arrB = sorted(arrB, reverse=True)

   for i in range(k):
      if arrB[i] > arrA[i]:
         arrA[i] = arrB[i]
      
   print(sum(arrA))

f2()
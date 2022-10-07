import sys

num = int(input())
i = 0
while i<num:
   human = int(input())
   record = []
   result = 1

   for j in range(human):
      record.append(list(map(int, sys.stdin.readline().split(" "))))

   record.sort()

   high = record[0][1]

   for k in range(1, human):
      if (high > record[k][1]):
         result += 1
         high = record[k][1]

   print(result)

   i+=1
   

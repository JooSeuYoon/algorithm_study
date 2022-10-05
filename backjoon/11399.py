import sys

num = int(input())
arr = list(map(int, sys.stdin.readline().split(" ")))

arr.sort()
sum = 0
result = 0


for i in arr:
   sum += i
   result += sum

print(result)
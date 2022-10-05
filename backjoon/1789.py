from re import I


num = int(input())

sum = 0
i = 1

while (sum <= num):
   sum += i
   i += 1

if (sum != num):
   i -= 2
else:
   i -=1

print(i)
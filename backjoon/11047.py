import sys

N, K = map(int, sys.stdin.readline().split(" "))

coin = []

for i in range(N):
   
   coin.append(int(sys.stdin.readline()))

count = 0
j = 1
while K != 0:
   if(K / coin[N-j] > 0):
      count += int(K / coin[N-j])
      K -= (int(K / coin[N-j])) * coin[N-j]
   j += 1

print(count)
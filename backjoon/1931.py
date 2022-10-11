import sys

N = int(sys.stdin.readline())

meeting = []

for i in range(N):
   start, end = map(int, sys.stdin.readline().split(" "))

   meeting.append([start, end])

meeting.sort(key=lambda x:x[0])
meeting.sort(key=lambda x:x[1])

end = meeting[0][1]

count = 1

for j in range(1, N):
   if(meeting[j][0] >= end):
      count+=1 
      end = meeting[j][1]

print(count)
import sys

def check(brokenNums : list, channel : str):
   for one in list(channel):
      if one in brokenNums:
         return False
   return True

read = sys.stdin.readline

goChannel = read().rstrip()
brokenNum = int(read().rstrip())

if brokenNum != 0:
   broken = read().rstrip().split(" ")

#broken = list(map(int, broken))

makeChannel = 0
maxChannel = ""

for i in range(len(goChannel) + 1):
   maxChannel = maxChannel + "9"

min = int(goChannel)

if(goChannel == "100"):
   print(0)
elif(brokenNum==0):
   if(len(goChannel) < abs(100 - int(goChannel))):
      print(len(goChannel))
   else:
      print(100 - int(goChannel))
else:
   for i in range(0, int(maxChannel) + 1):
      if(check(broken, str(i))):
         if abs(int(goChannel) - i) < min:
            min = abs(int(goChannel) - i)
            makeChannel = i
   print(len(str(makeChannel)) + abs(int(goChannel) - makeChannel))
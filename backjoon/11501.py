import sys

def nextNum(brokenNum : list, nowIndex : int, goChannel : str, makeChannel : str):
   result = 0
   min = int(goChannel)
   zeros = ""
   for i in range(0, len(goChannel) - nowIndex):
      zeros = zeros + "0"

   for i in range(0, 10):
      if str(i) not in brokenNum:
         if min > abs(int(makeChannel + str(i) + zeros[0:len(zeros) - 1]) - int(goChannel)):
            result = i
            min = abs(int(makeChannel + str(i) + zeros[0:len(zeros) - 1]) - int(goChannel))

   return result



read = sys.stdin.readline

goChannel = read().rstrip()
brokenNum = int(read().rstrip())

if brokenNum != 0:
   broken = read().rstrip().split(" ")

#broken = list(map(int, broken))

makeChannel = ""
count = 0

if(goChannel == "100"):
   print(0)
   exit()
elif(brokenNum==0):
   if(len(goChannel) < abs(100 - int(goChannel))):
      print(len(goChannel))
   else:
      print(100 - int(goChannel))
   exit()
else:
   for i in range(len(goChannel)):
      # if goChannel[i] not in broken:
      #    makeChannel = makeChannel + goChannel[i]
      # else:
      makeChannel = makeChannel + str(nextNum(broken, i, goChannel, makeChannel))

   if(abs(int(goChannel) - 100) < len(makeChannel) + abs(int(makeChannel) - int(goChannel))):
      print(int(goChannel) - 100)
   else:
      print(len(makeChannel) + abs(int(makeChannel) - int(goChannel)))




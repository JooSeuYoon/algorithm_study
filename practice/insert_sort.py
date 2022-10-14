array = [1,3,5,4,7,5,2,8,6]

for i in range(len(array)):
   for j in range(i, 0, -1):
      if array[j] < array[j - 1]:
         array[j], array[j - 1] = array[j - 1], array[j]
      else:
         break
print(array)
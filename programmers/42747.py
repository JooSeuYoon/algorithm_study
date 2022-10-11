citations = [1, 4, 4, 5]

answer = 0
citations.sort()
    
for i in range(len(citations)):
   if((len(citations) - i) >= citations[i]):
      if(answer < citations[i]) : answer = citations[i] 
   else:
      if(len(citations) - i > answer):
         answer = len(citations) - i 


print(answer)
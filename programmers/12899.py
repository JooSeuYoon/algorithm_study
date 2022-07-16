#124 나라의 숫자

import math

def solution(n):
    answer = ''
    udt = ['4','1','2']
    
    while n > 0:
        answer = udt[n%3] + answer
        if n%3==0:
            n = math.floor(n/3) - 1
        else:
            n = math.floor(n/3)
    
    return answer
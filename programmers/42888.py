def solution(record):
    answer = []
    
    uid = {}
    
    for line in record:
        words = line.split(" ")
        
        if words[0] == "Enter":
            uid[words[1]] = words[2]
        elif words[0] == "Change":
            uid[words[1]] = words[2]
    
    for line in record:
        words = line.split(" ")
        
        if words[0] == "Enter":
            answer.append(uid[words[1]]+"님이 들어왔습니다.")
        elif words[0] == "Leave":
            answer.append(uid[words[1]] + "님이 나갔습니다.")
            
        
    
    return answer
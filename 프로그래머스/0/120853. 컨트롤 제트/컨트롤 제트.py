def solution(s):
    s = s.split(" ")
    print(s)
    answer=s
    for idx in range(len(s)):
        try: 
            if s[idx+1] == 'Z' :
                answer.remove(s[idx])
    
        except :
            for i in range(answer.count("Z")):
                answer.remove("Z")
            return sum([int(i) for i in answer])
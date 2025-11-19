def solution(n):
    answer = 0
    count = 0
    for i in range(1,n+1):
        for n in range(1,i+1):
            if i % n == 0:
                count+=1
        if count >= 3:
            answer += 1
        count = 0
    return answer
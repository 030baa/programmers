def solution(n):
    answer = []
    div = []
    count = 0
    for i in range(2, n+1):
        if n % i == 0:
            div.append(i)
    for i in div:
        for s in range(2, i+1):
            if i % s == 0:
                count += 1
        if count==1:
            answer.append(i)
        count = 0
                
                
    return answer
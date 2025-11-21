def solution(n):
    for i in range(1, 12):
        d = 1
        for s in range(1,i+1):
            d *= s
        if d > n:
            return i -1 
        
    #다른 풀이 생각해보기

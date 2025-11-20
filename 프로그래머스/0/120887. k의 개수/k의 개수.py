def solution(i, j, k):
    count, answer = 0, 0
    for i in range(i,j+1):
        count = 0
        count = str(i).count(str(k))
        answer += count
    return answer
def solution(order):
    answer = 0
    for i in '369':
        answer += str(order).count(i)
    return answer
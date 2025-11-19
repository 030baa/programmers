def solution(n):
    for i in range(1,601):
        if (i*6) % n == 0:
            return i
        
        
#while은 True일때 계속 돌아가는데, 0만 아니면 됨.
# 그렇다면, 0일 때 그만 돌아간다는 거고, 나머지가 0이면 그게 답이 되니까, 그때 반환하면 됨.
'''
while 6 * answer % n:
    answer += 1
    return answer
    '''
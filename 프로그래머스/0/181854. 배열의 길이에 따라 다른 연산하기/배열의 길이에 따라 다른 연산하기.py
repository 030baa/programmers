def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for idx, num in enumerate(arr):
            if idx % 2 == 1:
                answer.append(num+n)
            else:
                answer.append(num)
    else:
        for idx, num in enumerate(arr):
            if idx % 2 == 0:
                answer.append(num+n)
            else:
                answer.append(num)
    return answer
                
                
                
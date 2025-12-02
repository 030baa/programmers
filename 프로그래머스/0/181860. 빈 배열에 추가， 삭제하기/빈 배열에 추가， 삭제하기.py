def solution(arr, flag):
    answer = []
    for tf, num in zip(flag, arr):
        if tf == True:
            for i in range(num*2):
                answer.append(num)
        else:
            for i in range(num):
                answer.pop()
            
    return answer
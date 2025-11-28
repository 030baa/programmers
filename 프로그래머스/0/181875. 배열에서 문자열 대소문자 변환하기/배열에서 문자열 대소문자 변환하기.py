def solution(strArr):
    answer=[]
    for idx, string in enumerate(strArr):
        if idx % 2 == 0:
            answer.append(string.lower())
        else:
            answer.append(string.upper())
    return answer
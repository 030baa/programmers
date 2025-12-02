def solution(my_string, indices):
    answer = ''
    for idx, s in enumerate(my_string):
        if idx in indices:
            pass
        else:
            answer += s
    return answer
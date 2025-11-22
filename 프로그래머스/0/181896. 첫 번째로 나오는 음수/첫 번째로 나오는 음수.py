def solution(num_list):
    for i, d in enumerate(num_list):
        if d < 0:
            return i
    return -1
def solution(my_strings, parts):
    answer = ''
    for idx, string in enumerate(my_strings):
        index1 = parts[idx][0]
        index2 = parts[idx][1] + 1
        answer += string[index1:index2]
    return answer
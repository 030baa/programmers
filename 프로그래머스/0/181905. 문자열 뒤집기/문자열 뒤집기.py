def solution(my_string, s, e):
    dd = my_string[s:e+1][::-1]
    answer = my_string[:s] + dd + my_string[e+1:]
    return answer
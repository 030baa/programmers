def solution(my_string, m, c):
    string = []
    for i in range(len(my_string)//m):
        string.append(my_string[i*m:(i+1)*m:])
    return "".join([i[c-1] for i in string])
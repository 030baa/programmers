def solution(my_str, n):
    answer = []
    if len(my_str) % n == 0:
        d = len(my_str) // n
    else:
        d = len(my_str) // n + 1
        
    print(d)    
    for i in range(d):
        answer.append(my_str[n*i:n*(i+1)])
    return answer
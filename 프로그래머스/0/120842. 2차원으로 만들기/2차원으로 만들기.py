def solution(num_list, n):
    answer = []
    for i in range(1,len(num_list)//n+1):
        answer.append(num_list[n*(i-1):n*i])
    return answer
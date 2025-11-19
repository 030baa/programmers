def solution(rsp):
    dic = {'2':'0',"0":"5","5":"2"}
    return ''.join([dic[i] for i in rsp])

    
    
    
    '''
        answer = ''
    dic = {'2':'0',"0":"5","5":"2"}
    for i in rsp:
        for k,v in dic.items():
            if k == i:
                answer += v
    return answer

    '''
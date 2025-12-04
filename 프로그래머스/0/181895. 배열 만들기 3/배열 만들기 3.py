def solution(arr, intervals):
    answer = []
    for one, two in intervals:
        answer.extend(arr[one : two+1])
        
    return answer
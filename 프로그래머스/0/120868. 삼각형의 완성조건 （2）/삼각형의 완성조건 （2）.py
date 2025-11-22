def solution(sides):
    max_num = max(sides)
    min_num = min(sides)
    count = max_num - (max_num - min_num)
    count += (max_num+min_num-1) - max_num
    return count
def solution(before, after):
    for i in before:
        after = list(after)
        try:
            after.remove(i)
        except:
            return 0
        
    if len(after) > 0:
        return 0
    else:
        return 1

## 동일한 기준에서 보면 되지!
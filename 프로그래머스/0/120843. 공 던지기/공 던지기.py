def solution(numbers, k):
    if len(numbers) % 2 == 0:
        odd = numbers[::2]
        return odd[(k % len(odd)) -1]
    else:
        even = numbers[::2] + numbers[1::2]
        return even[(k%len(numbers)-1)]
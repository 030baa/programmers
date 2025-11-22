def solution(numbers):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, e in enumerate(eng):
        numbers = numbers.replace(e,str(i))
    return int(numbers)
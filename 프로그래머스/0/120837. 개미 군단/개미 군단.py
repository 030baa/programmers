def solution(hp):
    five, three, one = 0,0,0
    five = hp//5
    three = (hp-(five*5))//3
    one = (hp-(five*5 + three * 3)) // 1
    return five + three + one


# hp // 5 + hp%5 // 3 + (hp%5)%3 // 1

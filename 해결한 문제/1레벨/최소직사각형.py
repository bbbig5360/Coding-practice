def solution(sizes):
    min, max = sorted( sizes[0] )

    for x,y in sizes:
        # 작은 값, 큰 값으로 정렬합니다.
        x,y = sorted( [x,y] )

        # 두 값중에 작은값중에 가장 큰 값, 큰 값중에 가장 큰 값을 찾습니다.
        if x > min:
            min = x
        if y > max:
            max = y

    return min * max

print( solution([[60, 50], [30, 70], [60, 30], [80, 40]]) )
from itertools import product

def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    # 주어진 값은 + 또는 - 의 값을 잉요해 합한 후 결과값을 비교합니다. 
    # 즉, 주어진 값은 +x 또는 -x 의 2가지 경우의 수로 나뉩니다.

    s = list(map(sum, product(*l)))
    # product(*l) = [ [a,b,c,d,e], [a,b,c,d,-e], [a,b,c,-d,e], [a,b,-c,d,e], [a,-b,c,d,e], [-a,b,c,d,e], [-a,b,c,d,-e],  ...  ] 
    # itertools 라이브러리 중 product함수를 사용해 모든 경우의 수를 담은 리스트를 만듭니다.
    
    return s.count(target)
    # 후에 각 list의 값들을 합하여 target과 일치하는 개수를 찾습니다.

print( solution( [1, 1, 1, 1, 1], 3 ) )
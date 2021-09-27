from itertools import product
from copy import deepcopy

def solution(numbers):
    answer = set()
    # 정렬을 해야 밑에서 remove시 속도 향상.
    numbers = sorted( numbers )
    num_list = deepcopy(numbers)

    for num in num_list:
        # 현재와 중복되는 숫자 제거.
        numbers.remove(num)
        # 두 숫자로 이루어진 리스트 생성 후 answer와 합집합 계산.
        answer = answer | set(map(sum,product([num], numbers)))

    answer = sorted( list( answer ) )
    return answer
    
# 전에 보았던 itertools의 product가 생각나 이용했으나
# 단순 for문을 사용해 해결하는 것이 훨씬 더 효율적인 코드. 
# 아래 참고.

# def solution(numbers):
#     answer = []
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             answer.append(numbers[i] + numbers[j])
#     return sorted(list(set(answer)))

print( solution( [0, 10, 53, 21] ) )
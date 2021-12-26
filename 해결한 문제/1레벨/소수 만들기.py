import math
from itertools import combinations

# 소수 판별식
def find_prime(num):
    if num < 2:
        return False
    elif num == 2 :
        return True
    else:
        # 현재 수의 제곱근값보다 작은 경우에서 나머지가 0이 나온다면, 소수가 아님.
        for i in range(2, int( num ** 0.5 )+1 ):
            if num % i == 0:
                return False
        return True

def solution(nums):
    if len(nums) < 3:
        return 0
            
    # 리스트 내의 원소 3개로 만든 숫자의 합이 소수라면 1, 아니라면 0으로 리스트를 구성.
    # 모두 합하여 소수인 개수를 반환.
    return sum([1 if find_prime(sum(comb_nums)) else 0 for comb_nums in list(combinations(nums, 3)) ])

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))
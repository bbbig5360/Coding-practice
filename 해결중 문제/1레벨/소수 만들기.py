import math
from itertools import combinations

def find_prime(num):
    # 현재 수의 제곱근값보다 작은 경우에서 나머지가 0이 나온다면, 소수가 아님.
    for i in range(2,math.floor( math.sqrt(num) )):
        if num % i == 0:
            return False
    return True

def limit_prime_num(limit_num):
    result = [2,3,5,7,11,13,17,19]
    for check_num in range(23, limit_num):
        # 소수라면 True 반환
        if find_prime(check_num):
            result.append(check_num)
    return result


def solution(nums):
    prime_num_limit = 1000
    primes_to_limit = limit_prime_num( prime_num_limit )
    
    answer = 0
    
    for comb_nums in list(combinations(nums, 3)):
        sum_list = sum(comb_nums)
        if sum_list in primes_to_limit:
            print( f'{comb_nums}를 이용해서 {sum_list}을 만들 수 있습니다.' )
            answer += 1

    return answer

print(solution([1,2,3,4]))
# print(solution([1,2,7,6,4]))
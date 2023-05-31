import math

def check_prime_num(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    
    for i in range(2,  int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def consecutively_zero_del(n):
    while '00' in n:
        n = n.replace('00','0')
    return n

def change(n,k):
    ret_base = ''
    while n > 0:
        n, mod = divmod(n,k)
        ret_base += str(mod)

    return ret_base[::-1]

def solution(n, k):
    answer = 0
    number = str(int(consecutively_zero_del(change(n,k))))
    
    if '0' not in number:
        answer = 1 if check_prime_num(int(number)) else 0
    else:
        tmp = ''
        for num in number:
            if num != '0':
                tmp += num
            else:
                answer += 1 if check_prime_num(int(tmp)) else 0
                tmp = ''
        if tmp != '':
            answer += 1 if check_prime_num(int(tmp)) else 0
        
    return answer

print(solution(437674,3))
print(solution(110011,10))
print(solution(10,10))
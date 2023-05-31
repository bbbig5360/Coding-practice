def check_prime_num(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    
    for i in range(2, n):
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
    print('number =',number)
    
    if '0' not in number:
        answer = 1 if check_prime_num(int(number)) == True else 0
    else:
        num_list = list(map(int, number.split('0')))
        print(num_list)
        for num in num_list:
            answer += 1 if check_prime_num(num) == True else 0
        
    return answer

print(solution(437674,3))
print(solution(110011,10))
from itertools import combinations_with_replacement, permutations, product

def solution(users, emoticons):
    answer = [0,0]
    rate_list = [40, 30, 20, 10]     
    emot_len = len(emoticons)
    total_rate_list = []
    for x in range(emot_len):
        total_rate_list.append(rate_list)
    total_rate_list = list(product(*total_rate_list))    
    # print('total_rate_list =',total_rate_list)
    # print('len = ', len(total_rate_list))
    # total_rate_list = list/(permutations(rate_list, emot_len))    
    # print('total_rate_list =',total_rate_list)
    
    tmp_dict = {}
    
    # 해당 할인율일때 최대의 구독자수를 구한다.
    # 최대 구독자수에서 최대의 가격을 찾는다.
    for rate in total_rate_list:
        tmp_dict[rate] = []

        for idx, user in enumerate(users):
            price = 0
            tmp_dict[rate].append([0,0])
            
            # rate 할인율일 때 emoticon 구매시 가격 총합 추출
            for i in range(emot_len):                
                if  rate[i] >= user[0]:
                    price += emoticons[i] * (100-rate[i])
                    # print(f'user  : {user} >> i, rate, emotions, price = {i} {rate[i]} {emoticons[i]} {price/100}')
            price = int(price/100)

            # 해당 가격일때 구독한다면 바로 끝. 아니라면 price 계산
            if price >= user[1]:
                tmp_dict[rate][idx][0] = 1
                continue
            else:
                if tmp_dict[rate][idx][1] < price:
                    tmp_dict[rate][idx][1] = price
    
    # print('tmp_dict =',tmp_dict)
    for k, val in tmp_dict.items():            
            tmp_ret = [0,0]    
            for v in val:
                tmp_ret[0] += v[0]
                tmp_ret[1] += v[1]                
            
            if tmp_ret[0] > answer[0]:
                answer[0] = tmp_ret[0]
                answer[1] = tmp_ret[1]          
            
            elif tmp_ret[0] == answer[0] :
                if answer[1] < tmp_ret[1]:
                    answer[1] = tmp_ret[1]
    
    return answer


print(solution([[40,10000], [25,10000]], [7000,9000]))
print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))

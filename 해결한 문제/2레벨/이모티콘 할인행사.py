from itertools import product

def solution(users, emoticons):
    rate_list = [40, 30, 20, 10]
    emot_len = len(emoticons)
    total_rate_list = list(product(rate_list,repeat=emot_len))
    
    # {(할인율1, 할인율1, 할인율1) : [user1의 멤버 가입 여부, user1의 이모티콘 구매가격],
    #  (할인율1, 할인율1, 할인율2) : [user2의 멤버 가입 여부, user2의 이모티콘 구매가격],
    #  (할인율1, 할인율2, 할인율1) : [user3의 멤버 가입 여부, user3의 이모티콘 구매가격],
    #  ...
    # }
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
            price = int(price/100)

            # 해당 가격일때 구독한다면 바로 끝. 아니라면 price 계산
            if price >= user[1]:
                tmp_dict[rate][idx][0] = 1
                continue
            else:
                if tmp_dict[rate][idx][1] < price:
                    tmp_dict[rate][idx][1] = price
    

    answer = [0,0]    
    
    # 각 할인율에서 최대 멤버 가입수에 따른 최대 이모티콘 구매 가격을 추출
    print('tmp_dict =',tmp_dict)
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
# print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))

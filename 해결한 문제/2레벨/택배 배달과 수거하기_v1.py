import copy

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    d_sum = sum(deliveries)
    p_sum = sum(pickups)
        
    # while d_sum != 0 and p_sum != 0:
    while d_sum != 0 or p_sum != 0:
        print(deliveries)
        print(pickups)
        # print('d_sum= ',d_sum)
        # print('p_sum= ',p_sum)
        dist = 0
        
        tmp_cap = copy.deepcopy(cap)        
        for i in range(n-1,-1,-1):
            if deliveries[i] == 0:
                continue
            else:
                if dist < i+1:
                    dist = i+1                    
                if tmp_cap - deliveries[i] >= 0:
                    tmp_cap -= deliveries[i]
                    d_sum -= deliveries[i]
                    deliveries[i] = 0
                else:
                    deliveries[i] -= tmp_cap
                    d_sum -= tmp_cap                    
                    break
                
        tmp_cap = copy.deepcopy(cap)                    
        for i in range(n-1,-1,-1):
            if pickups[i] == 0:
                continue
            else:
                if dist < i+1:
                    dist = i+1
                if tmp_cap - pickups[i] >= 0:
                    tmp_cap -= pickups[i]
                    p_sum -= pickups[i]
                    pickups[i] = 0
                else:
                    pickups[i] -= tmp_cap
                    p_sum -= tmp_cap
                    break              
                    
        print('dist =',dist)
        answer += dist*2    
    return answer

# print(solution(4,5,[1,0,3,1,2],[0,3,0,4,0]))
print(solution(2,7,[1,0,2,0,1,0,2],[0,2,0,1,0,2,0]))
# print(solution(2,7,[1,9,2,10,1,0,21],[0,2,10,18,30,22,10]))
# 차량 한도/ 배달 집 / 배달 개수 / 수거 개수

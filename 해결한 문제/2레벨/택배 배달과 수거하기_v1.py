def solution(cap, n, deliveries, pickups):
    answer = 0
    if sum(deliveries) == 0 and sum(pickups) == 0:
        return answer
    
    delivery = 0
    pickup = 0
    
    for i in range(n-1,-1,-1):
        delivery += deliveries[i]
        pickup += pickups[i]
        while delivery > 0 or pickup > 0:                
            delivery -= cap
            pickup -= cap
            answer += 2*(i+1)            
        
    return answer

print(solution(4,5,[1,0,3,1,2],[0,3,0,4,0]))
print(solution(2,7,[1,0,2,0,1,0,2],[0,2,0,1,0,2,0]))
print(solution(2,7,[1,9,2,10,1,0,21],[0,2,10,18,30,22,10]))
# 차량 한도/ 배달 집 / 배달 개수 / 수거 개수

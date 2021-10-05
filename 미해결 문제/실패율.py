def solution(N, stages):
    answer = []
  
    result_list = [ 0 for x in range(1, N+1)]
    print(result_list)
    
    for stage in stages:        
        result_list[stage] += 1
        
    return answer


print( solution(5, [2,1,2,6,2,4,3,3]) )


# 스테이지 도달했으나 클리어 못한 수 / 스테이지에 도달한 플레이어 수.
# 위에 주어진 스테이지는, 도달했으나 클리어 못 함. 
# 모두 클리어한 사람은 N+1 인 사람임.즉, 클리어한 사람은 N+1의 숫자이거나, 현재 숫자보다 큰 사람.
# 현재 ?단계를 클리어하지 못한 사람은 현재의 숫자가 ?인 사람.

# 즉, 1번 스테이지 실패율 구한다.
# 2번 스테이지 실패율 = 2번 실패율 + a / ( 총 숫자 - 1번 실패한 사람 )
# 3번 스테이지 실패율 = 2번 실패율 + a / ( 총 숫자 - 1번 실패한 사람 - 2번 실패한 사람)
# 총 숫자
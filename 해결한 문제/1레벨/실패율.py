def solution(N, stages):
    result = {}
    stage_len = len(stages)

    for stage in range(1, N+1):
        if stage_len != 0:            
            # 스테이지 별로 진행중인 사람 세기
            count = stages.count(stage)
            # 현재 스테이지 실패율 = (해당 스테이지 진행중인 사람 / 현재 스테이지를 진행한 모든 사람)
            result[stage] = count/stage_len
            # 다음 스테이지 진행한 모든 사람
            stage_len -= count
        else:
            result[stage] = 0
            
    return sorted(result, key=lambda x : result[x], reverse=True)
    
print('solution = ', solution(4, [2, 1, 2, 6, 2, 4, 3, 3] ) )
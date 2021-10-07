from collections import deque

def solution(N, stages):
    answer = []
    remain_human = len(stages)

    challenge_list = [ 0 for x in range(0, N+1)]
    
    # 도전중인 인원
    for stage in stages:
        if stage != N+1:
            challenge_list[stage] += 1
        
    print('ch_list = ',challenge_list)

    zero_index = deque()
    for i, val in enumerate(challenge_list):
        if val == 0:
            zero_index.append( i )
    
    # 성공률 0인 값들 인덱스 추출.
    zero_index.remove(0)
    print('zero_index = ',zero_index)

    # 실패율
    fail_rate_list = []
    for chall in challenge_list:
        fail_rate_list.append(chall/remain_human)
        remain_human -= chall
    print('실패율 = ',fail_rate_list)

    # 실패율이 큰 인덱스부터 순서대로 추출.
    # 실패율이 0일경우, 모두 0이 됨. 즉, 위에서 실패율 0인 인덱스 추출. 후에 대입.
    for i in range( len(fail_rate_list)-1 ):
        max_index = fail_rate_list.index(max(fail_rate_list))
        answer.append( max_index )
        fail_rate_list[max_index] = 0
    print('실패율이 큰 인덱스부터 추출 ',answer)

    # 0일 경우, zero index일 경우 
    for i in range(N):
        try:
            if answer[i] == 0:
                del answer[i]
                answer.insert(i,zero_index.popleft())
                print(answer)
        except:
            break
    return answer


# print( 'solution = ',solution(5, [2,1,2,6,2,4,3,3]) )

print('solution = ', solution(4, [4,4,4,4,4]) )

# 스테이지 도달했으나 클리어 못한 수 / 스테이지에 도달한 플레이어 수.
# 위에 주어진 스테이지는, 도달했으나 클리어 못 한 스테이지. 즉, 현재 ?단계를 클리어하지 못한 사람은 현재의 숫자가 ?인 사람.

# 즉, 1번 스테이지 실패율 구한다.
# 2번 스테이지 실패율 = 2번 실패율 + a / ( 총 숫자 - 1번 실패한 사람 )
# 3번 스테이지 실패율 = 2번 실패율 + a / ( 총 숫자 - 1번 실패한 사람 - 2번 실패한 사람)
# 총 숫자
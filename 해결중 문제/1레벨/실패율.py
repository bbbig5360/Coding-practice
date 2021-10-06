def solution(N, stages):
    answer = []
    remain_human = len(stages)

    challenge_list = [ 0 for x in range(0, N+1)]
    
    # 도전중인 인원
    for stage in stages:
        if stage != N+1:
            challenge_list[stage] += 1
    print(challenge_list)

    zero_index = set([0])
    print(zero_index)
    for i, val in enumerate(challenge_list):
        if val == 0:
            zero_index.add( i )
        
    zero_index = zero_index - {0}
    print('zero_index = ',zero_index)
    # 실패율
    tmp = []
    for chall in challenge_list:
        tmp.append(chall/remain_human)
        remain_human -= chall

    for i in range( len(tmp)-1 ):
        max_index = tmp.index(max(tmp))
        answer.append( max_index )
        tmp[max_index] = 0

    for i in range(N):
        try:
            if answer[i] == 0:
                del answer[i]
                answer.insert(i,zero_index.pop())
                print(answer[-1])
        except:
            break
    return answer


print( 'solution = ',solution(5, [2,1,2,6,2,4,3,3]) )

print('solution = ', solution(4, [4,4,4,4,4]) )

# 스테이지 도달했으나 클리어 못한 수 / 스테이지에 도달한 플레이어 수.
# 위에 주어진 스테이지는, 도달했으나 클리어 못 한 스테이지. 즉, 현재 ?단계를 클리어하지 못한 사람은 현재의 숫자가 ?인 사람.

# 즉, 1번 스테이지 실패율 구한다.
# 2번 스테이지 실패율 = 2번 실패율 + a / ( 총 숫자 - 1번 실패한 사람 )
# 3번 스테이지 실패율 = 2번 실패율 + a / ( 총 숫자 - 1번 실패한 사람 - 2번 실패한 사람)
# 총 숫자
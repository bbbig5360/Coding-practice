import copy

def bonus_step(ch, score):
    # print('bonus_step')
    if ch == 'S':
        return score
    elif ch == 'D':
        return score * score
    else:
        return score * score * score
    
def option_step(ch, score, pre_score):
    # print('option step')
    # print('pre_score = ', pre_score)
    return score * 2 + pre_score if ch == '*' else score * -1

def solution(dartResult):
    answer = 0
    step_flag = True
    tmp_score = 0
    special_ch = ['*', '#']
    
    for ch in dartResult:
        # print(ch, end=' ')
        # 시작이 숫자일 경우
        # *, # 존재할 경우 처리
        if step_flag:
            if not ch.isdigit():
                tmp_score = option_step(ch, tmp_score, pre_score)
                continue
            answer += tmp_score
            pre_score = copy.deepcopy(tmp_score)
            tmp_score = int(ch)
            step_flag = False
        # 이어진 숫자가 존재하는 경우(10)
        # S, D, T 존재할 경우 처리
        else:
            if ch.isdigit():
                tmp_score = int(str(tmp_score)+ch)
                continue
            else:
                tmp_score = bonus_step(ch, tmp_score)
                step_flag = True
                
    answer += tmp_score    
    return answer

print('result = ',solution('1S2D*3T')) # 37
print('result = ',solution('1D2S#10S')) # 9
print('result = ',solution('1D2S0T')) # 3
print('result = ',solution('1S*2T*3S')) # 23
print('result = ',solution('1D#2S*3S')) # 5
print('result = ',solution('1T2D3D#')) # -4
print('result = ',solution('1D2S3T*')) # 59
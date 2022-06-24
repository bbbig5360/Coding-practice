import copy

def first_step(ch):
    print('1st_step')
    return int(ch)

def second_step(ch, score):
    print('2nd_step')
    if ch == 'S':
        return score
    elif ch == 'D':
        return score * score
    else:
        return score * score * score
    
def third_step(ch, score, pre_score):
    print('3rd step')
    print('pre_score = ', pre_score)
    return score * 2 + pre_score if ch == '*' else score * -1

def solution(dartResult):
    answer = 0
    step_flag = 0
    tmp_score = 0
    special_ch = ['*', '#']
    
    for ch in dartResult:
        print(ch, end=' ')
        # 1단계. 시작 숫자 확보.
        # *#이 연속으로 들어갔을 경우 처리.
        if step_flag == 0:
            if not ch.isdigit():
                tmp_score = third_step(ch, tmp_score, pre_score)
                continue
            answer += tmp_score
            pre_score = copy.deepcopy(tmp_score)
            tmp_score = first_step(ch)
            
        # S, D, T 처리
        elif step_flag == 1:
            if ch.isdigit():
                tmp_score = first_step(str(tmp_score)+ch)
                step_flag = 0
            else:
                tmp_score = second_step(ch, tmp_score)
            
        # 입력된 형식이 끝나거나 *,#이 나왔을 경우 처리
        else:
            if ch in special_ch:
                tmp_score = third_step(ch, tmp_score, pre_score)
                step_flag = -1
            else:
                answer += tmp_score
                pre_score = copy.deepcopy(tmp_score)
                tmp_score = first_step(ch)
                step_flag = 0                
        step_flag += 1
        
    answer += tmp_score    
    return answer

# print('result = ',solution('1S2D*3T')) # 37
# print('result = ',solution('1D2S#10S')) # 9
# print('result = ',solution('1D2S0T')) # 3
# print('result = ',solution('1S*2T*3S')) # 23
# print('result = ',solution('1D#2S*3S')) # 5
# print('result = ',solution('1T2D3D#')) # -4
print('result = ',solution('1D2S3T*')) # 59
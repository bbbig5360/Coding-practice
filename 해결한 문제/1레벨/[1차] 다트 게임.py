import copy

def bonus_step(ch, score):
    # print('bonus_step')
    score = int(score)
    
    if ch == 'S':
        return score
    elif ch == 'D':
        return score ** 2
    else:
        return score ** 3
    
def option_step(ch, score, pre_score):
    # print('option step, pre_score = ', pre_score)
    return (2*score + pre_score if ch == '*' else -score), True if ch in '*' else False

def solution(dartResult):
    answer = 0
    tmp_score = 0
    step_flag = True
    star_flag = False
    
    for ch in dartResult:
        # print(ch, end=' ')
        # 시작이 숫자일 경우와
        # *, # 존재할 경우
        # 마지막 결과 총합까지 처리
        if step_flag:
            if not ch.isdigit():
                tmp_score, star_flag = option_step(ch, tmp_score, pre_score)
                continue
            answer += tmp_score
            # print('answer = ', answer)
            
            pre_score = copy.deepcopy(tmp_score) - pre_score if star_flag else copy.deepcopy(tmp_score)
            tmp_score = ch
            step_flag = False
            
        # 이어진 숫자가 존재하는 경우(10)와
        # S, D, T 존재할 경우 처리
        else:
            if ch.isdigit():
                tmp_score = tmp_score + ch
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
print('result = ',solution('1S2D*3T*')) # 72
print('result = ',solution('1S*2D*3T*')) # 74
print('result = ',solution('1S#2D*3T*')) # -1 -1 + 8 + 8 + 54 = 68
print('result = ',solution('1D#2S#0T*')) # -1 -2 -2 + 0 = -5
print('result = ',solution('10S*2T*10S')) # 20 + 20 + 16 + 10 = 66
print('result = ',solution('10S*2T#3S*')) # 20 - 8 - 8 + 6 = 10
print('result = ',solution('10S*2T#3S*5S*2D#')) # 20 - 8 - 8 + 6 + 6 + 10 - 4 = 22
print('result = ',solution('10S*2T#3S5S*2D#')) # 20 - 8 + 3 + 3 + 10 - 4 = 24
print('result = ',solution('1S2T#3S5S*2D#')) # 1 - 8 + 3 + 3 + 10 - 4 = 5
print('result = ',solution('2T#3S5S*2D#')) # -8 + 3 + 3 + 10 - 4 = 4
print('result = ',solution('2T#3S*5S2D#')) # -8 -8 + 6 + 5 - 4 = -9
print('result = ',solution('2T#3S*5S2D')) # -8 -8 + 6 + 5 + 4 = -1
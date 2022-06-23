def first_step(ch):
    print('first_step')
    return int(ch)

def second_step(ch, score):
    print('2nd_step')
    if ch == 'S':
        return score
    elif ch == 'D':
        return score * score
    else:
        return score * score * score
    

def third_step(ch, score):
    print('3rd step')
    return score * 2 if ch == '*' else score * -1

def solution(dartResult):
    answer = 0
    step_flag = 0
    tmp_score = 0
    special_ch = ['*', '#']
    
    for ch in dartResult:
        print(ch, end=' ')
        # 1단계. 숫자 확보.
        # *#이 연속으로 들어갔을 경우 처리.
        if step_flag == 0:
            if not ch.isdigit():
                tmp_score = third_step(ch, tmp_score)
                continue
            answer += tmp_score
            tmp_score = first_step(ch)
            
        # S, D, T 처리
        elif step_flag == 1:
            tmp_score = second_step(ch, tmp_score)
            
        # 입력된 형식이 끝나거나 *,#이 나왔을 경우 처리
        else:
            if ch in special_ch:
                tmp_score = third_step(ch, tmp_score)
                step_flag = -1
            else:
                answer += tmp_score
                tmp_score = first_step(ch)
                step_flag = 0                
        step_flag += 1
    answer += tmp_score    
    
    return answer

print('result = ',solution('1S2D*3T'))
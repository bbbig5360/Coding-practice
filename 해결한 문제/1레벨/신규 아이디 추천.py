import string

def solution(new_id):
    new_id = new_id.lower()
    alphabet_list = list(string.ascii_lowercase)
    num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    special_char_list = ['-', '_', '.']
    answer = []

    for ch in new_id:
        if ch in alphabet_list or ch in num_list:
            answer.append(ch)
        elif ch in special_char_list:
            answer.append(ch)
            try:
                if answer[-1] == '.' and answer[-2] == '.':
                    answer.pop()
            except:
                pass
        if len(answer)>16:
            break
    
    if answer == []:
        answer = ['a',]
    
    else:
        if answer[0] == '.':
            del answer[0]

        if len(answer) > 15:
            answer = answer[:15]
        
    try:
        if answer[-1] == '.':
            answer = answer[:-1]
    except:
        answer = ['a',]
    
    if len(answer) < 3:
        while len(answer) < 3:
            answer.append(answer[-1])

    return ''.join(answer)

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
# 모두 소문자(lower 사용)
# a~z, -, _, .
# . => 처음과 끝 안 됨. 연속 안 됨.
# 규격에 맞는지 확인 후 새로운 아이디 추천.
    # 규격에 맞는 경우
    # 규격에 맞지 않는 경우
    
    # 정규식으로 모든 문자 가져오기. a~z, -, _, .가져오기.
    # 마침표 연속 확인. 2개 이상 -> 하나로.
    

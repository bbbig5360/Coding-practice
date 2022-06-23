def solution(new_id):
    new_id = new_id.lower()
    special_list = ['-', '_', '.']
    answer = ''

    for ch in new_id:
        if ch.isalpha() or ch.isdigit():
            answer+=ch
        elif ch in special_list:
            try:
                if ch == '.' and answer[-1] == '.':
                    continue
                else:
                    answer+=ch
            except:
                pass
        if len(answer) > 15:
            break
    
    if answer == '':
        answer = 'a'
    
    else:
        if answer[0] == '.':
            answer = answer[1:]

        if len(answer) > 15:
            answer = answer[:15]
        
        try:
            if answer[-1] == '.':
                answer = answer[:-1]
        except:
            answer = 'a'
    
    if len(answer) < 3:
        while len(answer) < 3:
            answer+=answer[-1]

    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
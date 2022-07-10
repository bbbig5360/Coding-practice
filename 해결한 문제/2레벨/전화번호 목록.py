def solution(phone_book):
    answer = True
    
    for idx, word in enumerate(phone_book):
        word_len = len(word)
        
        for idx2, ch in enumerate(phone_book):
            if idx == idx2:
                continue
            if word == ch[:word_len]:
                answer = False
                break
            
        if answer == False:
            break
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))

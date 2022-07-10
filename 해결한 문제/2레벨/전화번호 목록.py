def solution(phone_book):
    answer = True
    phone_book.sort()
    tot_len = len(phone_book)

    for i in range(tot_len):
        if tot_len > i + 1:
            start_num = phone_book[i]
            y = phone_book[i+1]
            
            if start_num > y:
                start_num, y = y, start_num
                
            if start_num in y[:len(start_num)]:
                answer = False
                break
        
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","1234121","1235","567","88"]))

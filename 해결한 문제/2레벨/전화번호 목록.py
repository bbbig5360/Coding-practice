def solution(phone_book):
    answer = True
    phone_book.sort()
    tot_len = len(phone_book)

    for i in range(tot_len):
        if tot_len > i + 1:
            x = phone_book[i]
            y = phone_book[i+1]
            
            if x < y:
                if x in y[:len(x)]:
                    answer = False
                    break
            else:
                if y in x[:len(y)]:
                    answer = False
                    break
        
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","1234121","1235","567","88"]))

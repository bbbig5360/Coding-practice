def solution(phone_book):
    phone_book.sort()
    tot_len = len(phone_book)

    for i in range(tot_len):
        if tot_len > i + 1:
            x = phone_book[i]
            y = phone_book[i+1]
            
            if x > y:
                x, y = y, x
                
            if y.startswith(x):
                return False
        
    return True

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","1234121","1235","567","88"]))

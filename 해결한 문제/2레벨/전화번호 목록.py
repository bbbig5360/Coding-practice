from itertools import combinations

def solution(phone_book):
    answer = True
          
    check_list = list(combinations(phone_book, 2))

    for x in check_list:
        i, j = x
        if i < j:
            if i in j[:len(i)]:
                answer = False
                break
        else:
            if j in i[:len(j)]:
                answer = False
                break
        
    return answer

print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))

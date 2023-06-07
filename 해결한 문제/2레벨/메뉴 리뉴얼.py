import itertools

def solution(orders, course):
    answer = set()
    single_menu = set()
    
    for menu in ''.join(orders):
        single_menu.add(menu)
    single_menu = sorted(single_menu)    
    
    for c_num in course:
        course_combination_list = list(map(''.join,itertools.combinations(single_menu, c_num)))
        course_dict = {}
        for order in orders:
            for course_combination in course_combination_list:
                flag = True
                for c in course_combination:
                    if c in order:
                        continue
                    else:
                        flag = False
                if flag:
                    if course_dict.get(course_combination) != None:
                        course_dict[course_combination] += 1
                    else:
                        course_dict[course_combination] = 1
        
        tmp = ''
        max_cnt = 0
        for combination, count  in course_dict.items():
            if count < 2:
                continue
            if max_cnt < count:
                max_cnt = count
                tmp = combination
        if tmp != '':
            answer.add(tmp)
            
        for combination, count  in course_dict.items():
            if max_cnt == 0:
                break
            if max_cnt == count:
                answer.add(combination)
        
        course_dict.clear()
    
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
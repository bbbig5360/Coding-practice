import itertools

def solution(orders, course):
    answer = []
    single_menu = set()
    
    for menu in ''.join(orders):
        single_menu.add(menu)
    single_menu = sorted(single_menu)
    
    for c_num in course:
        course_dict = {}    
        for order in orders:
            course_combination_list = list(itertools.combinations(sorted(order), c_num))
            for course_combination in course_combination_list:
                flag = True
                for c in course_combination:
                    if c not in order:
                        flag = False
                        break
                if flag:
                    if course_dict.get(course_combination) != None:
                        course_dict[course_combination] += 1
                    else:
                        course_dict[course_combination] = 1
        
        tmp = []
        max_cnt = 2
        for combination, count  in course_dict.items():
            if max_cnt < count:
                max_cnt = count
                tmp.clear()
                tmp.append(combination)
            elif max_cnt == count:
                tmp.append(combination)
                
        for t in tmp:
            answer.append(''.join(t))
            
        course_dict.clear()

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
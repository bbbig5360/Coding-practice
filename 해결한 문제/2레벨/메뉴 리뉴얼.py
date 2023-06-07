from time import time
import itertools

def solution(orders, course):
    answer = set()
    single_menu = set()
    
    for menu in ''.join(orders):
        single_menu.add(menu)
    single_menu = sorted(single_menu)    
    
    
    
    for c_num in course:
        if len(single_menu) < c_num:
            continue
        st = time()
        course_combination_list = list(itertools.combinations(single_menu, c_num))
        print('combination time = ', time() - st )

        course_dict = {}    
        for order in orders:
            # collections Counter 사용하는것과 같음
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
        print('get courst_dict time = ', time() - st)
        st = time()
        
        # collections의 .most_common과 같음
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
            answer.add(''.join(t))
            
        course_dict.clear()

        print('calcurate max count time = ',time() - st)
    return sorted(answer)

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["ABCDEFGHI", "ABDGHIZ", "CDXJKWZ", "ADEFGIK", "LMNOXYZ", "PQXYZ", "ACDRZ"], [5,6,7]))
# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
# print(solution(["XYZ", "XWY", "WXA"], [1,2,3,4]))



print(list(map(''.join,itertools.combinations(['a','b'], 3))))
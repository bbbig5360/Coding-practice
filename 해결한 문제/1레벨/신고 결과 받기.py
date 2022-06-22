def solution(id_list, report, k):
    
    if report == []:
        return [0 for x in range(len(id_list))]
    
    # print(report)
    report_dict = {}
    for id in id_list:
        report_dict[id] = []

    reported_dict = {}
    for one_report in set(report):
        report_p, reported_p = one_report.split(' ')
        try:
            reported_dict[reported_p] += 1
        except:
            reported_dict[reported_p] = 1

        if reported_p not in report_dict[report_p]:
            report_dict[report_p].append(reported_p)
        else:
            reported_dict[reported_p] -= 1

    # print('id_list = ', id_list)
    # print('report_dict = ', report_dict)
    # print('reported_dict = ', reported_dict)

    punished_people = []

    for key, val in reported_dict.items():
        if val >= k:
            punished_people.append(key)

    answer = [0 for x in range(len(id_list))]
    
    for idx, (key, vals) in enumerate(report_dict.items()):
        # print('key = ', key)
        if len(vals) >= 1:
            for val in vals:
                if val in punished_people:
                    print('punished +1')
                    answer[idx] += 1
        else:
            continue            
    
    return answer


# print( solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2) )
# print('solution = ',solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print('solution2 = ', solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))

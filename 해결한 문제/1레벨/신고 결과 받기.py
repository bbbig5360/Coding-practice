def solution(id_list, report, k):    
    answer = [0] * len(id_list)

    if report == []:
        return answer

    report = set(report)
    # 중복 제거
    
    reported_dict = {x : 0 for x in id_list}

    for record in report:
        report_p, reported_p = record.split(' ')
        reported_dict[reported_p] += 1
            
    # print('id_list = ', id_list)
    print('reported_dict = ', reported_dict)

    id_list_dict = {x : idx for idx, x in enumerate(id_list)}
    # {'muzi': 0, 'frodo': 1, 'apeach': 2, 'neo': 3}
    
    for record in report:
        report_p, reported_p = record.split(' ')
                
        if reported_dict[reported_p] >= k:
            # 신고한 사람이 일정 수 이상이면 처벌받음
            # 해당 인원이 처벌됐다는 메일을 신고한 사람에게 메세지 보낸 횟수 추가함
            answer[id_list_dict[report_p]] += 1
        
    return answer

# print('solution = ',solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print('solution2 = ', solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
def binary_search(max, tmp_info_list, score):
    start = 0
    end = max
    
    while start != end and start != max:
        if tmp_info_list[(start+end)//2][0] >= int(score):
            end = (start+end)//2
        else:
            start = (start+end)//2 + 1
    return start
    
def solution(info, query):
    answer = []
    info_list = []
    info_len = len(info)
    
    # st = time.time()
    for idx, info_row in enumerate(info):
        score, food, career, ability, language = info_row.split()[::-1]
        info_row = [int(score), food, career, ability, language]
        info_list.append(info_row)

    info_list.sort()
    # print(info_list)
    
    for query_row in query:
        # st = time.time()
        query_list = [x for x in query_row.split()[::-1] if x != 'and']
        # print('query_list =', query_list)
        
        info_strainer = [True]*info_len
        target_idx = 0
        for idx, query_element in enumerate(query_list):
            # print('idx', idx)
            # print(info_row[idx],query_element)
            if query_element == '-':
                continue
            
            if idx == 0:
                # 여기서 점수값 위치 binary search
                target_idx = binary_search(info_len, info_list, query_element)
                
            for info_idx in range(target_idx, info_len):
                # print(info_row[idx], query_element)
                if info_strainer[info_idx] == False:
                    continue
                
                if idx != 0:
                    if info_list[info_idx][idx] != query_element:
                        info_strainer[info_idx] = False
                        continue
                    
        answer.append(info_strainer.count(True)-target_idx)
        # print(query_row, (time.time() - st)*(100000))
    return answer


print(solution(["java backend junior pizza 150",
                "python frontend senior chicken 210",
                "python frontend senior chicken 150",
                "cpp backend senior pizza 260",
                "java backend junior chicken 80",
                "python backend senior chicken 50"],
                ["java and backend and junior and pizza 100",
                "python and frontend and senior and chicken 200",
                "cpp and - and senior and pizza 250",
                "- and backend and senior and - 150",
                "- and - and - and chicken 100",
                "- and - and - and - 150"]
                )
     )
from collections import defaultdict

def solution(info, query):
    answer = []
    info_list = []
    
    for info_row in info:
        split_list = info_row.split()
        tmp_dict = defaultdict(lambda:int(split_list[-1]))
        for element in split_list:
            tmp_dict[element]
        info_list.append(tmp_dict)    
    
    for query_row in query:
        query_list = [ x for x in query_row.split() if x != 'and']
    
        cnt = 0
        for info_row in info_list:      
            query_idx = -1
            for query_element in query_list:
                if query_element == '-':
                    query_idx += 1
                    continue
                query_idx += 1
                
                if query_idx != 4:
                    if query_element not in info_row:
                        break
                else:
                    if int(query_element) <= list(info_row.values())[0]:
                        cnt += 1
        answer.append(cnt)
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
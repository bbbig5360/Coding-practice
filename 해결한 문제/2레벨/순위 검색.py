def solution(info, query):
    answer = []
    
    for query_row in query:
        query_list = query_row.split()
        # print('query_list =',query_list)
        
        cnt = 0
        for info_row in info:      
            query_index = -1
            for query_element in query_list:
                # [and, -] 무시함. 이후 index 맞춰줄 것
                if query_element == 'and':
                    continue
                elif query_element == '-':
                    query_index += 1
                    continue
                else:
                    query_index += 1
                
                # 마지막 조건까지 맞는다면 조건에 부합하는 것으로 카운트
                if query_index < 4:
                    if query_element not in info_row:
                        break
                else:
                    if int(query_element) <= int(info_row.split()[-1]):
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
import time

def solution(info, query):
    answer = []
    info2number_list = []
    
    element2number_dict = {'cpp':0, 'backend':0, 'junior':0, 'chicken':0, 'java':1, 'frontend':1, 'senior':1, 'pizza':1, 'python':2}
    
    '''
    cpp, java, python
    backend, frontend
    junior senior
    chicken pizza
    '''
    st = time.time()
    for idx, info_row in enumerate(info):
        info_list = info_row.split()
        info2number_list.append([])
        for element in info_list:
            if element in ['cpp', 'backend', 'junior', 'chicken']:
                info2number_list[idx].append(0)
            elif element in ['java', 'frontend', 'senior', 'pizza']:
                info2number_list[idx].append(1)
            elif element == 'python':
                info2number_list[idx].append(2)
            else:
                info2number_list[idx].append(int(element))
    print('info to number time =',(time.time() - st)*(100000))

    for query_row in query:
        st = time.time()
        query_list = query_row.split()
        info_strainer = [True]*len(info2number_list)
        # print('query_list =',query_list)
        
        query_index = -1
        # query 내부 원소값으로 비교함. 해당 인덱스의 위치는 query index로 설정
        for query_element in query_list:
            # [and, -] 무시함. 이후 index 맞춰줄 것
            if query_element == 'and':
                continue
            elif query_element == '-':
                query_index += 1
                continue
            else:
                query_index += 1
                
            # 하나씩 info_row를 확인. 해당하지 않는 경우 info_strainer에 False
            for idx, info_row in enumerate(info2number_list):
                
                # 걸러지는 경우
                if not info_strainer[idx]:
                    continue
                
                # 계속 진행하는 경우
                # 위의 dictionary에 없는 경우, 코딩 점수임
                if element2number_dict.get(query_element) == None:
                    if int(query_element) > info_row[query_index]:
                        info_strainer[idx] = False
                else:
                    if element2number_dict[query_element] != info_row[query_index]:
                        info_strainer[idx] = False
        answer.append(info_strainer.count(True))
        # print('info_strainer =',info_strainer)
        # print('info_strainer.count(True) =',info_strainer.count(True))
        print(query_row, (time.time() - st)*(100000))
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
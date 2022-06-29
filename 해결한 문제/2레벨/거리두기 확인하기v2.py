def all_check(places, row_idx, col_idx, order):
    check_position = [[0,1],[1,0],[-1,0],[0,-1]]
    check_direction = [0, 1, 2, 3]
    reverse_dir_dict = {0:3, 1:2, 2:1, 3:0}
    # {'right':0, 'under':1, 'up':2, 'left':3}
    ret = False
    for pos, dir in zip(check_position, check_direction):
        check_dir = reverse_dir_dict[dir]
        # 시작한 방향 예외처리. 
        # 예시) 왼쪽에서 시작했다면 왼쪽은 제외하고 상하좌우 확인
        if order != check_dir:
            tmp_row_idx = row_idx + pos[0]
            tmp_col_idx = col_idx + pos[1]

            if tmp_row_idx < 0 or tmp_col_idx < 0:
                continue
            try:
                if places[tmp_row_idx][tmp_col_idx] == 'P':
                    ret = True
                    # print('POP find : ', row_idx, col_idx, ' -> ', tmp_row_idx, tmp_col_idx)
                    break
            except:
                pass
    return ret

def check_element(places, row_idx, col_idx, order):
    ret = False
    order_dict = {'right':0, 'under':1, 'up':2, 'left':3}
    pos_dict = {0:[0,1], 1:[1,0], 2:[-1,0], 3:[0,-1]}
    
    order = order_dict[order]
    row_idx += pos_dict[order][0]
    col_idx += pos_dict[order][1]
    # 방향에 맞는 위치로 이동

    try: 
        check_ch = places[row_idx][col_idx]
        if check_ch == 'P':
            ret = True 
        elif check_ch == 'O':
            ret = all_check(places, row_idx, col_idx, order)
        elif order == 0 and check_ch == 'X':
            # 예외 케이스. 오른쪽과 아래만 확인하다보니 생기는 문제. 
            # OPXXX, PXOOO의 경우에 찾지못함.
            try:
                row_idx -= 1
                col_idx -= 1
                if row_idx < 0 or col_idx < 0:
                    return False

                if places[row_idx][col_idx] == 'O' and places[row_idx][col_idx+1] == 'P':
                    ret = all_check(places, row_idx, col_idx, order)
            except:
                pass
        else:
            pass
    except:
        pass
    
    return ret    

def solution(places):
    answer = []
    ret = False
    
    for place in places:
        right_ret = False
        under_ret = False
        ret = False
        for row_idx, row in enumerate(place):
            for col_idx, ch in enumerate(row):
                # 사람이 있는지 확인. 이후 오른쪽과 아래쪽 확인
                # 오른쪽과 아래로 훑어가면 전부 훑게되기 때문
                # 이후 O가 나온다면 상하좌우 체크 = all_check()함수
                if ch == 'O':
                    right_ret = check_element(place, row_idx, col_idx, 'right')
                    under_ret = check_element(place, row_idx, col_idx, 'under')
                    if right_ret or under_ret:
                        ret = True
                        break
            if ret:
                break
        answer.append(0 if ret else 1)
    return answer        

# print('result = ', solution([["POOOP","OXXOX","OPXPX","OOXOX","POXXP"],
#                              ["POOPX","OXPXP","PXXXO","OXXXO","OOOPP"], 
#                              ["PXOPX","OXOXP","OXPOX","OXXOP","PXPOX"], 
#                              ["OOOXX","XOOOX","OOOXX","OXOOX","OOOOO"],
#                              ["PXPXP","XPXPX","PXPXP","XPXPX","PXPXP"]] ))

print('result = ', solution([["OPXOP", 
                              "PXPXO",
                              "OOXPO"],]))
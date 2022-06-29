def check_P(place, row_idx, col_idx):
    pos_list = [[0,1], [1,0], [-1,0], [0,-1]]
    p_cnt = 0

    for pos in pos_list:
        tmp_row_idx = row_idx + pos[0]
        tmp_col_idx = col_idx + pos[1]

        if tmp_row_idx < 0 or tmp_col_idx < 0:
            continue

        try: 
            if place[tmp_row_idx][tmp_col_idx] == 'P':
                p_cnt += 1
        except:
            continue

        if p_cnt >= 2:
            break
    
    return True if p_cnt >= 2 else False

def check_element(place, row_idx, col_idx, order):
    ret = False
    order_dict = {'right':0, 'under':1, 'up':2, 'left':3}
    pos_dict = {0:[0,1], 1:[1,0], 2:[-1,0], 3:[0,-1]}
    
    order = order_dict[order]
    row_idx += pos_dict[order][0]
    col_idx += pos_dict[order][1]

    if row_idx < 0 or col_idx < 0:
        return False
                    
    try: 
        check_ch = place[row_idx][col_idx]
        if check_ch == 'P':
            ret = True 
    except:
        pass
    
    return ret    

def solution(places):
    answer = []
    ret = False
    
    for place in places:
        right_ret = False
        under_ret = False
        o_ret = False
        ret = False
        for row_idx, row in enumerate(place):
            for col_idx, ch in enumerate(row):
                if ch == 'P':
                    right_ret = check_element(place, row_idx, col_idx, 'right')
                    under_ret = check_element(place, row_idx, col_idx, 'under')
                    
                elif ch == 'O':
                    o_ret = check_P(place, row_idx, col_idx)

                if right_ret or under_ret or o_ret:
                    ret = True
                    break

            if ret:
                break
        answer.append(0 if ret else 1)
    return answer        
    
print('result = ', solution([["POOOP","OXXOX","OPXPX","OOXOX","POXXP"],
                             ["POOPX","OXPXP","PXXXO","OXXXO","OOOPP"], 
                             ["PXOPX","OXOXP","OXPOX","OXXOP","PXPOX"], 
                             ["OOOXX","XOOOX","OOOXX","OXOOX","OOOOO"],
                             ["PXPXP","XPXPX","PXPXP","XPXPX","PXPXP"]] ))

print('result = ', solution([["OPXOP", 
                              "PXPXO",
                              "OOXPO"],]))
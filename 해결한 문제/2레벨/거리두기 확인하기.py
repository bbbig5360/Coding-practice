def right_check(places, row, row_idx, col_idx):
    ret = False
    try:
        ret = True if places[row_idx][col_idx + 1] == 'P' else False
    except:
        pass
    return ret

def under_check(places, row, row_idx, col_idx):
    ret = False
    try:
        ret = True if places[row_idx+1][col_idx] == 'P' else False
    except:
        pass
    return ret

def solution(places):
    answer = []
    tmp_class = []
    ret = False
    for place in places:
        for row_idx, row in enumerate(place):
            print(row)
            for col_idx, ch in enumerate(row):
                if ch == 'P':
                    right_ret = right_check(places, row, row_idx, col_idx)
                    under_ret = under_check(places, row, row_idx, col_idx)
                if right_ret or under_ret:
                    print(right_ret, under_ret)
                    break
            if ret:
                break
        print()
        answer.append(0 if ret else 1)
    return answer        

print('result = ', solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]], ))
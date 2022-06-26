def solution(dartResult):
    score_list = []
    tmp_ch = ''
    for ch in dartResult:
        if ch.isdigit():
            tmp_ch += ch
        else:
            if ch == 'S':
                score_list.append(int(tmp_ch))
            elif ch == 'D':
                score_list.append(int(tmp_ch)**2)
            elif ch == 'T':
                score_list.append(int(tmp_ch)**3)
            elif ch == '#':
                score_list[-1] = -score_list[-1]
            elif ch == '*':
                try:
                    score_list[-1] = score_list[-1] * 2
                    score_list[-2] = score_list[-2] * 2
                except:
                    pass
            tmp_ch = ''
    return sum(score_list)

print('result = ',solution('1S2D*3T')) # 37
print('result = ',solution('1D2S#10S')) # 9
print('result = ',solution('1D2S0T')) # 3
print('result = ',solution('1S*2T*3S')) # 23
print('result = ',solution('1D#2S*3S')) # 5
print('result = ',solution('1T2D3D#')) # -4
print('result = ',solution('1D2S3T*')) # 59
print('result = ',solution('1S2D*3T*')) # 72
print('result = ',solution('1S*2D*3T*')) # 74
print('result = ',solution('1S#2D*3T*')) # -1 -1 + 8 + 8 + 54 = 68
print('result = ',solution('1D#2S#0T*')) # -1 -2 -2 + 0 = -5
print('result = ',solution('10S*2T*10S')) # 20 + 20 + 16 + 10 = 66
print('result = ',solution('10S*2T#3S*')) # 20 - 8 - 8 + 6 = 10
print('result = ',solution('10S*2T#3S*5S*2D#')) # 20 - 8 - 8 + 6 + 6 + 10 - 4 = 22
print('result = ',solution('10S*2T#3S5S*2D#')) # 20 - 8 + 3 + 3 + 10 - 4 = 24
print('result = ',solution('1S2T#3S5S*2D#')) # 1 - 8 + 3 + 3 + 10 - 4 = 5
print('result = ',solution('2T#3S5S*2D#')) # -8 + 3 + 3 + 10 - 4 = 4
print('result = ',solution('2T#3S*5S2D#')) # -8 -8 + 6 + 5 - 4 = -9
print('result = ',solution('2T#3S*5S2D')) # -8 -8 + 6 + 5 + 4 = -1
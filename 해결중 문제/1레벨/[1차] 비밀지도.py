def solution(n, arr1, arr2):
    answer = []
    modular_arr1 = []
    modular_arr2 = []
    for i in range(n):
        modular_arr1.append([])
        modular_arr2.append([])

        while arr1[i] > 0:
            modular_arr1[i].append( arr1[i] % 2 )
            arr1[i] = arr1[i] // 2
        modular_arr1[i].reverse()
        while len( modular_arr1[i] ) != n:
            modular_arr1[i].insert(0,0)
        
        while arr2[i] > 0:
            modular_arr2[i].append( arr2[i] % 2 )
            arr2[i] = arr2[i] // 2
        modular_arr2[i].reverse()
        while len( modular_arr2[i] ) != n:
            modular_arr2[i].insert(0,0)

    arr_len = len( modular_arr1 )

    for j in range( arr_len ) :
        answer.append([])
        for i in range(n):
            answer[j].append( modular_arr1[j][i] + modular_arr2[j][i] )
        
    for j in range( arr_len ):
        for i in range(n):
            if answer[j][i] >= 1:
                answer[j][i] = '#'
            else:
                answer[j][i] = ' '
        answer[j] = ''.join(answer[j])
    return answer

print(solution( 6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10] ))

# 해결은 했지만 코드를 더 깔끔하게 바꿔볼 것.
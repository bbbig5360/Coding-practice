# def solution(n, arr1, arr2):
#     answer = []
#     modular_arr1 = []
#     modular_arr2 = []
#     for i in range(n):
#         modular_arr1.append([])
#         modular_arr2.append([])

#         while arr1[i] > 0:
#             modular_arr1[i].append( arr1[i] % 2 )
#             arr1[i] = arr1[i] // 2
#         modular_arr1[i].reverse()
#         while len( modular_arr1[i] ) != n:
#             modular_arr1[i].insert(0,0)
        
#         while arr2[i] > 0:
#             modular_arr2[i].append( arr2[i] % 2 )
#             arr2[i] = arr2[i] // 2
#         modular_arr2[i].reverse()
#         while len( modular_arr2[i] ) != n:
#             modular_arr2[i].insert(0,0)

#     arr_len = len( modular_arr1 )

#     for j in range( arr_len ) :
#         answer.append([])
#         for i in range(n):
#             answer[j].append( modular_arr1[j][i] + modular_arr2[j][i] )
        
#     for j in range( arr_len ):
#         for i in range(n):
#             if answer[j][i] >= 1:
#                 answer[j][i] = '#'
#             else:
#                 answer[j][i] = ' '
#         answer[j] = ''.join(answer[j])
#     return answer

# def solution(n, arr1, arr2):
#     answer = []
#     modular_arr1 = []
#     modular_arr2 = []
#     for i in range(n):
#         modular_arr1.append([])
#         modular_arr2.append([])

#         modular_arr1[i] = format( arr1[i], 'b')
#         while len( modular_arr1[i] ) != n:
#             modular_arr1[i] = '0' + modular_arr1[i]
        
#         modular_arr2[i] = format( arr2[i], 'b')
#         while len( modular_arr2[i] ) != n:
#             modular_arr2[i] = '0' + modular_arr2[i]

#     for j in range( len(modular_arr1) ) :
#         answer.append([])
#         for i in range(n):
#             answer[j].append( str( int(modular_arr1[j][i]) | int(modular_arr2[j][i]) ) ) 
#         answer[j] = ''.join(answer[j])
#         answer[j] = answer[j].replace('0',' ')
#         answer[j] = answer[j].replace('1','#')
            
    # return answer

# def solution(n, arr1, arr2):
#     answer = []
#     for i in range(n):
#         answer.append([[],[]])

#         # 각각의 배열의 숫자를 2진수로 바꾼 뒤( foramt(,'b') )
#         # 해당 숫자를 .zfill() 하여 요구하는 자리수에 맞는 숫자로 변형합니다.
#         answer[i][0], answer[i][1] = format( arr1[i], 'b').zfill(n), format( arr2[i], 'b').zfill(n)

#         # 변경된 숫자 두개를 or 연산처럼 계산하여 ' ' 또는 '#'을 이용한 리스트로 만듭니다.
#         tmp = [' ' if a=='0' and b=='0' else '#' for a,b in zip(answer[i][0], answer[i][1]) ] 

#         # 각 ' '와 '#'를 연결해 비밀지도를 만듭니다.
#         answer[i] = ''.join(tmp)
            
#     return answer

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 두 숫자를 or 연산한 후, 2진수로 변경합니다.
        # 후에 zfill()함수를 이용해 요구하는 자리수에 맞춥니다.
        answer.append( format( (arr1[i] | arr2[i]), 'b').zfill(n) )
        
        # 나온 숫자가 0이라면 ' '를, 1이라면 '#'으로 변경해 리스트로 만듭니다.
        answer[i] = answer[i].replace('0',' ').replace('1','#')
            
    return answer

print( solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]) )
print( solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]) )

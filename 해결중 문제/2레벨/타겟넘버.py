def solution(numbers, target):
    start = ''

    # 리스트 절반의 합보다 결과값이 낮다면 +가 많도록 시작.
    # 아니라면 -가 많도록 시작.
    if sum(numbers[:len(numbers)//2]) < target:
        start = '+'
        end = '-'
    else:
        start = '-'
        end = '+'
    
    # 전부 더한 값으로 값 비교.
    # -를 하나씩 늘려감.


    answer = 0
    return answer


print( solution( [1, 1, 1, 1, 1], 3 ) )


# 모두 같은 값일 경우
# - 를 하나씩 늘려가며 정답값이 나오도록 만든다.
# +,-의 개수를 찾아서 조합 돌리기. nC(-개수 or + 개수)

# 아닐 경우 
# 동적 계획법? 모든 값에 +,-의 조합을 사용해서 구한다?
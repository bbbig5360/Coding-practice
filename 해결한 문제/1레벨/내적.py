
def solution(a, b):
    answer=0
    # 각 자리수에 맞는 숫자들을 곱한 후, 더한다.
    for i in range(len(a)):
        answer += a[i] * b[i]   
    return answer

    # 찾아보니 한줄로 끝내는 멋진 방법도 있었습니다.
    # 의외로 comprehension보다 위의 코드가 더 빨랐습니다.
    # return sum( [ x*y for x,y in zip(a,b)] )

print( solution( [1,2,3,4], [-3,-1,0,2] ) )
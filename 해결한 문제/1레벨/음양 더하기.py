# def solution(absolutes, signs):
#     answer = 0
#     for num,sig in zip(absolutes, signs):
#         if not sig:
#             num = -num
#         answer += num
#     return answer

def solution(absolutes, signs):
    # signs가 False일 때, -로 바꿔서 저장한 리스트를 만듭니다. 후에 각 리스트를 더해줍니다.
    answer = sum([ num if sig else -num for num,sig in zip(absolutes,signs) ])
    return answer



print( solution([4,7,12],[True,False,True]) )
print( solution([1,2,3],[False,False,True]) )
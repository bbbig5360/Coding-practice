
def solution(board, moves):
    answer = 0
    stack = []

    for i in range(len(moves)):
        catch = moves[i]

        for i in range(len(board)):
            if board[i][catch-1] != 0:
                stack.append(board[i][catch-1])
                board[i][catch-1] = 0

                if(len(stack) > 1):
                    if stack[-1] == stack[-2]:
                        answer += 2
                        stack.pop()
                        stack.pop()
                break
    return answer

print( solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) )


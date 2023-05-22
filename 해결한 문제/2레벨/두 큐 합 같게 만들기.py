from collections import deque

def false_check(q1, q2):
    flag = True
    
    total_sum = (sum(q1)+sum(q2))
    if total_sum % 2 == 1:
        flag = False
        
    total_sum_half = total_sum // 2
    if total_sum_half < max(q1) or total_sum_half < max(q2):
        flag = False
    
    return flag

def solution(queue1, queue2):
    answer = 0
    while_flag = false_check(queue1, queue2)
    
    queue1, queue2 = deque(queue1), deque(queue2)
    if while_flag == False:
        return -1
    
    limit = (len(queue1) + len(queue2)) * 10
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    # sum을 반복하지 않게 여기서 + -
        
    while while_flag:
        # print( answer, queue1,queue2,sum_q1, sum_q2)
        if sum_q1 == sum_q2:
            break
        elif sum_q1 > sum_q2:
            q_pop = queue1.popleft()
            queue2.append(q_pop)
            sum_q1 -= q_pop
            sum_q2 += q_pop            
        else:
            q_pop = queue2.popleft()
            queue1.append(q_pop)
            sum_q1 += q_pop
            sum_q2 -= q_pop
        
        if answer > limit:
            return -1
        answer += 1
    return answer
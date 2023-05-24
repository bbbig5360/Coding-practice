from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    d_index = n
    p_index = n
        
    d_deque = deque(deliveries)
    p_deque = deque(pickups)    

    if sum(deliveries) == 0 and sum(pickups) == 0:
        return answer
    
    while d_index != 0 or p_index != 0:
        # print('d_index= ',d_index)
        # print('p_index= ',p_index)
        
        dist = 0
        
        tmp_cap = cap
        while d_index > 0:
            if dist < d_index:
                dist = d_index    
                
            get_val = d_deque.pop()
            d_index -= 1
            if get_val == 0:
                continue        
            
            if tmp_cap - get_val >= 0:
                tmp_cap -= get_val
            else:
                get_val -= tmp_cap
                d_deque.append(get_val)
                d_index += 1
                break
        
        tmp_cap = cap 
        while p_index > 0:
            if dist < p_index:
                dist = p_index           
                
            get_val = p_deque.pop()
            p_index -= 1 
            if get_val == 0:
                continue
            
            if tmp_cap - get_val >= 0:
                tmp_cap -= get_val
            else:
                get_val -= tmp_cap
                p_deque.append(get_val)
                p_index += 1
                break
                    
        # print(d_deque)
        # print(p_deque)
        # print('d_sum= ',d_sum)
        # print('p_sum= ',p_sum)
        # print('dist =',dist)
        answer += dist*2    
    return answer
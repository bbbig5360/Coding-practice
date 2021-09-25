from collections import deque

num_cordinate = { 1:(0, 0), 2:(0, 1), 3:(0, 2), 4:(1, 0), 5:(1, 1), 6:(1, 2), 7:(2, 0), 8:(2, 1), 9:(2, 2), 10:(3,0), 0:(3, 1), 11:(3,2) }

def cordinate_distance(left, right):
    left_cord = num_cordinate[left]
    right_cord = num_cordinate[right]
    return abs(left_cord[0] - right_cord[0]) + abs(left_cord[1] - right_cord[1])

def solution(numbers, hand):
    answer = ''
    curr_left = 10
    curr_right = 11

    left_right_dict = {'left':'L', 'right':'R'}
    
    curr_hand = ''

    for number in numbers:
        input_button = number

        if input_button in [1,4,7]:
            curr_hand = 'left'
        elif input_button in [3,6,9]:
            curr_hand = 'right'

        else:
            distance_cordinate = cordinate_distance(curr_left, input_button) - cordinate_distance(curr_right, input_button)
            if distance_cordinate > 0:
                curr_hand = 'right'
            elif distance_cordinate < 0:
                curr_hand = 'left'
            else:
                curr_hand = hand
            
        answer += left_right_dict[curr_hand]

        if left_right_dict[curr_hand] == 'L':
            curr_left = input_button
        else:
            curr_right = input_button

    return answer


print( solution( [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left' ) )
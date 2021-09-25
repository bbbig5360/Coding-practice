def solution(s):
    answer = s

    try:
        answer = int(answer)
    except:
        dict_num = {'zero':'0','one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

        for num_str,value in dict_num.items():
            if num_str in answer:
                answer = answer.replace( num_str, value )
        answer = int(answer)

    return answer

print(solution('one4seveneight'))
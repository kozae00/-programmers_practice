def solution(angle):
    answer = 0
    
    if angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90<angle<180:
        answer = 3
    elif angle>= 180:
        answer = 4
    
    return  answer


""" def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer """

## if문이 아닌 answer값을 지정해 angle이 주어진 값에 따라
# 연산 후 1,2,3,4 리턴값을 출력함 
def solution(quiz):
    
    answer = []
    
    for i in quiz:
        a, b = i.split('=')
        a = a.split()
        
        # '+', '-' else를 분리하지 않고 묶어서 표현하게 된다면                                       
        # 연산자가 양수 음수 연산과정에서 (음수 + 음수) 식에서 양수로 판정이되어 오류가 나올 수 있다.
        if a[1] == '+' :
            if int(a[0]) + int(a[2]) == int(b):
                answer.append('O')
            else :
                answer.append('X')
        elif a[1] == '-' : 
            if int(a[0]) - int(a[2]) == int(b):
                answer.append('O')
            else :
                answer.append('X') 

    return answer
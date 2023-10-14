def solution(A,B):
    answer = 0
    A.sort(reverse = True) #A를 내림차순
    B.sort()               #B를 오음차순

    for i in range(len(A)):
        answer += (A[i]*B[i])

    return answer

#요구사항 분석
#길이가 같은 A,B
#A,B 각각 하나의 인덱스 값을 구해
#최소의 곱 값을 도출해야한다
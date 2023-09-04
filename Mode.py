def solution(array):
    
    count = [0] * (max(array)+1) #숫자 출연 횟수 리스트

    for i in array:
        count[i] += 1
        
    m = 0 #최빈값의 개수
    for c in count:
        if c == max(count):
            m += 1
    
    if m>1: #최빈값이 2개 이상이면 -1 리턴
        return -1
    
    else: #최빈값이 1개면 해당 숫자 리턴
        return count.index(max(count))
    

## enumerate를 이용해 해결

""" def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1 """

""" enumerate는 인덱스와 요소를 같이 반환하므로 위 코드에서 i는 인덱스, a가 요소가 된다.
set(array)의 요소(a)를 지워가는 과정을 반복한다.
array = [1, 2, 3, 3, 3, 4] 이면 set(array)는 (1, 2, 3, 4) 이다.
enumerate는 인덱스와 요소를 같이 반환하므로 위 코드에서 i는 인덱스, a가 요소가 된다.
i=0, a=1 → array에서 a(= 1) 제거 → array [2, 3, 3, 3, 4]
i=1, a=2 → array에서 a(= 2) 제거 → array [3, 3, 3, 4]
i=2, a=3 → array에서 a(= 3) 제거 → array [3, 3, 4]
i=3, a=4 → array에서 a(= 4) 제거 → array [3, 3]
그럼 현재 i는 3이므로 if 조건문이 참이 아니고, array의 길이도 0이 아니므로 다시 for문을 반복한다. """
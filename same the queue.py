#solution   
def solution(queue1, queue2):
    _sum = (sum(queue1) + sum(queue2)) // 2
    if (max(queue1 + queue2) > _sum) : return -1
    answer, start1, start2 = 0, 0, 0
    end1, end2 = len(queue1) - 1, len(queue1) - 1
    lst1 = queue1 + queue2 + queue1
    lst2 = queue2 + queue1 + queue2
    sum1, sum2 = sum(queue1), sum(queue2)
    while sum1 != _sum and sum2 != _sum :
        if sum1 < _sum :
            end1 += 1
            if end1 == len(lst1) : return -1
            sum1 += lst1[end1]
        else :
            sum1 -= lst1[start1]
            start1 += 1
        if sum2 < _sum :
            end2 += 1
            if end2 == len(lst2) : return -1
            sum2 += lst2[end2]
        else :
            sum2 -= lst2[start2]
            start2 += 1
        answer += 1
    return answer

## 실행시간 초과원인 분석
## total_queue %2를 활용해서 홀짝여부를 확인하는데 발생하는 문제점 분석


""" def solution(queue1, queue2):
    A=[]
    B=[]
    queue1.reverse()
    queue2.reverse()
    total_queue = queue1+queue2
    total_queue.sort()
    
    for i in range(0, len(total_queue)):
        # -1 과 0구분
        if sum(A) == sum(B):
            A.append(total_queue.pop())
        elif sum(A) < sum(B):
            A.append(total_queue.pop())
        else:
            B.append(total_queue.pop())
    
        
    if sum(A) != sum(B):
        return -1
    else:
        answer=0
        while sum(queue1) != sum(queue2):
            if sum(queue1) > sum(queue2):
                queue2.insert(0, queue1.pop())
                answer+=1
            else:
                queue1.insert(0, queue2.pop())
                answer+=1
        return answer """
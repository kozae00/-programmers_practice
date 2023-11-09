def solution(arr1, arr2):
    answer = []
    m, n, r = len(arr1), len(arr1[0]), len(arr2[0])
    
    for i in range(m):
        arr = arr1[i]
        result = []    
    
        for j in range(r):
            hap = 0
            for k in range(n):
                hap += arr[k] * arr2[k][j]
            result.append(hap)
        answer.append(result)

    return answer

# arr1에서 하나의 행을 가져와 arr로 저장한 후, 
# arr2의 하나의 열과 곱해 hap을 구하고 
# 이 hap들을 하나의 행에 대한 곱셈 결과인 result에 추가한다.
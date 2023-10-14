def solution(s):
    nums = list(map(int, s.split()))
    #문자열 s를 공백을 기준으로 분할해 리스트로 만듬. 
    #map 함수를 사용하여 각 요소를 정수로 변환합니다. 
    #이를 다시 리스트로 변환하여 nums에 저장합니다.
    
    min_num = str(min(nums))
    max_num = str(max(nums))
    return min_num + " " + max_num



#요구사항
#문자열 s 숫자들이 저장
#최소값과 최대값을 출력
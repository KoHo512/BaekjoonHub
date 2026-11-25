def solution(clothes):
    answer = 1
    
    # [의상 이름, 의상 종류]
    # 종류 별 이름이 몇가지 있는지 파악
    category_count = {}
    
    for name, category in clothes:
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1
        
    # 각 종류 별로 입을 수 있는 경우의 수 계산
    for i in category_count.values():
        answer *= i + 1
    
    return answer - 1
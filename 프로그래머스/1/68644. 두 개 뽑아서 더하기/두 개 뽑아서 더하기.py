from itertools import combinations

def solution(numbers):
    answer = set()
    
    for nums in combinations(numbers, 2):
        answer.add(sum(nums))
        
    return sorted(answer)
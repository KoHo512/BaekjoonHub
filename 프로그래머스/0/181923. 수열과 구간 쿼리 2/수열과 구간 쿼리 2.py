def solution(arr, queries):
    answer = []
    
    for s, e, k in queries:
        for a in sorted(arr[s: e + 1]):
            if a > k:
                answer.append(a)
                break
        else:
            answer.append(-1)
        
    return answer
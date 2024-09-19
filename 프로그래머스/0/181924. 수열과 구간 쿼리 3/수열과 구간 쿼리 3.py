def solution(arr, queries):
    for query in queries:
        a = arr[query[0]]
        arr[query[0]] = arr[query[1]]
        arr[query[1]] = a
        
    return arr
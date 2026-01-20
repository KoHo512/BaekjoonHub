def solution(s, n):
    answer = ''
    
    for ss in s:
        if ss.isupper():
            answer += chr((ord(ss) - ord('A') + n) % 26 + ord('A'))
        elif ss.islower():
            answer += chr((ord(ss) - ord('a') + n) % 26 + ord('a'))
        else:
            answer += ss

    return answer
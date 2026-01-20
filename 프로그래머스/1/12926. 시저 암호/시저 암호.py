def solution(s, n):
    answer = ''
    
    for ss in s:
        if ord(ss) in range(65, 91):
            if ord(ss) + n < 91:
                answer += chr(ord(ss) + n)
            else:
                answer += chr(ord(ss) + n - 26)
        elif ord(ss) in range(97, 123):
            if ord(ss) + n < 123:
                answer += chr(ord(ss) + n)
            else:
                answer += chr(ord(ss) + n - 26)
        else:
            answer += ss

    return answer
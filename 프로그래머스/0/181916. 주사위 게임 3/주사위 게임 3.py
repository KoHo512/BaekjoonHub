def solution(a, b, c, d):
    a, b, c, d = sorted([a, b, c, d])
    
    if a == d:
        return 1111 * a
    
    if a == c:
        return (10 * a + d)**2
    
    if b == d:
        return (10 * d + a)**2

    if a == b and c == d:
        return (a + d) * (d - a)
    
    if a == b:
        return c * d
    
    if b == c:
        return a * d
    
    if c == d:
        return a * b
    
    return a
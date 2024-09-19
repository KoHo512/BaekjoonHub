def solution(num_list):
    mul = 1
    sum_square = sum(num_list) ** 2
    
    for i in num_list:
        mul = mul * i
    
    if mul < sum_square:
        return 1
    else:
        return 0
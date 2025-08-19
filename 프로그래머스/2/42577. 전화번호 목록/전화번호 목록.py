def solution(phone_book):
    phone_book = sorted(set(phone_book))
    
    for i in range(len(phone_book) - 1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
            
    return True

#     phone_book.sort()
    
#     for i in range(len(phone_book)):
#         for j in range(i + 1, len(phone_book)):
#             if phone_book[i][0] != phone_book[j][0]:
#                 pass
            
#             if phone_book[i] == phone_book[j][:len(phone_book[i])]:
#                 return False            
    
#     return True
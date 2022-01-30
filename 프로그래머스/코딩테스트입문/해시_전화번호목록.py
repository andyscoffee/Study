def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if len(phone_book[i]) < len(phone_book[i+1]):
            if phone_book[i+1].find(phone_book[i]) == 0:
                return False

    return answer

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))

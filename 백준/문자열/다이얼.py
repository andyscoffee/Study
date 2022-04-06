# 5622 무슨 이런 정신병자 할머니가 다있음;

s = input()
total = 0

for l in s:
    if 65 <= ord(l) <= 67:
        total += 3
    elif 68 <= ord(l) <= 70:
        total += 4
    elif 71 <= ord(l) <= 73:
        total += 5
    elif 74 <= ord(l) <= 76:
        total += 6
    elif 77 <= ord(l) <= 79:
        total += 7
    elif 80 <= ord(l) <= 83:
        total += 8
    elif 84 <= ord(l) <= 86:
        total += 9
    elif 87 <= ord(l) <= 90:
        total += 10

print(total)

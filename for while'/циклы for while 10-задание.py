# Найти все простые числа от 2 до 50.
lst = []
for i in range(2, 51):
    simple = True
    for j in range(2, i):
        if i % j == 0:
            simple = False
            break
    if simple:
            lst.append(i)

print(*lst)

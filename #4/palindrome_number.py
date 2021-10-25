pali = []
for i in range(999, 99, -1):
    if i % 10 == 0:
        continue
    for n in range(i, 99, -1):
        number = str(i * n)
        if number == number[::-1]:
            pali.append(int(number))
print(max(pali))
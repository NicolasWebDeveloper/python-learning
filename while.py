i = 0

while i < 10:
    if i == 5:
        i += 1
        continue

    if i == 9:
        break
    print(i)
    i += 1
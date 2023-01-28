


# P P P F

adres = [192, 168, 10, 128]
maska = [255, 255, 255, 0]

for a, m in zip(adres, maska):

    print((a & m), end='.')


# SQL F P P F
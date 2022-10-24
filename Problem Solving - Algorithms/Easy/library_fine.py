from datetime import date

d1, m1, y1 = 1, 1, 2001
d2, m2, y2 = 1, 1, 2000

if (date(y2, m2, d2) - date(y1, m1, d1)).days >= 0:
    print(0)

else:
    print((15 * (d1 - d2) if m1 == m2 else 500 * (m1 - m2)) if y1 == y2 else 10000)

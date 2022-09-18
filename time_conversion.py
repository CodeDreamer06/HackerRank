s = '12:05:45AM'
h = int(s[:2])
# Re
print(
    f'{str((0 if h == 12 else 12 if s[-2] == "P" else 0) + (0 if h == 12 else 12 if s[-2] == "A" else h)).zfill(2)}{s[2:-2]}')

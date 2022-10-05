s = '12:05:45AM'
h = int(s[:2])

print(f'{str((h + 12 if h < 12 and s[-2] == "P" else 0 if s[-2] == "A" and h == 12 else h)).zfill(2)}{s[2:-2]}')
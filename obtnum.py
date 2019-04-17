str = "h3110 23 cat 444.4 rabbit 11 2 dog"
par = [int(s) for s in str.split() if s.isdigit()]
print(str)
print(par)
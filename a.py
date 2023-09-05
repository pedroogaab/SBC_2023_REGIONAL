n, m = map(int, (input().split()))

alt = input().split()

cc = 0
for b in alt:
    if m >= int(b):
        cc += 1

print(cc)

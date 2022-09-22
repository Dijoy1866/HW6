N = int(input("Pleaes input :"))
i = N
d = '*'
s = N
p = ' '
print(d * i)
while s != 1:
    s -= 1
    i -= 1
    print(p * (N-i) + (d * i))
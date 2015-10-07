__author__ = 'rfischer'


n = input()
t = []
d = []
total = []

for i in range (0, n):
    tt, dd = raw_input().split()
    t.append(tt)
    d.append(dd)
    total.append((i + 1, int(tt) + int(dd)))

# print n, t, d
# print total
stotal =  sorted(total, key=lambda order: order[1])

for i in range (0, n):
    print stotal[i][0],

print
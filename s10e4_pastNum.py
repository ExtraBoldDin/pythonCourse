cin = map(int, input().split(' '))
seq = list(cin)

print('NO')
for xi in range(1, len(seq)):
    if seq[xi] in seq[:xi]:
        print('YES')
    else:
        print('NO')

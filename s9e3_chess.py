n, m = map(int, input().split(' '))

table = [['.' if xj%2 == 0 else '*' for xj in range(m)] if xi%2 == 0 else ['*' if xj%2 == 0 else '.' for xj in range(m)] for xi in range(n)]


for xi in table:
    print(' '.join(xi))

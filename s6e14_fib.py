n = int(input())

fib = [0, 1]

for xi in range(2, n+1):
    fib.append(fib[xi-1] + fib[xi-2])

print(fib[n])

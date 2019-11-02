cin = map(int, input().split(' '))
p = int(input())
seq = list(cin)

seq.append(p)
seq.sort()

print(len(seq)-seq.index(p))

num = int(input())

print('YES' if (num%4 == 0 and num%100 != 0) or num%400 == 0 else 'NO')
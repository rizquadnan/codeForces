n, m = input().split()
n = int(n)
m = int(m)

num_dominos = 0
if n == m:
    if n > 3:
        if n % 2 == 0:
            for i in range(int(n/2)):
                num_dominos += n
        else:
            for i in range(n // 2):
                num_dominos += n
            num_dominos += n // 2
    elif n > 2:
        num_dominos += n
        num_dominos += m % 2
    elif n == 2:
        num_dominos += n
    elif n < 2:
        num_dominos = 0
elif n > m:
    num_dominos += n
    if m > 3:
        if m % 2 == 0:
            for i in range((m // 2) - 1):
                num_dominos += n
        else:
            for i in range((m // 2) - 1):
                num_dominos += n
            num_dominos += n // 2
    elif m > 2:
        if n % 2 != 0:
            num_dominos += n // 2
        elif n % 2 == 0:
            num_dominos += n // 2
    elif m == 2:
        num_dominos += 0
    elif m == 1:
        num_dominos -= n
        num_dominos += n // 2
    elif m <= 0:
        num_dominos = 0        
elif m > n:
    num_dominos += m
    if n > 3:
        if n % 2 == 0:
            for i in range((n // 2) - 1):
                num_dominos += m
        else:
            for i in range((n // 2) - 1):
                num_dominos += m
            num_dominos += m // 2
    elif n > 2:
        if m % 2 != 0:
            num_dominos += m // 2
        elif m % 2 == 0:
            num_dominos += m // 2
    elif n == 2:
        num_dominos += 0
    elif n == 1:
        num_dominos -= m
        num_dominos += m // 2
    elif n <= 0:
        num_dominos = 0

print(num_dominos)

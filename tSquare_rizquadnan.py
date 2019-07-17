n, m, a = input().split()

from math import ceil
m = int(m)
n = int(n)
a = int(a)

if m % a == 0 and n % a == 0:
    jp = n / a
    jl = m / a
    j_flagstone = int(jp * jl)
elif m % a != 0 and n % a != 0:
    if m < a and n < a:
        j_flagstone = 1
    else:
        jp = ceil(n / a)
        jl = ceil(m / a)
        j_flagstone = int(jp * jl)
elif m % a != 0 and n % a == 0:
    jp = n / a
    jl = ceil(m / a)
    j_flagstone = int(jp * jl)
elif m % a == 0 and n % a != 0:
    jp = ceil(n / a)
    jl = m / a
    j_flagstone = int(jp * jl)

print(j_flagstone)


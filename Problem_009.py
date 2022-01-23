# special pythagorean triplet

import math
cond = 0
a = 1
while cond == 0:
    b = 1
    while b < 1000 and cond == 0:
        if (a + b + math.sqrt(a*a + b*b)) == 1000:
            ans = a*b*(1000-a-b)
            cond = 1
        else:
            b = b + 1
    a = a + 1

print(ans)
print(a - 1)
print(b)
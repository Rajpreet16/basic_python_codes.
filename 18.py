#Python Program that prints all real solutions to the quadratic equation ax2+bx+c = 0. Read in a, b, c and use the quadratic formula. If the discriminate b2-4ac is negative, display a message stating that there are no real solutions.

import cmath

a = int(input())
b = int(input())
c = int(input())

d = (b**2) - (4*a*c)
d1 = cmath.sqrt(d)
s1 = -b - (d1/(2*a))
s2 = -b + (d1/(2*a))

print(s1)
print(s2)

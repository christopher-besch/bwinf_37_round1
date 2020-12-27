from numpy import *
from scipy.optimize import *


def collide(a1, b1, c1, d1):
    global a, b, c, d
    a = a1
    b = b1
    c = c1
    d = d1
    z = fsolve(solve, array([1, 1]))

    if 0 < z[0] < 1 and 0 < z[1] < 1:
        return False
    else:
        return True


def solve(z):
    global a, b, c, d
    s = z[0]
    t = z[1]

    F = empty(2)
    F[0] = t*(a[0]-b[0])+s*(d[0]-c[0])-a[0]+c[0]
    F[1] = t*(a[1]-b[1])+s*(d[1]-c[1])-a[1]+c[1]
    return F


print(collide([1, 1], [1, 3], [1, 1], [1, 3]))

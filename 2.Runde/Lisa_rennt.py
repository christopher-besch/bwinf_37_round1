from numpy import *
from scipy.optimize import *


def my_function(z):
    x = z[0]
    y = z[1]

    F = empty(2)
    F[0] = pow(x, 2)+pow(y, 2)-20
    F[1] = y - pow(x, 2)
    return F


zGuess = array([1, 1])
z = fsolve(my_function, zGuess)
print(z)

from scipy.interpolate import BSpline
import numpy as np

class CardinalSpline:
    def __init__(self, n, h, k):
        self.k = k
        self.h = h
        self.n = n

    def __b(self, x, n):
        if n == 0:
            return 1.0 if (0 < x and x <=1) else 0.0
        else:
            return (x/n * self.__b(x, n-1) +
                (n+1-x)/n * self.__b(x-1, n-1))
         
    def __call__(self, x):
        return self.__b(x/self.h-self.k, self.n)

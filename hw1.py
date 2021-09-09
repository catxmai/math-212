#!/usr/bin/env python
# coding: utf-8

# problem 5
import math

p0 = 2.5
tol=10**-4

def f(x, tol ,max_n=80):
    i = 0
    err = 1
    
    while i < max_n and err > tol:
        r = (-10*math.cos(x))**(.5)
        err = abs(r-x)
        print(str(r) + " err :" + str(err))
        i += 1
        x = r
f(p0, tol)

# problem 5
import math

p0 = 2
tol=10**-4

def f(x, tol ,max_n=80):
    i = 0
    err = 1
    
    while i < max_n and err > tol:
        r = math.acos(-(x**2)/10)
        err = abs(r-x)
        print(str(r) + " err :" + str(err))
        i += 1
        x = r
f(p0, tol)


# problem 7
import math
def f(x):
    return (math.e**x) - (x**2) + (3*x) - 2

def secant_intercept(p0,p1):
    fp0 = f(p0)
    fp1 = f(p1)
    p2 = p1 - fp1*((p1-p0)/(fp1-fp0))
    return p2

def false_pos(p0, p1, tol, max_n = 5000):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    
    while (i < max_n):
        p = secant_intercept(p0,p1)
        if abs(p-p0) < tol:
            print(f"p_{i} = {p}, err = {abs(p-p0)}")
            print(f"approximation achieved after {i} iterations")
            return
        
        q = f(p)
        print(f"p_{i} = {p}, err = {abs(p-p0)}")
        i += 1
        if q*q1 < 0:
            p0 = p1
            q0 = q1 
            p1 = p
            q1 = q
        else:
            p0 = p
            q0 = f(p)

    print(f"Method failed after {max_n} interations")

p0 = 0
p1 = 1
TOL = 10**(-3)
false_pos(p0,p1,TOL)







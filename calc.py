import sympy as sp

x = sp.symbols("x")

y = input("Input the x value for the function y = x: ")

for i in range(-5, 6):
    print(f"x = {i}: y = {y.subs(x, i)}")

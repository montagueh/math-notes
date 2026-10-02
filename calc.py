import sympy as sp

x = sp.symbols("x")

y = -2 * (x - 1) ** 2 + 3

for i in range(-5, 6):
    print(f"x = {i}: y = {y.subs(x, i)}")

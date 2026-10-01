import sympy as sp

t = sp.symbols("t")
h = 3 + 2 * sp.sin((t * sp.pi / 4) - sp.pi / 2)

for i in range(9):
    print("Height at", i, "seconds is: ", h.subs(t, i))

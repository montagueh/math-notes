import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

t = sp.symbols("t")
h = 3 - 2 * sp.cos(t * sp.pi / 8)

h_of_t = sp.lambdify(t, h, "numpy")

t_values = np.arange(9)  # 0-8
h_values = h_of_t(t_values)

i = 1
for i, hv in zip(t_values, h_values):
    print("At time: ", i)
    print(hv)

plt.plot(t_values, h_values, marker="o")
plt.xlabel("t")
plt.ylabel("h(t)")
plt.show()

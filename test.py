import matplotlib.pyplot as plt
import numpy as np

# 1. Generate 100 points for x between -10 and 10
x = np.linspace(-10, 10, 100)

# 2. Calculate y = x^2
y = x**2

# 3. Create the plot
plt.figure(figsize=(6, 4))
plt.plot(x, y, color="blue", label="$y = x^2$")

# 4. Add titles and grid
plt.title("Plot of $y = x^2$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# 5. Show the graph
plt.show()

import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(12, 6))             # Create a figure containing a single Axes.

fig.suptitle("Figure Suptitle")

ax1.set_title("First axis title")
ax1.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
ax1.plot([2, 5, 6, 7], [2, 5, 4, 5])  # Plot some data on the Axes.
ax1.set_xlabel("$x$")
ax1.set_ylabel("$y$")

ax2.set_title("Second axis title")
x = np.random.randint(10, size=10)
y = np.random.randint(10, size=10)
ax2.plot(x,y)  # Plot some data on the Axes.
ax2.scatter(x,y)  # Plot some data on the Axes.

plt.show()

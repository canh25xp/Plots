import matplotlib.pyplot as plt
from plot_utils import Save_fig

# Coordinates of the points
points = [(0, 0.6561), (1, 0.2916), (2, 0.0486), (3, 0.0036), (4, 0.0001)]

# Separate the coordinates into two lists: x and y
xs, ys = zip(*points)

# Create the plot
fig, ax = plt.subplots()

# Move the left and bottom spines to x = 0 and y = 0, respectively.
ax.spines[["left", "bottom"]].set_position(("data", 0))
# Hide the top and right spines.
ax.spines[["top", "right"]].set_visible(False)

# Draw arrows (as black triangles: ">k"/"^k") at the end of the axes.
# In each case, one of the coordinates (0) is a data coordinate
# (i.e., y = 0 or x = 0, respectively)
# and the other one (1) is an axes coordinate
# (i.e., at the very right/top of the axes).
# Also, disable clipping as the marker actually spills out of the Axes.
ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)

ax.scatter(xs, ys, color='blue')

# Annotate each point with its coordinates
for (x, y) in points[3:]:
    ax.annotate(f'{y}', (x, y), textcoords="offset points", xytext=(0,5), ha='center')

# Draw dotted lines to the x and y axes for each point
for (x, y) in points[1:3]:
    ax.plot([x, x], [0, y], "k--", alpha=0.5)
    ax.plot([0, x], [y, y], "k--", alpha=0.5)

# Set the x and y limits
ax.set_xlim(-0.05, 4.5)
ax.set_ylim(-0.01, 0.7)

# Draw xy ticks
ax.set_xticks(xs[1:])
ax.set_yticks(ys[:3])

# Set custom x and y axis labels at the tip of the arrows
ax.annotate('$x$', xy=(4.5, 0), xytext=(20, 0), textcoords='offset points', ha='center', va='center')
ax.annotate('$p_X(x)$', xy=(0, 0.7), xytext=(0, 20), textcoords='offset points', ha='center', va='center')
# ax.set_xlabel("$x$")
# ax.set_ylabel("$p_X(x)$")

# Annotate the origin label
ax.annotate('0', xy=(0, 0), xytext=(-10, -10), textcoords='offset points', ha='center', va='center')

# Add grid lines
# ax.grid(True)

# Save_fig(fig, "template.eps")

# Display the plot
plt.show()

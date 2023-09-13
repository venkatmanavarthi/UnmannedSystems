import matplotlib.pyplot as plt
import numpy as np

# function to compute index for each x and y
def compute_index(min_x, max_x, min_y, max_y, grid_spacing, cx, cy) -> int:

    index = ((cx - min_x)/grid_spacing) + \
            (((cy - min_y)/grid_spacing) * \
            (((max_x + grid_spacing)-min_x)/grid_spacing))

    return int(index)
    

# step
grid_spacing = 0.5

# X
min_x = 0
max_x = 10

# Y
min_y = 0
max_y = 10

x_values = np.arange(min_x, max_x + grid_spacing, grid_spacing)
y_values = np.arange(min_y, max_y + grid_spacing, grid_spacing)

for y in y_values:
    for x in x_values:
        index = compute_index(min_x, max_x, min_y, max_y, grid_spacing, x, y)
        plt.text(x, y, str(index), color='red', fontsize=8, ha='center', va='center')

plt.xlim(min_x - grid_spacing, max_x + grid_spacing)
plt.ylim(min_y - grid_spacing, max_y + grid_spacing)
plt.title("Problem 4")
plt.show()
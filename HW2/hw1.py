class Node:
    def __init__(self, x, y, cost=0, parent_index=-1, g_cost=0, h_cost=0):
        self.x = x
        self.y = y
        self.parent_index = parent_index
        self.cost = cost
        self.g_cost = g_cost
        self.h_cost = h_cost

def compute_index(min_x, max_x, min_y, max_y, grid_spacing, cx, cy) -> int:

    index = ((cx - min_x)/grid_spacing) + \
            (((cy - min_y)/grid_spacing) * \
            (((max_x + grid_spacing)-min_x)/grid_spacing))

    return int(index)

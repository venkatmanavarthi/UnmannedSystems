class Node:
    def __init__(self, x, y, cost, parent_index):
        self.x = x
        self.y = y
        self.parent_index = parent_index
        self.cost = cost

def compute_index(min_x, max_x, min_y, max_y, grid_spacing, cx, cy) -> int:

    index = ((cx - min_x)/grid_spacing) + \
            (((cy - min_y)/grid_spacing) * \
            (((max_x + grid_spacing)-min_x)/grid_spacing))

    return int(index)

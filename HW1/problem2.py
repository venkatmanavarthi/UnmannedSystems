class node:
    def __init__(self, x, y, parent_cost, index):
        self.x = x
        self.y = y
        self.parent_cost = parent_cost
        self.index = index


root_node = node(1, 2, 1, 1)
print(root_node.__dict__)
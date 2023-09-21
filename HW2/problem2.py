from .problem1 import calculate_distance
import matplotlib.pyplot as plt

class Obstacle:
    def __init__(self, x, y, radius=0) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    def is_inside(self, cur_x, cur_y, r_radius=0.2) -> bool:
        """
        Args:
          cur_x: X position of the robot
          cur_y: Y potition of the robot
          r_radius: Robot radius

        Returns:
          True if point is inside the obstacle
          False if point is outside the obstacle
        """ 
        dis = calculate_distance(cur_x, cur_y, self.x, self.y)
        if dis > (self.radius + r_radius):
            return False
        return True


def is_valid(obs, x_min, y_min, x_max, y_max, cur_x, cur_y, r_radius=0) -> bool:
    """
    Args:
        obs: List of Obstacles
        x_min: Grid Bounds
        y_min: Grid Bounds
        x_max: Grid Bounds
        y_max: Grid Bounds
        cur_x: X position of the robot
        cur_y: Y potition of the robot
        r_radius: Robot radius

    Returns:
        True if point is a valid location
        False if point is a invalid location
    """
    for each_obs in obs:
        if each_obs.is_inside(cur_x, cur_y, r_radius):
            return False
        
    if x_min > cur_x:
        return False
    if x_max < cur_x:
        return False
    if y_min > cur_y:
        return False
    if y_max < cur_y:
        return False
    
    return True


if __name__ == "__main__":
    obs_pos = [(1, 1), (4, 4), (3, 4), (5, 0), (5, 1),
               (0, 7), (1, 7), (2, 7), (3, 7)]
    obs_radius = 0.25
    r_radius = 0.25
    
    cur_x, cur_y = 2, 2
    
    obs_list = [Obstacle(each_ob[0], each_ob[1], obs_radius)
                for each_ob in obs_pos]
    x_min, y_min, x_max, y_max = 0, 0, 10, 10
    if is_valid(obs_list, x_min, y_min, x_max, y_max, cur_x, cur_y, r_radius):
        print("Valid Location")
    else:
        print("Invalid Location")
    
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)    
    for obs in obs_list:
        obs_plot = plt.Circle((obs.x, obs.y), obs.radius, color='blue')
        ax.add_patch(obs_plot)
    
    agent_plot = plt.Circle((cur_x, cur_y), r_radius, color='red')
    ax.add_patch(agent_plot)
    plt.title("Problem 2")
    plt.show()

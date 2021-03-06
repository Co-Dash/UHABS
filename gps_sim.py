import numpy as np

# Fixed propulsion of the craft 10 m/s
PROPULSION = 10

# Spatial resolution of the currents map 100 m
GRID_RESOLUTION = 100

# Ten second timesteps
TIMESTEP = 10


def caluclate_position(currents_map, bearing, position):
    # Code here
    """
    Calculates position based off currents map, bearing, and propulsion of the module
    :param currents_map: u(y, x), v(y, x) 2Dd component arrays for current values; np.dstack
    :param position: (y, x) present position of module; tuple
    :param bearing: angle defined from East for module heading; float
    :return: (y, x) new position of module; tuple
    """
    # Grab module position in grid
    n, m = position

    # Grab v and u arrays from current maps
    v_array = currents_map[::, ::, 0]
    u_array = currents_map[::, ::, 1]

    # Calculate velocity components of module
    boat_x_velocity = PROPULSION * np.cos(bearing)
    boat_y_velocity = PROPULSION * np.sin(bearing)

    # Calculate new position of module
    new_position = [n + (v_array[n] + boat_y_velocity) * timestep,
                    m + (u_array[m] + boat_x_velocity) * timestep]

    # Round values of position tuple to fix to a grid vertex
    new_position = np.rint(new_position)

    return new_position


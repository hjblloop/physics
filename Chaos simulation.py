import matplotlib.pyplot as plt
import numpy as np
import random
from matplotlib.animation import FuncAnimation

num_points = 100
left_side_width = 0.5
velocity = 0.05
initial_positions = np.random.rand(num_points, 2) 
initial_positions[:, 0] *= left_side_width # Random initial 2D coordinates on left side
velocity = np.random.rand(num_points, 2) * random.uniform(-1*velocity,velocity)  # Random velocities
time_steps = 1000

# Initialize position array
positions = np.zeros((time_steps, num_points, 2))
positions[0] = initial_positions

# Simulation loop
for t in range(1, time_steps):
    positions[t] = positions[t - 1] + velocity
    
    for i in range(num_points):
        if positions[t, i, 0] < 0:
            velocity[i, 0] *= -1
            positions[t, i, 0] = 0
        elif positions[t, i, 0] > 1:
            velocity[i, 0] *= -1
            positions[t, i, 1] = 1
        elif positions[t, i, 1] < 0:
            velocity[i, 1] *= -1
            positions[t, i, 1] = 0
        elif positions[t, i, 1] > 1:
            velocity[i, 1] *= -1
            positions[t, i, 1] = 1

# Create the initial plot
fig, ax = plt.subplots()
scatter = ax.scatter(initial_positions[:, 0], initial_positions[:, 1], label='Points')

# Update function for animation
def update(frame):
    scatter.set_offsets(positions[frame])
    ax.set_title(f"Point Movement over Time (Step {frame + 1}/{time_steps})")
    return scatter,

# Animation
ani = FuncAnimation(fig, update, frames=time_steps, blit=True)
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.ylim(0,1)
plt.xlim(0,1)
plt.legend()
plt.show()
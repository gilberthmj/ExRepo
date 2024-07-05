import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def draw_cube(ax, position, colors, edge_color='k'):
    # Define a single cube data
    r = [0, 1]
    for s, e in combinations(np.array(list(product(r, r, r))), 2):
        if np.sum(np.abs(s-e)) == r[1]-r[0]:
            ax.plot3D(*zip(s+position, e+position), color=edge_color)
    
    # Draw the faces
    face_idx = [
        [4, 5, 7, 6], # Top face
        [0, 1, 3, 2], # Bottom face
        [1, 3, 7, 5], # Right face
        [0, 2, 6, 4], # Left face
        [2, 3, 7, 6], # Front face
        [0, 1, 5, 4]  # Back face
    ]
    face_color = [colors[i] for i in range(6)]
    
    for idxs, color in zip(face_idx, face_color):
        sq = [[s+position] for s in [r[i] for i in idxs]]
        x, y, z = zip(*sq)
        ax.add_collection3d(Poly3DCollection([list(zip(x, y, z))], facecolor=color))

def plot_cubes(cube1, cube2):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    draw_cube(ax, [0, 0, 0], cube1, edge_color='k')
    draw_cube(ax, [1.5, 0, 0], cube2, edge_color='k')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    ax.set_xlim([-1, 3])
    ax.set_ylim([-1, 3])
    ax.set_zlim([-1, 3])

    plt.show()

# Colors for each face of the cube
colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']
cube_initial = colors
rotations = (1, 2, 1)  # Example rotations
cube_final = apply_rotations(rotations, cube_initial)

plot_cubes(cube_initial, cube_final)

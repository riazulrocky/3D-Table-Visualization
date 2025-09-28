import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Table leg
def create_leg_vertices(x, y, z, width=0.1, depth=0.1, height=1.0):
    return np.array([
        [x, y, z, 1],
        [x + width, y, z, 1],
        [x + width, y + depth, z, 1],
        [x, y + depth, z, 1],
        [x, y, z + height, 1],
        [x + width, y, z + height, 1],
        [x + width, y + depth, z + height, 1],
        [x, y + depth, z + height, 1]
    ])

# Table top
def create_top_vertices(x, y, z, width=1.2, depth=0.8, height=0.1):
    return np.array([
        [x, y, z, 1],
        [x + width, y, z, 1],
        [x + width, y + depth, z, 1],
        [x, y + depth, z, 1],
        [x, y, z + height, 1],
        [x + width, y, z + height, 1],
        [x + width, y + depth, z + height, 1],
        [x, y + depth, z + height, 1]
    ])

# Faces for cuboids
component_faces = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [0, 1, 5, 4],
    [2, 3, 7, 6],
    [1, 2, 6, 5],
    [0, 3, 7, 4]
]

# Create table components
leg1 = create_leg_vertices(0.1, 0.1, 0, height=1.0)
leg2 = create_leg_vertices(1.0, 0.1, 0, height=1.0)
leg3 = create_leg_vertices(0.1, 0.7, 0, height=1.0)
leg4 = create_leg_vertices(1.0, 0.7, 0, height=1.0)
tabletop = create_top_vertices(0, 0, 1.0, 1.2, 0.8, 0.1)

table_components = [leg1, leg2, leg3, leg4, tabletop]

# Draw function
def draw_object(ax, components, faces, colors=None, alpha=0.8, edgecolor='black'):
    if colors is None:
        colors = ['#8B4513'] * len(components)
    for i, component in enumerate(components):
        for face in faces:
            square = [component[j][:3] for j in face]
            ax.add_collection3d(
                Poly3DCollection(
                    [square],
                    facecolors=colors[i],
                    linewidths=1,
                    edgecolors=edgecolor,
                    alpha=alpha
                )
            )

if __name__ == "__main__":
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    # Background wall
    X, Z = np.meshgrid(np.linspace(-2, 2, 2), np.linspace(0, 3, 2))
    Y = np.ones_like(X) * 2.5
    ax.plot_surface(X, Y, Z, color="lightblue", alpha=0.7)

    # Draw table
    table_colors = ['#8B4513', '#8B4513', '#8B4513', '#8B4513', '#A0522D']
    draw_object(ax, table_components, component_faces, colors=table_colors, alpha=0.9)

    ax.set_xlim([-2, 2])
    ax.set_ylim([-1, 2])
    ax.set_zlim([0, 3])
    ax.view_init(elev=20, azim=-70)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Table with Stable Wall Background')

    ax.grid(False)
    ax.set_box_aspect([1, 1, 1])
    plt.tight_layout()
    plt.show()
    fig.savefig("table_with_stable_wall.png", dpi=300)

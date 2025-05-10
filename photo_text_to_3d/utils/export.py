import trimesh
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import os

def save_and_visualize(mesh, filename="outputs/model.obj"):

    os.makedirs(os.path.dirname(filename), exist_ok=True)


    mesh.export(filename)
    print(f"Model saved to {filename}")


    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.title("Preview of 3D Model")
    plt.show()

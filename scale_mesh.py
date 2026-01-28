import trimesh
import numpy as np
import argparse

def scale_vertices(vertices):
    bounds = np.array([vertices.min(axis=0), vertices.max(axis=0)])
    center = (bounds[0] + bounds[1]) / 2
    vertices_norm = (vertices - center[None, :])
    vertices_norm = vertices_norm / np.abs(vertices_norm).max() * 0.9995
    return vertices_norm

def scale_mesh(input_mesh_path, output_mesh_path):
    """
    Scales a 3D mesh by a given factor and saves the result.

    Args:
        input_mesh_path (str): Path to the input mesh file.
        output_mesh_path (str): Path to save the scaled mesh file.
        scale_factor (float): Factor by which to scale the mesh.
    """
    # Load the mesh
    mesh = trimesh.load(input_mesh_path)
    # Scale the vertices
    mesh.vertices = scale_vertices(mesh.vertices)
    # Save the scaled mesh
    mesh.export(output_mesh_path)

if __name__ == "__main__":
    

    parser = argparse.ArgumentParser(description="Scale a 3D mesh.")
    parser.add_argument("--input_mesh", type=str, help="Path to the input mesh file.")
    parser.add_argument("--output_mesh", type=str, help="Path to save the scaled mesh file.")

    args = parser.parse_args()

    scale_mesh(args.input_mesh, args.output_mesh)
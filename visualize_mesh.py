import argparse
import trimesh

def visualize_mesh(mesh_path):
    """Load and visualize a mesh file."""
    print(f"Loading mesh from: {mesh_path}")
    
    # Load the mesh
    mesh = trimesh.load(mesh_path)
    
    # Print mesh info
    print(f"Vertices: {len(mesh.vertices)}")
    print(f"Faces: {len(mesh.faces)}")
    print(f"Bounds: {mesh.bounds}")
    
    # Visualize
    print("Opening visualization window...")
    mesh.show()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize a 3D mesh file")
    parser.add_argument("--mesh", type=str, required=True, help="Path to the mesh file (.obj, .ply, etc.)")
    
    args = parser.parse_args()
    visualize_mesh(args.mesh)

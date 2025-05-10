import trimesh

def generate_from_text(prompt):
    print(f"Generating 3D model for prompt: {prompt}")

    if "car" in prompt.lower():
        mesh = trimesh.creation.box(extents=(2, 1, 0.5))
    elif "chair" in prompt.lower():
        mesh = trimesh.creation.box(extents=(1, 1, 2))
    else:
        mesh = trimesh.creation.icosphere(radius=1.0)

    return mesh

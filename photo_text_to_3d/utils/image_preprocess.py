from PIL import Image
import numpy as np
import trimesh
from rembg import remove
import io

def process_image(image_path):
   
    with open(image_path, "rb") as i:
        input_image = i.read()
    output_image = remove(input_image)

    
    with open("outputs/cleaned.png", "wb") as o:
        o.write(output_image)

   
    mesh = trimesh.creation.box(extents=(1, 1, 1))
    return mesh

import os
import sys
import argparse
from utils.image_preprocess import process_image
from utils.text_to_3d import generate_from_text
from utils.export import save_and_visualize


def main():
    parser = argparse.ArgumentParser(description="Convert photo or text to 3D model")
    parser.add_argument("--input", required=True, help="Path to image file or text prompt in quotes")
    parser.add_argument("--type", choices=["image", "text"], required=True, help="Type of input")
    args = parser.parse_args()

    if args.type == "image":
        mesh = process_image(args.input)
    else:
        mesh = generate_from_text(args.input)

    save_and_visualize(mesh)


if __name__ == "__main__":
    main()

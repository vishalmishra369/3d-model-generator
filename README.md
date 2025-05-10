# Photo or Text to 3D Model Converter

This project is a beginner-friendly prototype that converts either a photo (with a simple object) or a short text prompt into a basic 3D model (.obj). You can preview the model and download it for further use or 3D printing.

## 🧩 Features
- Accepts either an image file or text prompt.
- Removes background from image using `rembg`.
- Creates simple geometric 3D shapes (for demonstration purposes).
- Saves model as `.obj` and visualizes it using `matplotlib`.

## ✅ Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
```

## ▶️ How to Run

### For Text Input
```bash
python main.py --input "A small toy car" --type text
```

### For Image Input
```bash
python main.py --input path/to/image.jpg --type image
```

The generated 3D model will be saved in `outputs/model.obj` and a preview will pop up.

## 🧠 My Thought Process
- I chose `rembg` for image background removal because it's lightweight and works out-of-the-box.
- For text, I mapped keywords to simple geometric models using `trimesh` to simulate generation.
- I kept the structure modular and beginner-friendly.
- Advanced 3D recovery (like DreamFusion or Meshroom) was skipped to focus on clean code and simplicity.

## 📁 Project Structure
```
project/
├── main.py
├── utils/
│   ├── image_preprocess.py
│   ├── text_to_3d.py
│   └── export.py
├── outputs/
│   └── model.obj
├── requirements.txt
└── README.md
```

## 💡 Improvements Possible
- Integrate actual mesh recovery from images.
- Use real text-to-3D models like Shap-E or TripoSR.
- Support STL file export in addition to OBJ.

---
This prototype demonstrates the working logic with clear, readable code. Great for learning or further extension!

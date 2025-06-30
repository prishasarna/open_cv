# 🧠 Computer Vision Projects Suite

This repository contains a collection of computer vision scripts developed using Python and OpenCV. It includes utilities for face and eye detection, image classification, edge detection, image rotation, thresholding, and blurring. These scripts serve as foundational tools for experimenting with image processing and real-time webcam integrations.

---

## 📁 Project Structure

```
├── apples_banana/                      # Image dataset directory
├── edgedetection.py                    # Edge detection using Canny/Sobel filters
├── face_and_eyes.py                    # Real-time face and eye detection with webcam
├── faces.png                           # Sample image for testing
├── flask_proj.py                       # Flask app (work in progress)
├── haarcascade_eye.xml                 # Haar cascade for eye detection
├── haarcascade_frontalface_default.xml # Haar cascade for frontal face detection
├── image_basics.py                     # Basic OpenCV operations
├── image_classification.py            # Basic image classification experiment
├── imageblurring.py                   # Image blurring filters (Gaussian, Median, etc.)
├── open_cv1.py                         # Introductory OpenCV script
├── rotation.py                         # Image rotation functionality
├── thresholding.py                     # Binary and adaptive thresholding
├── tiger.jpg, trump-modi.jpg          # Sample test images
```

---

## 🚀 Features

- Real-time **face and eye detection** using Haar cascades
- **Edge detection** with Canny and Sobel operators
- **Image blurring** with different filtering techniques
- **Thresholding** methods including binary and adaptive
- **Image classification** prototype for dataset experimentation
- Base setup for a **Flask web interface** (under development)

---

## 🛠 Technologies Used

- Python 3
- OpenCV
- Flask (for future web integration)
- Haar Cascades (XML models)

---

## ▶️ Getting Started

### 1. Clone this repository
```bash
git clone https://github.com/prishasarna/open_cv.git
cd open_cv
```

### 2. Set up the environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # or use venv\Scripts\activate on Windows
pip install opencv-python flask
```

### 3. Run an example script
```bash
python face_and_eyes.py
```

---

## 🧪 Example Use Cases

- Test `face_and_eyes.py` with a webcam to detect faces in real time
- Use `edgedetection.py` to experiment with edge detection filters
- Explore `thresholding.py` for grayscale to binary conversions
- Run `image_classification.py` for basic dataset classification (if dataset is provided)

---

## 👤 Author

**Prisha Sarna**  
📧 [psarna@ualberta.ca](mailto:psarna@ualberta.ca)  
🔗 [LinkedIn](https://www.linkedin.com/in/prishasarna) | [GitHub](https://github.com/prishasarna) | [Portfolio](https://portfolio-jkivg69qy-prisha-sarnas-projects.vercel.app)

# YOLOv8 Safety Gear Detection

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-FF4B4B)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Detection-7D3C98)
![PyTorch](https://img.shields.io/badge/PyTorch-CPU-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Image_Processing-green)
![Ultralytics](https://img.shields.io/badge/Ultralytics-Library-yellow) 

Minimal, modern web app for detecting **helmets** and **safety vests** using a fine-tuned **YOLOv8** model.  
Upload an image → get real-time predictions → clean UI powered by Streamlit.

## Run Locally
Clone the repository
```bash
git clone https://github.com/tekle-eyesus/yolov8-safety-gear-detection.git
cd yolov8-safety-gear-detection
```
Create and activate virtual environment (recommended: Python 3.10)
```bash
py -3.10 -m venv venv
# or on Linux/macOS:
# python3.10 -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Linux/macOS
```
Install dependencies
```bash
pip install -r requirements.txt
```
## Features
- Upload image → detect helmets & safety vests  
- Clean modern UI  
- Lightweight CPU-only model  
- Fast inference using YOLOv8  
- Works on Windows, Linux, macOS  

## License
MIT License. Free to use, modify, and build upon.


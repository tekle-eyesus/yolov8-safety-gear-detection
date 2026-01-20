from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image

class SafetyModel:
    def __init__(self, weight_path="app/model/best.pt"):
        self.model = YOLO(weight_path)

    def predict(self, image: Image.Image):
        # Convert PIL to array
        img_array = np.array(image)
        results = self.model.predict(img_array, conf=0.5)

        output = results[0].plot()  # Draw bounding boxes
        output = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
        return Image.fromarray(output)

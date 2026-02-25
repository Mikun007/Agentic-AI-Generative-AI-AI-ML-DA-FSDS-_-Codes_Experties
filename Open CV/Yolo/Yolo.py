# import ultralytics
# ultralytics.checks()
#
from ultralytics import YOLO
import numpy

# Load a pretrained YOLOv8n model
model = YOLO("yolov8n.pt", "v8")

# Predict on an image
detection_output = model.predict(source=r"C:\Users\mikun\Downloads\surprise.jpg", save=True)

# display tensor array
print(detection_output)


# display numpy array
# print(detection_output[0].numpy())
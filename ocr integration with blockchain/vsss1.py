import ultralytics
from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolov9c.pt")

# Perform detection on the webcam feed
results = model.predict(source="0", show=True)

# Print results
print(results)
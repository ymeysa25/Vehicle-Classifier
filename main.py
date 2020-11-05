import cv2
from detect_car_yolo import detect_car
from color_classifier import ColorClassifier
from vehicle_classifier import VehicleClassifier
from plate_recognition_alpr import get_plate_alpr
import json
import time
# declare image path that want to proceed
img_path = "img_test/agya2.jpg"

# ========= Load model ===================
# declare object for VehicleClassifier
vehicle_classifier = VehicleClassifier()

# declare object for color_classifier
color_classifier = ColorClassifier()
# ========= End Load model =================


start = time.time()
# get Car object using Yolo
cars = detect_car(img_path)

# declare variable to save vehicle and color prediction
colors = []
car_models = []
for ind, car in enumerate(cars):
    # Predict Color
    color = color_classifier.predict(car)

    # Predict Vehicle make and model
    pred = vehicle_classifier.predict(car)

    # Save to list Variable
    colors.append(color)
    car_models.append(pred)

# Get plate recognition with ALPR
plates = get_plate_alpr(img_path)

results = {
    "vehicle": car_models,
    "color": colors,
    "alpr": plates
}

print(json.dumps(results, indent=4))
end = time.time()
print("[INFO] All process took {:.6f} seconds".format(end - start))

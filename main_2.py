from plate_recognition_alpr import get_plate_alpr
import json
import time
from vehicle_classifier import VehicleClassifier
from color_classifier import ColorClassifier
import cv2


# # declare object for VehicleClassifier
# vehicle_classifier = VehicleClassifier()
#
# # declare object for color_classifier
# color_classifier = ColorClassifier()

def get_car_info(img_path, vehicle_classifier, color_classifier):
    # declare image path that want to proceed
    img = cv2.imread(img_path)

    # declare variable to save vehicle and color prediction
    colors = []
    car_models = []

    alpr = get_plate_alpr(img_path)
    # get vehicle bounding box from alpr
    boxes = alpr['vehicles']

    start = time.time()

    for box in boxes:
        x, y, w, h = box['x'], box['y'], box['width'], box['height']
        # get Vehicle object in image
        cropImage = img[y:y + h, x:x + w]
        # Predict color
        color = color_classifier.predict(cropImage)
        # Predict Car Make and Model
        result = vehicle_classifier.predict(cropImage)

        # Save to list Variable
        car_models.append(result)
        colors.append(color)

    hasil_akhir = {
        "vehicle": car_models,
        "color": colors,
        "alpr": alpr
    }
    end = time.time()

    print("[INFO] All process took {:.6f} seconds".format(end - start))

    return hasil_akhir

# print(json.dumps(hasil_akhir, indent=4))

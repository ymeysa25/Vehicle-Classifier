import cv2
from detect_car_yolo import detect_car
from vehicle_classifier import VehicleClassifier, load_label
import json
import time
import os
import datetime


# declare image path that want to proceed
img_path = "img_test/agya2.jpg"

image = cv2.imread(img_path)

# ========= Load model ===================
# declare object for VehicleClassifier
vehicle_classifier = VehicleClassifier()
# ========= End Load model =================

start = time.time()
# get Car object using Yolo
cars = detect_car(img_path)

# declare variable to save vehicle and color prediction
car_models = []
for ind, car in enumerate(cars):
    # Predict Vehicle make and model
    pred = vehicle_classifier.predict(car)

    # Save to list Variable
    car_models.append(pred)

print(json.dumps(car_models, indent=4))
end = time.time()
print("[INFO] All process took {:.6f} seconds".format(end - start))

print("""
Note : 
    Y --> Ya
    N --> Tidak  
""")

print(f"Mobil yang terdeksti adalah {car_models[0]['make'].capitalize()} {car_models[0]['model'].capitalize()}")
correction = input("Apakah klasifikasi mobil sudah benar? ")

if "y" in correction.lower():
    print("Baik, Terima Kasih")
elif "n" in correction.lower():
    label = load_label()

    print("Baik, Silahkan pilih label mobil yang benar")
    print(label)
    corr_label = input("Silahkan masukan sesuai kategori diatas : ")
    path = 'image'
    filename = label[corr_label] + "@" + str(datetime.datetime.now()) + ".jpg"
    filename = filename.replace(":", "_")
    cv2.imwrite(os.path.join(path, filename), image)
    cv2.waitKey(0)
    print("OK, akan kita perbaiki")
else:
    print("Wrong Input")


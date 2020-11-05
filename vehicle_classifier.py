import cv2
from keras.models import model_from_json
import json
import numpy as np
import config


size = config.vehicle_classifier_input_size
model_arch = config.vehicle_model_json
model_weight = config.vehicle_model_weight
label_path = config.vehicle_car_label

def load_model():
    with open(model_arch, 'r') as file:
        json_model = file.read()

    model = model_from_json(json_model)
    model.load_weights(model_weight)
    return model


def load_label():
    with open(label_path) as file:
        label = json.load(file)

    return label


class VehicleClassifier():
    def __init__(self):
        self.model = load_model()
        self.label = load_label()

    def predict(self, image):
        model = self.model
        LABELS = self.label
        img = cv2.resize(image, size)
        # img = img / 255
        img = img.reshape(1, *size, 3)
        pred = model.predict(img)
        label = LABELS[str((np.argmax(pred)))]
        proba = max(pred[0])

        min_val = sorted(pred[0], reverse=True)[1:4]
        indices = [list(pred[0]).index(val) for val in min_val]
        candidates = []

        for i, index in enumerate(indices):
            can_label = LABELS[str(index)]
            can_labels = can_label.split(" ")

            can_make = can_labels[0]
            can_model = " "
            can_model = can_model.join(can_labels[1:])
            candidates.append({
                "make": can_make.capitalize(),
                "model": can_model.capitalize(),
                "proba": str(round(min_val[i], 6))
            })

        # print(candidates)
        cars_label = label.split(" ")
        car_make = cars_label[0]
        car_model = ' '
        car_model = car_model.join(cars_label[1:])
        data = {"make": car_make.capitalize(),
                "model": car_model.capitalize(),
                "prob": str(proba),
                "vehicle_candidates" : candidates
                }

        return data

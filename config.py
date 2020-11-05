# Copyright © 2019 by Spectrico
# Licensed under the MIT License

# Color Classifier
# =======================================================================================
model_file = "model/model-weights-spectrico-car-colors-mobilenet-224x224-052EAC82.pb"  # path to the car color classifier
label_file = "color_labels.txt"   # path to the text file, containing list with the supported makes and models
input_layer = "input_1"
output_layer = "softmax/Softmax"
classifier_input_size = (224, 224) # input size of the classifier

# =======================================================================================

# Vehicle Classifier
vehicle_model_weight = "model/xception_299x299_weight.h5"
vehicle_model_json = "model/xception_299x299.json"
vehicle_car_label = "vehicle_labels.json"
vehicle_classifier_input_size = (299, 299)




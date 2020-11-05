from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from vehicle_classifier import VehicleClassifier
from color_classifier import ColorClassifier
from main_2 import get_car_info
import time

# declare object for VehicleClassifier
vehicle_classifier = VehicleClassifier()

# declare object for color_classifier
color_classifier = ColorClassifier()

UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/getCarInfo", methods=["POST"])
def homePage():
    try:
        data = {}
        start = time.time()
        file = request.files['images']
        file_name = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(file_path)

        result = get_car_info(img_path=file_path,
                              vehicle_classifier=vehicle_classifier,
                              color_classifier=color_classifier)

        plate_info = ''
        msg = ''
        try:
            if request.form['plate'].lower() == "true":
                plate_info = True
            elif request.form['plate'].lower() == "false":
                plate_info = False
            else:
                msg = "Sorry, wrong keyword"

        except:
            plate_info = True

        classifier_info = ''
        try:
            if request.form['classifier'].lower() == "true":
                classifier_info = True
            elif request.form['classifier'].lower() == "false":
                classifier_info = False
            else:
                msg = "Sorry, wrong keyword"
        except:
            classifier_info = False

        if plate_info:
            data['alpr'] = result['alpr']

        if classifier_info:
            for ind, color in enumerate(result['color']):
                result['vehicle'][ind]['color'] = color
            data['classifier'] = result['vehicle']

        end = time.time()
        print("Cost Time : ", end - start)

        message = {
            "message": "Success to Classify",
            "success": True,
            "data": data
        }

        if msg != '':
            message['message'] = msg
        return jsonify(message)

    except Exception as e:
        data = {"message": "Failed to Classify",
                "success": False,
                "error": str(e)
                }
        return data


if __name__ == '__main__':
    app.run(debug=True)

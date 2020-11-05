# Requires "requests" to be installed (see python-requests.org)
import requests
import datetime

def getRemoveBg(img_path):
    filename = img_path.split(".")[0] + "@" + str(datetime.datetime.now()) + ".png"
    filename = filename.replace(":", "_")

    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(img_path, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'bAq62fF4u382w7gG2PUrKHPH'},
    )
    if response.status_code == requests.codes.ok:
        with open(filename, 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)

    return filename

getRemoveBg("img_test/3.jpg")
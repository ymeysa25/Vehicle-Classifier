import cv2
import datetime
img_path = "img_test/agya2.jpg"

img = cv2.imread(img_path)
filename = str(datetime.datetime.now()) + ".jpg"
filename = filename.replace(":", "_")
print(filename)

cv2.imwrite(f"image/{filename}", img)
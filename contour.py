import cv2
from plate_recognition_alpr import get_plate_alpr
img_path = "img_test/3.jpg"
img = cv2.imread(img_path)

alpr = get_plate_alpr(img_path)
boxes = alpr['vehicles']
for box in boxes:
    x, y, w, h = box['x'], box['y'], box['width'], box['height']
    # get Vehicle object in image
    cropImage = img[y:y + h, x:x + w]
    img = cropImage

imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
height, width, _ = img.shape
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    area = cv2.contourArea(contour)
    print(area)
    x, y, w, h = cv2.boundingRect(approx)
    if area > 50:
        cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
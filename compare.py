from skimage.measure import compare_ssim
from plate_recognition_alpr import get_plate_alpr
import cv2
from removebg import getRemoveBg

size = (500, 500)
img1_path = "img_test/agya2.jpg"
img2_path = "img_test/13.jpeg"

img1 = cv2.imread(img1_path)
alpr = get_plate_alpr(img1_path)
boxes = alpr['vehicles']
for box in boxes:
    x, y, w, h = box['x'], box['y'], box['width'], box['height']
    # get Vehicle object in image
    cropImage = img1[y:y + h, x:x + w]

    img1_crop = cropImage

img2 = cv2.imread(img2_path)
alpr = get_plate_alpr(img2_path)
boxes = alpr['vehicles']
for box in boxes:
    x, y, w, h = box['x'], box['y'], box['width'], box['height']
    # get Vehicle object in image
    cropImage = img2[y:y + h, x:x + w]
    img2_crop = cropImage

cv2.imwrite("removebg/gambar1.jpg", img1_crop)
cv2.imwrite("removebg/gambar2.jpg", img2_crop)

# img1_removebg = getRemoveBg("removebg/gambar1.jpg")
# img2_removebg = getRemoveBg("removebg/gambar2.jpg")
img1_removebg = "img"

img1_crop = cv2.imread("removebg/gambar1@2020-10-23 13_27_00.929563.png")
img2_crop = cv2.imread("removebg/gambar2@2020-10-23 13_27_03.851647.png")

img1_crop = cv2.resize(img1_crop, size)
img2_crop = cv2.resize(img2_crop, size)

# img1_crop = cv2.cvtColor(img1_crop, cv2.COLOR_BGR2GRAY)
# img2_crop = cv2.cvtColor(img2_crop, cv2.COLOR_BGR2GRAY)
#
# img1_crop = cv2.Canny(img1_crop, 100,200)
# img2_crop = cv2.Canny(img2_crop, 100,200)

img1_crop = img1_crop / 255
img2_crop = img2_crop / 255


# cv2.imwrite("gambar1.jpg", img1_crop)
# cv2.imwrite("gambar2.jpg", img2_crop)
img1_crop = cv2.flip(img1_crop, 1)
hasil = compare_ssim(img1_crop, img2_crop, multichannel=True)
print(hasil)

cv2.imshow("Image 1", img1_crop)
cv2.imshow("Image 2", img2_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
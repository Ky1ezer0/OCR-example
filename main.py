import cv2
import pytesseract
from pytesseract import Output
import os

# For windows
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = (
        r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    )

images = cv2.imread("test.png")
# gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Image", images)
# cv2.imshow("Image Gray", gray)

result = pytesseract.image_to_data(images, output_type=Output.DICT)
# print(result.keys())

# show box
n_boxes = len(result["text"])
for i in range(n_boxes):
    if float(result["conf"][i]) > 60:
        (x, y, w, h) = (
            result["left"][i],
            result["top"][i],
            result["width"][i],
            result["height"][i],
        )
        images = cv2.rectangle(images, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Result", images)
cv2.waitKey(0)

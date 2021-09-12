import cv2
import pytesseract

images = cv2.imread("test.jpg")
gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Image", images)
# cv2.imshow("Image Gray", gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
print(pytesseract.image_to_string(images))

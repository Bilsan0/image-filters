
import cv2 as cv

img = cv.imread('photos/photo1.jpg')

print("Available filters:")
print("1 - Gray")
print("2 - Blur")
print("3 - Canny Edges")
print("Enter numbers separated by comma (e.g. 1,3):")

choices = input("Your choice: ").split(",")

result = img.copy()

if "1" in choices:
    result = cv.cvtColor(result, cv.COLOR_BGR2GRAY)

if "2" in choices:
  
    if len(result.shape) == 2:
        result = cv.cvtColor(result, cv.COLOR_GRAY2BGR)
    result = cv.GaussianBlur(result, (15,15), cv.BORDER_DEFAULT)

if "3" in choices:
    gray_for_canny = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  
    result = cv.Canny(gray_for_canny, 50, 150)


cv.imshow("Filtered Image", result)
cv.waitKey(0)
cv.destroyAllWindows()

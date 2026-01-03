import cv2

# Read grayscale image
img = cv2.imread("Macho.jpg", cv2.IMREAD_GRAYSCALE)

# Apply threshold
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

cv2.imshow("Thresholded", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

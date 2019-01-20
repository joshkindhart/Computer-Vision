import cv2

img = cv2.imread("./picameraisworking.jpg", 0)

cv2.imshow("Me",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

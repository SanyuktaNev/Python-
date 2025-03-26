import cv2
import matplotlib.pyplot as plt
img=cv2.imread("geeks.png.jpg")

#plt.imshow(img)
#plt.waitforbuttonpress()
#plt.close('all')

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
import numpy as np
import cv2

# Load the correction values previously calculated
mtx = np.load('mtx.npy')
dist = np.load('dist.npy')
newcameramtx = np.load('newcameramtx.npy')

# Open camera
cam = cv2.VideoCapture(0)
res, src = cam.read()

# Generate undistortion maps
map1, map2 = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, src.shape[1::-1], cv2.CV_32FC1)

while(True):
	# Update camera input in real time
	res, src = cam.read()

	# Remap the image using the undistortion maps
	dst = cv2.remap(src, map1, map2,cv2.INTER_LINEAR)

	# Show corrected image
	cv2.imshow('Imagen_corregida',dst)
	
	# Press q to close the program
	if cv2.waitKey(1) == ord('q'):
		break
	
cv2.destroyAllWindows()
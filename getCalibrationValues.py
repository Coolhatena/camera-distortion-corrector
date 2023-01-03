import numpy as np
import cv2
import glob

# set here your chessboard height and width (measured in squares, example: 5 squares height and 6 squares width)
chessHeight = 5
chessWidth = 6

# prepare object points
objp = np.zeros((chessHeight*chessWidth,3), np.float32)
objp[:,:2] = np.mgrid[0:chessWidth,0:chessHeight].T.reshape(-1,2)

# Declare arrays for the object points and image points of the sample images
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
 
images = glob.glob('./images/*.jpg')
 
for imgName in images:
    img = cv2.imread(imgName)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
    # Find chessboard Corners
    ret, corners = cv2.findChessboardCorners(gray, (chessWidth,chessHeight),None)
	
	# if the corners are found, add object points and image points (Using cornerSubPix to increase precision)
    if ret == True:
        objpoints.append(objp)
 
        newCorners = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1), (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
        imgpoints.append(newCorners)

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, gray.shape[::-1], 0)

np.save('mtx.npy', mtx)
np.save('dist.npy', dist)
np.save('newcameramtx.npy', newcameramtx)

cam = cv2.VideoCapture(0)
    
res, src = cam.read()
cv2.imwrite('./original_image.jpg',src)
    
dst = cv2.undistort(src, mtx, dist, None, newcameramtx)
cv2.imwrite('./Corrected_image.jpg',dst)

import cv2

# Open camera and show what its seeing
cam = cv2.VideoCapture(0)
ret, src = cam.read()
cv2.imshow('Image', src)

# Repeat the loop n times, where n is the number of sample photos needed
# default its 11 (10 photos), but this number can be changed
for i in range(1, 11):
    print(f'image {i} of {10}')
    while(True):
        # Update camera input in real time and display it
        ret, src = cam.read()
        cv2.imshow('Image', src)
        
        # Press q to take photo
        key = cv2.waitKey(1);
        if key == ord('q'):
            print('Taking image... Smile :)')
            break
            
    ret, src = cam.read()
    cv2.imwrite(f'./images/image_{i}.jpg', src)

cv2.destroyAllWindows();

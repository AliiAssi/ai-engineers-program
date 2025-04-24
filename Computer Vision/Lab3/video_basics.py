import cv2
import time

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print('Error: Could not open camera. Please check if the webcam is connected and accessible.')
    exit(1)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f'Camera opened. Frame size: {frame_width}x{frame_height}')

time.sleep(2)

while True:
    ret, frame = cam.read()
    if not ret or frame is None:
        print('Error: Failed to retrieve frame from camera. Exiting...')
        break
    if frame.shape[0] > 0 and frame.shape[1] > 0:
        cv2.imshow('Camera', frame)
    else:
        print(f'Error: Invalid frame dimensions: {frame.shape if frame is not None else "None"}')
    if cv2.waitKey(1) == ord('q'):
        print('Quitting...')
        break

cam.release()
cv2.destroyAllWindows()
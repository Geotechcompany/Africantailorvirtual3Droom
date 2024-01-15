import cv2

def check_camera_index(index):
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        print(f"Camera index {index} is working.")
        cap.release()
    else:
        print(f"Camera index {index} is not working.")

# Try different camera indices
for i in range(10):
    check_camera_index(i)

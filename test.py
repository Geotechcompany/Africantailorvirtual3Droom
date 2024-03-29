from flask import Flask, render_template, Response, request, redirect, url_for
import cv2
import imutils
import numpy as np
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

cap = cv2.VideoCapture(0)
curClothId = 0
size = 100
images = [
    cv2.imread('tshirt/tshirt1.png', cv2.IMREAD_UNCHANGED),  # Use PNG for images with transparency
    cv2.imread('tshirt/tshirt2.png', cv2.IMREAD_UNCHANGED),
    # Add more cloth images as needed
]
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

uploaded_image = None  # Variable to store the uploaded image

def generate_frames():
    global size, uploaded_image

    while True:
        success, cam = cap.read()
        if not success:
            break
        else:
            cam = cv2.flip(cam, 1, 0)

            if uploaded_image is not None:
                # Use the uploaded image if available
                t_shirt = uploaded_image
            else:
                # Display a text message if no image is uploaded
                t_shirt = np.zeros_like(cam)
                cv2.putText(t_shirt, "Hi there! Upload a design to try on", (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            resized = imutils.resize(cam, width=800)
            gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
            circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

            if circles is not None:
                circles = np.round(circles[0, :]).astype("int")
                for (x, y, r) in circles:
                    if r > 30:
                        cv2.circle(cam, (x, y), r, (0, 255, 0), 4)
                        cv2.rectangle(cam, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
                        size = r * 7

            if size > 350:
                size = 350
            elif size < 100:
                size = 100

            t_shirt_resized = imutils.resize(t_shirt, width=size)

            f_height = cam.shape[0]
            f_width = cam.shape[1]
            t_height = t_shirt_resized.shape[0]
            t_width = t_shirt_resized.shape[1]
            height = int(f_height / 2 - t_height / 2)
            width = int(f_width / 2 - t_width / 2)

            # Check if the shirt image already has an alpha channel
            if t_shirt_resized.shape[2] == 3:
                t_shirt_resized = cv2.cvtColor(t_shirt_resized, cv2.COLOR_BGR2BGRA)

            mask = t_shirt_resized[:, :, 3] / 255.0
            blended = (cam[height:height + t_height, width:width + t_width] * (1.0 - mask[:, :, None]) +
                       t_shirt_resized[:, :, :3] * (mask[:, :, None]))

            cam[height:height + t_height, width:width + t_width] = blended

            font = cv2.FONT_HERSHEY_PLAIN
            x = 10
            y = 20
        
            ret, buffer = cv2.imencode('.jpg', cam)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.php')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/change_cloth/<direction>', methods=['POST'])
def change_cloth(direction):
    global curClothId, uploaded_image

    # Reset the uploaded image variable when changing cloth
    uploaded_image = None

    if direction == 'next':
        curClothId = (curClothId + 1) % len(images)
    elif direction == 'prev':
        curClothId = (curClothId - 1) % len(images)

    return redirect(url_for('index'))

@app.route('/upload', methods=['POST'])
def upload():
    global images, uploaded_image

    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Process and save the uploaded image
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Load the uploaded image with an alpha channel
        uploaded_image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)

        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

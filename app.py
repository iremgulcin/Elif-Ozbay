from flask import Flask, render_template, Response
import cv2
from keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
import numpy as np

app = Flask(__name__)

face_classifier = cv2.CascadeClassifier(r'C:\Users\elifo\Desktop\samsung_innovation_campus\emotion_detection\haarcascade_frontalface_default.xml')
classifier = load_model(r'C:\Users\elifo\Desktop\samsung_innovation_campus\emotion_detection\static\model.h5')
print("Model yüklendi:", classifier)

emotion_labels = ['Kizgin', 'Igrenme', 'Korku', 'Mutlu', 'Normal', 'Uzgun', 'Sasirmis']

cap = cv2.VideoCapture(0)
def detect_faces(frame):
    #yüzleri algılanması
    faces = face_classifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            
    # web sitesi için kontrol yüzlerin algılanıp algılanmadığını anlamak için
    return faces


def gen_frames():
    while True:
        success, frame = cap.read()  
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = detect_faces(gray)
            print(faces)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
                print("Yüz koordinatları:", x, y, w, h)
                
                if np.sum([roi_gray]) != 0:
                    roi = roi_gray.astype('float')/255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi, axis=0)

                    prediction = classifier.predict(roi)[0]
                    label = emotion_labels[prediction.argmax()]
                    label_position = (x, y)
                    cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
            
         


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

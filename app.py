from flask import Flask, render_template, Response
import cv2
import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array




app = Flask(__name__)

# Model ve yüz sınıflandırıcısını yükleme
classifier = load_model(r'C:\Users\elifo\Desktop\samsung_innovation_campus\emotion_detection\static\model.h5')
if classifier:
    print("Model başarıyla yüklendi.")
else:
    print("Model yüklenirken bir hata oluştu.")
face_classifier = cv2.CascadeClassifier(r'C:\Users\elifo\Desktop\samsung_innovation_campus\emotion_detection\haarcascade_frontalface_default.xml')
if face_classifier.empty():
    print("Yüz algılama dosyası yüklenirken bir hata oluştu.")
else:
    print("Yüz algılama dosyası başarıyla yüklendi.")
# Duygu etiketleri
emotion_labels = ['Kizgin', 'Igrenme', 'Korku', 'Mutlu', 'Normal', 'Uzgun', 'Sasirmis']

# Kamerayı başlat
cap = cv2.VideoCapture(0)

def detect_faces(frame):
    # Yüz tespiti     
    faces = face_classifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=6, minSize=(50, 50))
    for (x, y, w, h) in faces:
        print("Algılanan yüz koordinatları: x=", x, "y=", y, "w=", w, "h=", h)
    return faces

def gen_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            # Görüntüyü yatay olarak ters çevirme
            frame = cv2.flip(frame, 1)
            
            # Gri tonlamaya dönüştürme
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            # Yüz tespiti 
            faces = detect_faces(gray)
            
            for (x, y, w, h) in faces:
                # Algılanan yüzleri dikdörtgen içine alma
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
                
                # Yüz bölgesini kırpma
                roi_gray = gray[y:y+h, x:x+w]
                roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)
                
                # ROI'nin içeriğini kontrol etme
                print("ROI içeriği:", roi_gray)
                
                if np.sum([roi_gray]) != 0:
                    # Yüz bölgesini hazırlame ve modelde tahmin yapma
                    roi = roi_gray.astype('float')/255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi, axis=0)

                    prediction = classifier.predict(roi)[0]
                    label = emotion_labels[prediction.argmax()]
                    
                    # Duygu tahmin sonucunu ekrana yazdırma
                    print("Tahmin edilen duygu:", label)
                    
                    # Duygu etiketini ekrana yazdırma
                    cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
                
            # Görüntüyü JPEG formatına dönüştürme
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=False)

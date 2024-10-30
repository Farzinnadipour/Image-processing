import cv2
import face_recognition
import os
import numpy as np

# ایجاد دایرکتوری برای ذخیره چهره‌ها
if not os.path.exists('captured_faces'):
    os.makedirs('captured_faces')

# بارگذاری مدل‌های شناسایی
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# شروع ضبط از دوربین
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("خطا در باز کردن دوربین!")
    exit()

face_id = 0
known_face_encodings = []

while True:
    ret, frame = cap.read()
    if not ret:
        print("عدم دریافت فریم!")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # تبدیل به رنگ RGB
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # تبدیل به خاکستری برای پردازش
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_color = frame[y:y + h, x:x + w]

        # استخراج انکدینگ چهره
        face_encoding = face_recognition.face_encodings(rgb_frame, [(y, x + w, y + h, x)])[0]

        # بررسی تکراری بودن چهره
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        
        if not any(matches):  # اگر هیچ چهره‌ای مشابه نبود
            # ذخیره چهره و انکدینگ آن
            face_filename = f'captured_faces/face_{face_id}.jpg'
            cv2.imwrite(face_filename, roi_color)
            known_face_encodings.append(face_encoding)
            print(f"چهره ذخیره شد: {face_filename}")
            face_id += 1  # افزایش شناسه چهره برای چهره بعدی

        # رسم مستطیل دور چهره
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # شناسایی چشم‌ها
        roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=10, minSize=(15, 15))
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # شناسایی لبخند
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=22, minSize=(25, 25))
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2)

    # نمایش فریم در پنجره
    cv2.imshow('Camera', frame)

    # توقف با زدن کلید 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

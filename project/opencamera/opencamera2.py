import cv2
import face_recognition
import numpy as np
import os

# پوشه‌ای برای ذخیره تصاویر افراد جدید ایجاد کنید
if not os.path.exists('captured_faces'):
    os.makedirs('captured_faces')

# باز کردن دوربین
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("خطا در باز کردن دوربین!")
    exit()

# لیستی از چهره‌های شناسایی شده قبلی
known_face_encodings = []
face_id = 0  # شمارنده برای نام‌گذاری تصاویر

while True:
    # خواندن هر فریم از دوربین
    ret, frame = cap.read()
    if not ret:
        print("عدم دریافت فریم!")
        break

    # تغییر اندازه فریم برای بهبود سرعت پردازش
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]  # تبدیل BGR به RGB

    # شناسایی مکان چهره‌ها و استخراج ویژگی‌ها
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        # بررسی اینکه آیا چهره جدید است یا خیر
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
        if True not in matches:
            # چهره جدید است؛ ذخیره ویژگی‌ها
            known_face_encodings.append(face_encoding)

            # ذخیره عکس فرد جدید
            top, right, bottom, left = face_location
            top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4  # مقیاس به اندازه اصلی
            face_image = frame[top:bottom, left:right]
            cv2.imwrite(f"captured_faces/person_{face_id}.jpg", face_image)
            print(f"چهره جدید ذخیره شد: person_{face_id}.jpg")
            face_id += 1

        # رسم مستطیل دور چهره
        top, right, bottom, left = face_location
        top, right, bottom, left = top * 4, right * 4, bottom * 4, left * 4  # مقیاس به اندازه اصلی
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # نمایش فریم در پنجره
    cv2.imshow('Camera', frame)

    # با زدن کلید 'q' برنامه متوقف می‌شود
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# آزاد کردن منابع
cap.release()
cv2.destroyAllWindows()

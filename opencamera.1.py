import cv2

# باز کردن دوربین (دوربین پیش‌فرض دستگاه)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("خطا در باز کردن دوربین!")
    exit()

# بارگذاری مدل شناسایی چهره (در صورت نیاز به رهگیری چهره)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # خواندن هر فریم از دوربین
    ret, frame = cap.read()

    if not ret:
        print("عدم دریافت فریم!")
        break

    # تبدیل تصویر به خاکستری برای شناسایی چهره
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # شناسایی چهره‌ها در تصویر
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # رسم مستطیل دور چهره‌های شناسایی شده
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # نمایش فریم در پنجره
    cv2.imshow('Camera', frame)

    # با زدن کلید 'q' برنامه متوقف می‌شود
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# آزاد کردن منابع
cap.release()
cv2.destroyAllWindows()

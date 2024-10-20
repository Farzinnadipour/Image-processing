import cv2


def detect_rectangles(image_path):
    # خواندن تصویر
    image = cv2.imread(image_path)

    # تبدیل تصویر به مقیاس خاکستری
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # تشخیص لبه‌ها
    edges = cv2.Canny(gray, 50, 150)

    # یافتن مستطیل‌ها
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rectangles = []
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        if len(approx) == 4:
            rectangles.append(approx)

    return rectangles


# مسیر تصویر را اینجا قرار دهید
image_path = 'F:/python/code/image proccing/download.png'

rectangles = detect_rectangles(image_path)
print("تعداد مستطیل‌های یافت شده:", len(rectangles))
for i, rect in enumerate(rectangles):
    x, y, w, h = cv2.boundingRect(rect)
    print(f"مستطیل {i + 1}:")
    print(f"   طول = {w} پیکسل، عرض = {h} پیکسل")
    # محاسبه ابعاد مستطیل
    length_cm = w / 96 * 2.54  # 96 پیکسل در هر اینچ و 2.54 سانتی‌متر در هر اینچ
    width_cm = h / 96 * 2.54
    length_mm = length_cm * 10
    width_mm = width_cm * 10
    print(f"   طول = {length_cm:.2f} سانتی‌متر، عرض = {width_cm:.2f} سانتی‌متر")
    print(f"   طول = {length_mm:.2f} میلی‌متر، عرض = {width_mm:.2f} میلی‌متر")

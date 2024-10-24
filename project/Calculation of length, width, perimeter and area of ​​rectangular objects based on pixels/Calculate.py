import cv2
from tkinter import Tk, filedialog

def detect_rectangles(image_path):
    # Read the image
    image = cv2.imread(image_path)

    if image is None:
        print("Image not found or invalid path.")
        return []

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edges = cv2.Canny(gray, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rectangles = []
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

        if len(approx) == 4:
            rectangles.append(approx)

    return rectangles

# Open file dialog for selecting the image
Tk().withdraw()  # Hide the main Tkinter window
image_path = filedialog.askopenfilename(
    title="Select an image", 
    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp")]
)

if not image_path:
    print("No image selected.")
else:
    rectangles = detect_rectangles(image_path)
    print("Number of rectangles found:", len(rectangles))

    for i, rect in enumerate(rectangles):
        x, y, w, h = cv2.boundingRect(rect)
        print(f"Rectangle {i + 1}:")
        print(f"   Width = {w} pixels, Height = {h} pixels")

        # Calculate dimensions of the rectangle
        length_cm = w / 96 * 2.54
        width_cm = h / 96 * 2.54
        length_mm = length_cm * 10
        width_mm = width_cm * 10

        print(f"   Length = {length_cm:.2f} cm, Width = {width_cm:.2f} cm")
        print(f"   Length = {length_mm:.2f} mm, Width = {width_mm:.2f} mm")

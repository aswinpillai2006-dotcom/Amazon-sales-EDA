from ultralytics import YOLO
import cv2

# Load a stronger YOLO model
model = YOLO("yolo11n.pt")

# COCO class ID for cell phone
CELL_PHONE_CLASS = 67

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Webcam could not be opened.")
    exit()

print("Webcam started.")
print("Show your smartphone clearly to the camera.")
print("Press Q to quit.")

while True:
    success, frame = cap.read()

    if not success:
        print("ERROR: Could not read webcam.")
        break

    # Run YOLO
    results = model.predict(
        source=frame,
        conf=0.10,
        iou=0.45,
        verbose=False
    )

    # Only display CELL PHONE detections
    for result in results:

        if result.boxes is None:
            continue

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            # ONLY cell phone
            if class_id != CELL_PHONE_CLASS:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw box
            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                3
            )

            # Label
            text = f"SMARTPHONE {confidence * 100:.1f}%"

            cv2.putText(
                frame,
                text,
                (x1, max(y1 - 10, 30)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2
            )

    # Show webcam
    cv2.imshow("YOLO - Smartphone Detection Only", frame)

    # Q = quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
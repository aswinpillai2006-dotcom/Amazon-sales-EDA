from ultralytics import YOLO
import cv2
import numpy as np


# Load YOLO model
model = YOLO("yolo11n.pt")


# Vehicle classes in the COCO dataset
VEHICLE_CLASSES = {
    2: "Car",
    3: "Motorcycle",
    5: "Bus",
    7: "Truck"
}


def detect_vehicles(image):

    # Convert PIL image to NumPy array
    if not isinstance(image, np.ndarray):
        image = np.array(image)

    # Ensure RGB image
    if len(image.shape) == 3 and image.shape[2] == 4:
        image = cv2.cvtColor(
            image,
            cv2.COLOR_RGBA2RGB
        )

    # Copy image for annotations
    annotated_image = image.copy()

    # Run YOLO
    results = model(
        image,
        conf=0.25
    )

    # Vehicle counters
    vehicle_count = {
        "Car": 0,
        "Motorcycle": 0,
        "Bus": 0,
        "Truck": 0
    }

    # Process detections
    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])

            if class_id in VEHICLE_CLASSES:

                vehicle_name = VEHICLE_CLASSES[class_id]

                vehicle_count[vehicle_name] += 1

                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0].tolist()
                )

                confidence = float(box.conf[0])

                # Draw bounding box
                cv2.rectangle(
                    annotated_image,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                # Create label
                label = (
                    f"{vehicle_name} "
                    f"{confidence:.2f}"
                )

                # Draw label
                cv2.putText(
                    annotated_image,
                    label,
                    (x1, max(y1 - 10, 25)),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    return annotated_image, vehicle_count
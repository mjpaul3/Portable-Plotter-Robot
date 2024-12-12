import cv2
import numpy as np
from cv2 import aruco

# # Function to generate and save ArUco tags
# def generate_aruco_tags(dictionary_type, tag_id, tag_size, save_path):
#     aruco_dict = cv2.aruco.Dictionary(dictionary_type)
#     tag = np.zeros((tag_size, tag_size), dtype=np.uint8)
#     tag = cv2.aruco.drawMarker(aruco_dict, tag_id, tag_size)
#     cv2.imwrite(save_path, tag)
#     print(f"ArUco tag saved to {save_path}")
#
# # Generate and save a tag
# aruco_dict_type = cv2.aruco.DICT_6X6_250  # Use a 6x6 dictionary with 250 unique IDs
aruco_dict_type = aruco.getPredefinedDictionary(aruco.DICT_5X5_250)

# tag_id = 0  # ID of the tag
# tag_size = 200  # Tag size in pixels
# save_path = "aruco_tag.png"
# generate_aruco_tags(aruco_dict_type, tag_id, tag_size, save_path)

# Initialize camera and pose estimation
cap = cv2.VideoCapture(0)  # 0 selects the default camera
if not cap.isOpened():
    print("Error: Unable to access the camera")
    exit()

# Load the dictionary and parameters for pose estimation
aruco_dict = aruco_dict_type
parameters = cv2.aruco.DetectorParameters()  # Default detection parameters

# Camera calibration parameters (these should ideally be replaced with actual calibration data)
camera_matrix = np.array([
    [800, 0, 320],
    [0, 800, 240],
    [0, 0, 1]
], dtype=np.float32)
dist_coeffs = np.zeros((5,), dtype=np.float32)  # Assume no lens distortion for simplicity

# Marker size in meters (real-world size of the marker)
marker_size = 0.05  # 5 cm

print("Starting ArUco detection and pose estimation. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to read from the camera")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect markers in the frame
    corners, ids, rejected = cv2.aruco.detectMarkers(gray_frame, aruco_dict, parameters=parameters)

    if ids is not None:
        # Draw detected markers
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)

        # Perform pose estimation for each marker
        for corner, marker_id in zip(corners, ids):
            rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(corner, marker_size, camera_matrix, dist_coeffs)

            # Draw pose axes
            cv2.aruco.drawAxis(frame, camera_matrix, dist_coeffs, rvec, tvec, marker_size * 0.5)

            # Display translation vector
            tvec_text = f"ID: {marker_id[0]} T: {tvec[0][0]}"
            cv2.putText(frame, tvec_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("ArUco Pose Estimation", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close OpenCV windows
cap.release()
cv2.destroyAllWindows()

import cv2
import face_recognition
import numpy as np
from google.colab.patches import cv2_imshow

# Load the known image and encode it
known_image_path = "/content/sample_data/ANAND2.jpg"  # Path to your known face image
known_image = face_recognition.load_image_file(known_image_path)
known_encoding = face_recognition.face_encodings(known_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [known_encoding]
known_face_names = ["Anand"]

def recognize_faces(frame):
    """Identify faces in a given frame."""
    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # Check if the face matches any known face encodings
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        # Use the first match if found
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        face_names.append(name)

    # Draw boxes around recognized faces and display names
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    return frame

def process_video(video_path):
    """Process a video file to detect and recognize faces."""
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Break the loop if no frame is captured
        if not ret:
            break

        # Recognize faces in the frame
        processed_frame = recognize_faces(frame)

        # Display the resulting frame
        cv2_imshow(processed_frame)

    # When everything is done, release the capture
    video_capture.release()

# Process the uploaded video
video_file_path = "/content/sample_data/anand.mp4"  # Path to the uploaded video file
process_video(video_file_path)

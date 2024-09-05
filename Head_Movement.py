import cv2
import dlib
import random
import time
import numpy as np
from imutils import face_utils

# Load pre-trained dlib face detector and landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# Function to detect the direction of head movement
def detect_head_movement(landmarks):
    # Nose landmark is around point 30
    nose_point = landmarks[30]
    
    # Midpoints for face
    left_eye_point = landmarks[36]
    right_eye_point = landmarks[45]
    
    # Calculate the movement direction based on eye and nose positions
    horizontal_diff = nose_point[0] - (left_eye_point[0] + right_eye_point[0]) / 2
    vertical_diff = nose_point[1] - (left_eye_point[1] + right_eye_point[1]) / 2
    
    if abs(horizontal_diff) > 20:
        return "left" if horizontal_diff > 0 else "right"
    elif abs(vertical_diff) > 20:
        return "down" if vertical_diff > 0 else "up"
    else:
        return "center"

# Head movement prompt generator
def generate_random_prompt():
    prompts = ["up", "down", "left", "right"]
    return random.choice(prompts)

# Function to calculate accuracy
def calculate_accuracy(correct_count, total_count):
    if total_count == 0:
        return 0
    return (correct_count / total_count) * 100

# Function to calculate efficiency (time taken per prompt)
def calculate_efficiency(start_time, current_time, total_prompts):
    elapsed_time = current_time - start_time
    if total_prompts == 0:
        return 0
    return elapsed_time / total_prompts

# Initialize video capture
cap = cv2.VideoCapture(0)
time.sleep(1)  # Allow the camera to warm up

# Initialize variables for epoch tracking
total_prompts = 20  # Total number of prompts or epochs
current_prompt_count = 0
correct_count = 0

current_prompt = generate_random_prompt()
prompt_timer = time.time()
start_time = time.time()  # Start time for efficiency calculation

while current_prompt_count < total_prompts:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)
    
    for rect in rects:
        # Get landmarks
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)
        
        # Detect head movement
        head_movement = detect_head_movement(shape)
        
        # Display current prompt
        cv2.putText(frame, f"Move your head {current_prompt}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
        
        # Draw a green box if the movement matches the prompt, else red box
        if head_movement == current_prompt:
            color = (0, 255, 0)  # Green for correct movement
            correct_count += 1
        else:
            color = (0, 0, 255)  # Red for incorrect or no movement
        
        # Draw a box around the face
        (x, y, w, h) = face_utils.rect_to_bb(rect)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        
        # Update the prompt and print status every 5 seconds
        if time.time() - prompt_timer > 5:
            current_prompt = generate_random_prompt()
            prompt_timer = time.time()
            current_prompt_count += 1
            accuracy = calculate_accuracy(correct_count, current_prompt_count)
            efficiency = calculate_efficiency(start_time, time.time(), current_prompt_count)
            print(f"Epoch {current_prompt_count}/{total_prompts} - New prompt: {current_prompt} - Current movement detected: {head_movement}")
            print(f"Accuracy: {accuracy:.2f}%")
            print(f"Efficiency: {efficiency:.2f} seconds per prompt")

    # Display the video frame
    cv2.imshow("Head Movement Detection", frame)
    
    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources and close windows
cap.release()
cv2.destroyAllWindows()

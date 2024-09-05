import random
import cv2
import numpy as np
import mediapipe as mp
import time

# Function to generate a random 5-digit number
def generate_random_data():
    return [random.randint(1, 5) for _ in range(5)]  # List of 5 digits between 1 and 5

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands()

# Function to detect gesture (simplified example)
def detect_gesture(frame):
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        # Here you would implement actual gesture recognition logic
        # For demonstration, we'll just return a random number between 1 and 5
        # In practice, you'd analyze landmarks to recognize specific gestures
        return random.randint(1, 5)

    return None

def main():
    # Generate random 5-digit number
    target_number = generate_random_data()
    
    print(f"Generated 5-digit number: {target_number}")

    cap = cv2.VideoCapture(0)
    
    for digit in target_number:
        print(f"Please sign the digit: {digit}")
        
        # Display the digit to be signed for a few seconds
        time.sleep(3)  # Delay to give the user time to see the digit
        
        # Give a short delay before starting the detection
        time.sleep(2)
        
        correct_sign = False
        start_time = time.time()

        while True:
            ret, frame = cap.read()
            
            if not ret:
                break
            
            # Detect gesture
            gesture = detect_gesture(frame)
            
            if gesture is not None:
                if gesture == digit:
                    print(f"Correct gesture for digit {digit}")
                    correct_sign = True
                    break
                else:
                    print(f"Incorrect gesture for digit {digit}")
            
            # Draw hand landmarks on the frame
            if hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).multi_hand_landmarks:
                for landmarks in hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Display the frame
            cv2.imshow('Frame', frame)
            
            # Exit on 'q' key or time limit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            if time.time() - start_time > 10:  # 10 seconds to sign each digit
                print(f"Time limit exceeded for digit {digit}")
                break
        
        if not correct_sign:
            print("Failed to sign the correct digit in sequence.")
            cap.release()
            cv2.destroyAllWindows()
            return

    print("All digits signed correctly!")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

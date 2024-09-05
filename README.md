# Machine Learning Python Codes

Welcome to the Machine Learning Python Codes. This repository contains varieties of Machine Learning dependent Python Codes.

## Table of Contents
- [Face Recognition from Uploaded Video](#face-recognition-from-uploaded-video)
  - [About](#about)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Results](#results)
- [Live Face Recognition via Webcam](#live-face-recognition-via-webcam)
  - [About](#about-1)
  - [Requirements](#requirements-1)
  - [Installation](#installation-1)
  - [Usage](#usage-1)
  - [Results](#results-1)
- [Sign Language Digit Recognition via Webcam](#sign-language-digit-recognition-via-webcam)
  - [About](#about-2)
  - [Requirements](#requirements-2)
  - [Installation](#installation-2)
  - [Usage](#usage-2)
  - [Results](#results-2)
  - [Troubleshooting](#troubleshooting)
- [Head Movement Detection Project](#head-movement-detection-project)
  - [About](#about-3)
  - [Requirements](#requirements-3)
  - [Installation](#installation-3)
  - [Usage](#usage-3)
  - [Results](#results-3)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Face Recognition from Uploaded Video

### About

This project processes uploaded video files, identifying and tracking faces using pre-trained models. Each frame is analyzed to detect faces, which are then matched against a known database.

### Requirements

You'll need:
- **Google Colab** for running the project.
- **Python 3.6+** as your environment.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/a1n13a1n13d4/Face-Recognition-Project.git
   cd Face-Recognition-Project
   ```

2. **Open in Google Colab:**
   - Upload the repository to your Google Drive.
   - Open the `Face_Recognition_From_Upload_Video` notebook in Google Colab.

3. **Install dependencies:**
   ```python
   !pip install numpy opencv-python dlib face_recognition imutils
   ```

### Usage

1. **Upload your video file** to Google Drive.
2. **Update the script**:
   - Modify `video_path` in the script to point to your uploaded video.
3. **Run the script**:
   - Process the video, and the output will be saved in the specified directory.

### Results

The processed video with recognized faces will be saved to your Google Drive, along with a log file detailing detected faces and matches.

---

## Live Face Recognition via Webcam

### About

This project provides real-time face recognition via webcam, detecting and identifying faces against a pre-trained model.

### Requirements

You'll need:
- **Anaconda Navigator** to manage dependencies.
- **Python 3.6+** as your environment.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/a1n13a1n13d4/Face-Recognition-Project.git
   cd Face-Recognition-Project
   ```

2. **Create and activate a new Anaconda environment:**
   ```bash
   conda create -n face_recognition_env python=3.6
   conda activate face_recognition_env
   ```

3. **Navigate to the webcam project directory:**
   ```bash
   cd Live_Face_Recognition_Via_Webcam
   ```

4. **Install dependencies:**
   ```bash
   pip install numpy opencv-python dlib face_recognition imutils
   ```

### Usage

1. Ensure your webcam is properly set up.
2. Run the following command in the terminal:
   ```bash
   python live_face_recognition.py
   ```

The webcam feed will show real-time face detection and recognition.

### Results

The results are displayed live and logged to a file for future reference.

---

# Sign Language Digit Recognition via Webcam

## About

This project provides real-time sign language digit recognition via a webcam. It generates a random 5-digit number and prompts the user to sign each digit sequentially. The system verifies if the signed digits match the generated number and provides feedback on the accuracy.

## Requirements

You'll need:

- A Python 3.9.13
- A virtual environment manager (recommended: `venv`).

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/Sign-Language-Digit-Recognition.git
   cd Sign-Language-Digit-Recognition
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python -m venv envir
   ```

   - On Windows:

     ```bash
     envir\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source envir/bin/activate
     ```

3. **Install Dependencies**

   ```bash
   pip install mediapipe==0.9.1 opencv-python==4.7.0.72 numpy==1.21.4
   ```

## Usage

1. **Ensure Your Webcam is Properly Set Up**

   Make sure your webcam is connected and operational.

2. **Run the Script**

   ```bash
   python Sign_Detection.py
   ```

3. **How It Works**

   - The script generates a random 5-digit number consisting of digits 1-5.
   - For each digit, the script displays the digit to be signed and waits for the user to sign it.
   - The system uses MediaPipe to detect and recognize hand gestures.
   - The detected gestures are checked against the expected digits, and feedback is provided.

4. **Stopping the Program**

   - To stop the program at any time, press the 'q' key while the video window is open.

## Results

- **Real-Time Feedback**: The system provides live feedback on whether the signed digits match the generated number.
- **Logging**: Results are displayed on the terminal and can be customized to log to a file if needed.

## Troubleshooting

- **No Video Feed**:
  - Ensure your webcam is properly connected and accessible.
  - Check if other applications are using the webcam.

- **Import Errors**:
  - Verify that all required packages are installed in the virtual environment.

- **Gesture Recognition Not Accurate**:
  - Update the `detect_gesture()` function with more accurate gesture recognition logic using MediaPipe landmarks.

---
# Head Movement Detection Project

## About
This project uses a real-time video feed to detect and analyze head movements. It prompts users to move their heads in specific directions (up, down, left, right) and evaluates if the movements match the given prompt. The system uses pre-trained dlib models to detect faces and landmarks, and provides visual feedback based on detected movements.

## Requirements
You'll need:

- Python 3.9+ as your environment.
- OpenCV, dlib, numpy, and imutils libraries.
- A pre-trained dlib model for face landmarks (`shape_predictor_68_face_landmarks.dat`).

## Installation
1. **Clone the repository:**

    ```bash
    git clone https://github.com/a1n13a1n13d4/REPO2.ANAND.Live_Det_Spof/
    cd REPO2.ANAND.Live_Det_Spof
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv envir
    source envir/bin/activate  # On Windows use `envir\Scripts\activate`
    ```

3. **Install the required packages:**

    ```bash
    pip install opencv-python==4.5.5.64 dlib==19.22.1 imutils==0.5.4 face_recognition==1.3.0 numpy
    ```

4. **Download the dlib shape predictor model:**

    Download the `shape_predictor_68_face_landmarks.dat` file from the [dlib model repository](https://github.com/davisking/dlib-models). Extract the file and place it in the project directory.

## Usage
1. **Run the script:**

    Ensure your webcam is connected and working. Execute the script to start head movement detection:

    ```bash
    python Head_Movement.py
    ```

2. **Interact with the prompts:**

    The script will display prompts to move your head in different directions. Follow the instructions and see if your movements match the given prompt. The video feed will show visual feedback with green or red boxes based on your movements.

## Results
The processed video feed will be displayed in a window. No output files are saved; instead, the feedback is shown in real-time.

---

### Guidelines

- **Code Style:** Ensure your code adheres to the project’s coding style and conventions.
- **Documentation:** Include appropriate comments and documentation for your changes, especially if introducing new features or modifying existing ones.
- **Testing:** Write unit tests for any new functionality, and ensure that all existing tests pass before submitting your pull request.

## Contributing

We welcome contributions to improve these face recognition projects. Please follow the guidelines below for submitting your changes.

### How to Contribute

1. **Fork and clone** the repository.
2. **Create a new branch** for your changes.
3. **Implement and test** your changes.
4. **Submit a pull request** with a detailed description.

Thank you for your interest in contributing! 
---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For inquiries or suggestions, feel free to reach out:

**Anand Sundaramoorthy**  
**Email:** [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Enquiry%20About%20Machine%20Learning%20Python%20Codes&body=Hi%20Anand,%0A%0AI'm%20interested%20in%20learning%20more%20about%20the%20Machine%20Learning%20Python%20codes%20you%20developed.%20I%20have%20some%20questions%20and%20would%20like%20to%20discuss%20potential%20collaborations.%0A%0AThank%20you!%0A%0ABest%20regards,%0A[Your%20Name])

**LinkedIn:** [Anand Sundaramoorthy](https://www.linkedin.com/in/anands37/)





# Face Recognition Projects

Welcome to the Face Recognition Projects repository. This repository contains two distinct face recognition implementations: one for processing video uploads and another for live webcam feeds.

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

## Contributing

We welcome contributions to improve these face recognition projects. Please follow the guidelines below for submitting your changes.

### How to Contribute

1. **Fork and clone** the repository.
2. **Create a new branch** for your changes.
3. **Implement and test** your changes.
4. **Submit a pull request** with a detailed description.

---

### Guidelines

- **Code Style:** Ensure your code adheres to the project’s coding style and conventions.
- **Documentation:** Include appropriate comments and documentation for your changes, especially if introducing new features or modifying existing ones.
- **Testing:** Write unit tests for any new functionality, and ensure that all existing tests pass before submitting your pull request.

Thank you for your interest in contributing! Your efforts help make this project better for everyone.
---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For inquiries or suggestions, feel free to reach out:

**Anand Sundaramoorthy**  
**Email:** [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Inquiry%20About%20Face%20Recognition%20Project&body=Hi%20Anand,%0A%0AI'm%20interested%20in%20learning%20more%20about%20the%20Face%20Recognition%20Projects%20you%20developed%20during%20your%20Machine%20Learning%20Internship%20at%20Diffuse%20AI.%20I%20have%20some%20questions%20and%20would%20like%20to%20discuss%20potential%20collaborations.%0A%0AThank%20you!%0A%0ABest%20regards,%0A[Your%20Name])

**LinkedIn:** [Anand Sundaramoorthy](https://www.linkedin.com/in/anands37/)




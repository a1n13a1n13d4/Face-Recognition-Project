# Face Recognition Projects

Welcome to the Face Recognition Projects, part of my Machine Learning Internship at Diffuse AI. This repository contains two distinct projects focused on face recognition, each tailored for different input sources—video uploads and live webcam feeds.

## Table of Contents
- [Repo1A: Face Recognition from Uploaded Video](#repo1a-face-recognition-from-uploaded-video)
  - [About](#about-repo1a)
  - [Requirements](#requirements-repo1a)
  - [Installation](#installation-repo1a)
  - [Usage](#usage-repo1a)
  - [Results](#results-repo1a)
- [Repo1B: Live Face Recognition via Webcam](#repo1b-live-face-recognition-via-webcam)
  - [About](#about-repo1b)
  - [Requirements](#requirements-repo1b)
  - [Installation](#installation-repo1b)
  - [Usage](#usage-repo1b)
  - [Results](#results-repo1b)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Repo1A: Face Recognition from Uploaded Video

### About Repo1A

This project focuses on recognizing faces from an uploaded video file. The video is processed frame by frame to detect and identify faces using pre-trained models. The main objective is to extract faces from each frame and match them against a database of known faces.

### Requirements Repo1A

To run this project, you'll need:
- **Google Colab**: The project is designed to run in Google Colab for ease of use and to leverage the computational resources available on the platform.
- **Python 3.6+**: Ensure that your Colab environment is running Python 3.6 or higher.

### Installation Repo1A

1. **Clone the repository:**
   ```bash
   git clone https://github.com/a1n13a1n13d4/Machine-Learning-Intern-DiffuseAi.git
   cd Machine-Learning-Intern-DiffuseAi
   ```

2. **Open the project in Google Colab:**
   - Upload the `REPO1A.ANAND.Face_Recognition_From_Upload_Video` folder to your Google Drive.
   - Open `face_recognition_video.py` in Google Colab.

3. **Install the dependencies:**
   - Run the following commands in a Colab cell:
   ```python
   !pip install numpy opencv-python dlib face_recognition imutils
   ```

### Usage Repo1A

To run the face recognition on an uploaded video in Google Colab:

1. **Upload your video file**:
   - First, upload the video file to your Google Drive.

2. **Modify the script**:
   - Open `face_recognition_video.py` in Google Colab.
   - Modify the `video_path` variable in the script to point to the location of your uploaded video in Google Drive. For example:
     ```python
     video_path = '/content/drive/MyDrive/your_video.mp4'
     ```

3. **Run the script**:
   - Execute the entire script in Google Colab. The code will automatically process the video file and output the recognized faces.

### Results Repo1A

The processed video with recognized faces is saved in the specified output directory in Google Drive. Additionally, a log file is generated, detailing the number of faces detected, their locations in each frame, and the identities matched.

---

## Repo1B: Live Face Recognition via Webcam

### About Repo1B

This project implements real-time face recognition using a webcam. It continuously captures frames from the webcam, detects faces, and matches them against a pre-trained model's database of known faces. This project is ideal for applications requiring instant face recognition, such as security systems.

### Requirements Repo1B

To run this project, you'll need:
- **Anaconda Navigator**: The project is designed to run in an Anaconda environment to easily manage dependencies.
- **Python 3.6+**: Ensure that your Anaconda environment is running Python 3.6 or higher.

### Installation Repo1B

1. **Clone the repository:**
   ```bash
   git clone https://github.com/a1n13a1n13d4/Machine-Learning-Intern-DiffuseAi.git
   cd Machine-Learning-Intern-DiffuseAi
   ```

2. **Create and activate a new Anaconda environment:**
   ```bash
   conda create -n face_recognition_env python=3.6
   conda activate face_recognition_env
   ```

3. **Navigate to the Repo1B directory:**
   ```bash
   cd REPO1B.ANAND.Live_Face_Recognition_Via_Webcam
   ```

4. **Install the dependencies:**
   ```bash
   pip install numpy opencv-python dlib face_recognition imutils
   ```

### Usage Repo1B

To start live face recognition via your webcam:

1. Ensure your webcam is connected and properly configured.
2. Run the following command in Anaconda Prompt or terminal:
   ```bash
   python live_face_recognition.py
   ```

The script will launch a window showing the webcam feed with detected faces labeled in real-time.

### Results Repo1B

Real-time face recognition results are displayed directly in the webcam feed window. The program also logs the recognized identities and timestamps to a file for future reference.

---

## Contributing

We welcome contributions to improve the Face Recognition Projects! If you have an idea for a new feature, a bug fix, or improvements to the documentation, we encourage you to contribute. Here’s how you can get started:

1. **Fork the Repository:**
   - Click the "Fork" button at the top-right corner of this page to create a copy of this repository under your GitHub account.

2. **Clone Your Fork:**
   - Clone the forked repository to your local machine using the following command:
     ```bash
     git clone https://github.com/your-username/Machine-Learning-Intern-DiffuseAi.git
     cd Machine-Learning-Intern-DiffuseAi
     ```

3. **Create a New Branch:**
   - Create a new branch for your contribution:
     ```bash
     git checkout -b feature-or-bugfix-description
     ```

4. **Make Your Changes:**
   - Implement your changes, ensuring that your code follows the project’s coding standards and is well-documented.

5. **Test Your Changes:**
   - Thoroughly test your changes to ensure they work as expected and do not introduce new bugs.

6. **Commit and Push Your Changes:**
   - Commit your changes with a clear and concise commit message:
     ```bash
     git commit -m "Description of your changes"
     ```
   - Push your changes to your fork:
     ```bash
     git push origin feature-or-bugfix-description
     ```

7. **Submit a Pull Request:**
   - Navigate to the original repository on GitHub and click the "New Pull Request" button.
   - Provide a detailed description of your changes, including the problem your contribution addresses and how it improves the project.
   - Link any related issues in your pull request description.

8. **Review Process:**
   - Your pull request will be reviewed by the project maintainers. Please be responsive to any feedback or requests for changes.
   - Once your pull request is approved, it will be merged into the main branch.

### Guidelines

- **Code Style:** Ensure your code adheres to the project’s coding style and conventions.
- **Documentation:** Include appropriate comments and documentation for your changes, especially if introducing new features or modifying existing ones.
- **Testing:** Write unit tests for any new functionality, and ensure that all existing tests pass before submitting your pull request.

Thank you for your interest in contributing! Your efforts help make this project better for everyone.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any inquiries, suggestions, or further information about the Face Recognition Projects, feel free to reach out to me.

### About the Face Recognition Project

These projects were developed as part of my Machine Learning Internship at Diffuse AI. They focus on implementing and optimizing face recognition algorithms for different input sources, such as pre-recorded videos and live webcam feeds. The goal is to accurately identify and track faces using advanced machine learning models, providing real-time or post-processed recognition capabilities.

If you are interested in collaborating on similar projects or have questions about the implementation details, I'm always open to discussing new ideas and opportunities.

**Anand Sundaramoorthy**  
**Email:** [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Inquiry%20About%20Face%20Recognition%20Project&body=Hi%20Anand,%0A%0AI'm%20interested%20in%20learning%20more%20about%20the%20Face%20Recognition%20Projects%20you%20developed%20during%20your%20Machine%20Learning%20Internship%20at%20Diffuse%20AI.%20I%20have%20some%20questions%20and%20would%20like%20to%20discuss%20potential%20collaborations.%0A%0AThank%20you!%0A%0ABest%20regards,%0A[Your%20Name])

**LinkedIn:** [Anand Sundaramoorthy](https://www.linkedin.com/in/anands37/)

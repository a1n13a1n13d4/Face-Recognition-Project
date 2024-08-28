# Face Recognition Projects

Welcome to the Face Recognition Projects, part of my Machine Learning Internship at Diffuse AI. This repository contains two distinct projects focused on face recognition, each tailored for different input sources—video uploads and live webcam feeds.

## Table of Contents
- [Repo1A: Face Recognition from Uploaded Video](#repo1a-face-recognition-from-uploaded-video)
  - [About](#about-repo1a)
  - [Installation](#installation-repo1a)
  - [Usage](#usage-repo1a)
  - [Results](#results-repo1a)
- [Repo1B: Live Face Recognition via Webcam](#repo1b-live-face-recognition-via-webcam)
  - [About](#about-repo1b)
  - [Installation](#installation-repo1b)
  - [Usage](#usage-repo1b)
  - [Results](#results-repo1b)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Repo1A: Face Recognition from Uploaded Video

### About Repo1A

This project focuses on recognizing faces from an uploaded video file. The video is processed frame by frame to detect and identify faces using pre-trained models. The main objective is to extract faces from each frame and match them against a database of known faces.

### Installation Repo1A

1. **Clone the repository:**
   ```bash
   git clone https://github.com/a1n13a1n13d4/Machine-Learning-Intern-DiffuseAi.git
   cd Machine-Learning-Intern-DiffuseAi
   ```

2. **Navigate to the Repo1A directory:**
   ```bash
   cd REPO1A.ANAND.Face_Recognition_From_Upload_Video
   ```

3. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage Repo1A

To run the face recognition on an uploaded video:

1. Place the video file in the `input/` directory.
2. Run the following command:
   ```bash
   python face_recognition_video.py --video_path input/your_video.mp4
   ```

This will process the video and output the recognized faces with labels in the `output/` directory.

### Results Repo1A

The processed video with recognized faces is saved in the `output/` directory. Additionally, a log file is generated, detailing the number of faces detected, their locations in each frame, and the identities matched.

---

## Repo1B: Live Face Recognition via Webcam

### About Repo1B

This project implements real-time face recognition using a webcam. It continuously captures frames from the webcam, detects faces, and matches them against a pre-trained model's database of known faces. This project is ideal for applications requiring instant face recognition, such as security systems.

### Installation Repo1B

1. **Clone the repository:**
   ```bash
   git clone https://github.com/a1n13a1n13d4/Machine-Learning-Intern-DiffuseAi.git
   cd Machine-Learning-Intern-DiffuseAi
   ```

2. **Navigate to the Repo1B directory:**
   ```bash
   cd REPO1B.ANAND.Live_Face_Recognition_Via_Webcam
   ```

3. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Usage Repo1B

To start live face recognition via your webcam:

1. Ensure your webcam is connected and properly configured.
2. Run the following command:
   ```bash
   python live_face_recognition.py
   ```

The script will launch a window showing the webcam feed with detected faces labeled with their identities in real-time.

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
**Email:** [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com)  
**LinkedIn:** [Anand Sundaramoorthy](https://www.linkedin.com/in/anands37/)


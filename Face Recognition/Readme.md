# Face Recognition via Camera

A simple face recognition project built with Python and OpenCV.
The program uses a reference image to recognize a specific person through a webcam in real time.

## Features

* Real-time face detection
* Face recognition using a reference image
* Webcam support
* Displays the detected person's name or "Unknown"

## Technologies

* Python
* OpenCV
* face_recognition

## Installation

Install the required libraries:

```bash
pip install opencv-python
pip install face-recognition
```

## How to Run

1. Put the reference image inside the `images` folder.
2. Run the Python script.
3. The webcam will start automatically.
4. Press `Q` to close the program.

## Project Structure

```text
face-recognition/
├── main.py
├── requirements.txt
├── README.md
└── images/
    └── image1.jpg
```

## Demo

The program detects faces through the webcam and identifies whether the detected person matches the reference image.

-برنامه تشخیص چهره با python و opencv
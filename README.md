# Face Recognition Attendance System

## Overview
This project is a face recognition-based attendance system built using Python, OpenCV, and the `face_recognition` library. The application enables users to log in by recognizing their faces and registers new users into the system. Attendance logs are saved in a `log.txt` file, recording the name and date/time of successful logins.

## Features
- **Face Recognition for Login**: Detects and recognizes registered users' faces and logs attendance with timestamps.
- **User Registration**: Captures and saves new users' face images for future recognition.
- **Live Webcam Feed**: Streams the webcam video feed within the application.
- **Attendance Logs**: Keeps attendance records in a `log.txt` file.

## Project Structure
- `db/`: Directory to store user face images.
- `log.txt`: File to log attendance records.
- `util.py`: Utility functions for button creation, image labeling, and message display.
- `main.py`: Main script containing the application logic.

## Dependencies
- **Python 3.x**
- Libraries:
  - `tkinter`: For GUI elements.
  - `cv2 (OpenCV)`: For webcam integration and image processing.
  - `PIL (Pillow)`: For handling image objects in the GUI.
  - `face_recognition`: For facial recognition.
  - `datetime`: For logging timestamps.
  - `subprocess`: For executing external face recognition commands.

## How It Works

### Login Process:
1. Captures a frame from the webcam.
2. Uses the `face_recognition` library to match the face against registered user images in the `db` directory.
3. Displays a welcome message and logs the event if a match is found.
4. Displays an error message if no match is found.

### User Registration:
1. Captures a frame from the webcam.
2. Prompts the user to input their name.
3. Saves the captured image in the `db` directory with the entered name as the filename.

## Usage Instructions

### Set Up:
1. Ensure Python and all dependencies are installed.
2. Create a directory named `db` in the same location as the script.
3. Ensure `face_recognition` is installed and configured.

### Run the Application:
Execute the script using the command:
```bash
python main.py

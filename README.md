# Face Recognition Attendance and Automation Suite

## Overview
This project is a comprehensive attendance management system powered by face recognition and automation workflows. It combines Python-based face recognition technology with UIPath automation tools to streamline attendance tracking, log conversion, and deduction calculation.  

## Features
### Face Recognition Attendance System (Python)
- **Login with Face Recognition**: Identifies users via their facial features and logs attendance.  
- **User Registration**: Allows new users to register by capturing their face and saving it for future recognition.  
- **Attendance Logs**: Records name and timestamp in `log.txt` for each successful login.  
- **Real-time Webcam Feed**: Streams live video feed directly in the application interface.  

### Automation Processes (UIPath)
1. **Face Recognition Process Automation**:  
   - Automates the execution of the face recognition application.  
   - Opens the Python script, manages inputs, and handles application flow.  

2. **Log Conversion and Deduction Calculation**:  
   - Converts the `log.txt` attendance file into an Excel file.  
   - Automatically calculates deductions based on predefined rules.  
   - Generates a clean, formatted Excel sheet for further analysis.  

## Project Structure
### Python-Based Attendance System
- **db/**: Directory containing registered user face images.  
- **log.txt**: File where attendance records are stored.  
- **util.py**: Utility functions for GUI components.  
- **main.py**: Main application script for face recognition and GUI.  

### UIPath Automation
- **Face Recognition Automation**: Manages the execution of the Python-based attendance system.  
- **Log Conversion Automation**: Automates the transformation of `log.txt` into an Excel file and calculates deductions.  

## Prerequisites
### Python
- Python 3.x installed.  
- Required Libraries:  
  - `tkinter`, `cv2`, `PIL`, `face_recognition`, `subprocess`, `datetime`.  

### UIPath
- Installed UIPath Studio with active license.  
- Basic understanding of creating and running workflows in UIPath.  

## Setup and Usage
### Step 1: Run the Python Attendance System
1. Clone the repository and navigate to the Python project directory.  
2. Install the required Python libraries using `pip install -r requirements.txt`.  
3. Create a `db` folder for storing face images.  
4. Run the Python application using `python main.py`.  

### Step 2: Automate with UIPath
1. Open the provided UIPath projects in UIPath Studio.  
2. Configure paths to match your setup (Python script location and log file path).  
3. Execute the workflows:  
   - **Face Recognition Process Automation**: Launches the Python system.  
   - **Log Conversion Automation**: Processes the log file into an Excel sheet.  

## Outputs
- **Python Application**:  
  - Real-time face recognition for login.  
  - Updated `log.txt` file with attendance details.  

- **UIPath Automation**:  
  - Excel file containing attendance logs.  
  - Deduction calculations based on attendance records.  

## Limitations
- Requires clear and well-lit images for accurate face recognition.  
- Deduction rules need to be predefined and manually updated in UIPath.  

## Future Enhancements
- Add database integration for scalable attendance storage.  
- Enhance face recognition accuracy with preprocessing techniques.  
- Expand UIPath workflows for generating detailed attendance reports.  

---

For any questions or contributions, feel free to contact the project author.  

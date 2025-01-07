import tkinter as tk
import cv2
from PIL import Image, ImageTk
import util  # Custom utility functions for GUI elements like buttons and labels
import os
import face_recognition  # Library for face recognition tasks
import subprocess
import datetime

# To access the same directory of the file 
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Initialize the log file to store login activity with headers
log_path = "log.txt"
with open(log_path, 'w') as f:
    f.write("Name,Date\n")  # Write header to the log file
    f.close()

# Define the main application class
class App:
    def __init__(self):
        # Initialize the main application window
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")  # Set the size and position of the main window

        # Add login button to the main window
        self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
        self.login_button_main_window.place(x=750, y=200)  # Position the login button

        # Add register new user button to the main window
        self.register_new_user_button_main_window = util.get_button(self.main_window, 'register new user', 'gray',
                                                                    self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=300)  # Position the register button

        # Add a label to display the webcam feed
        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)  # Position the webcam feed

        # Start the webcam feed
        self.add_webcam(self.webcam_label)

        # Set up the database directory for storing registered user images
        self.db_dir = "db"
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)  # Create the database directory if it doesn't exist

        # Path to the log file
        self.log_path = "log.txt"

    # Method to add webcam feed to a label
    def add_webcam(self, label):
        if 'cap' not in self.__dict__:
            self.cap = cv2.VideoCapture(0)  # Open the default camera
        self._label = label
        self.process_webcam()  # Start processing the webcam feed

    # Method to process the webcam feed
    def process_webcam(self):
        ret, frame = self.cap.read()  # Capture a frame from the webcam

        self.most_recent_capture_arr = frame  # Store the most recent frame
        img_ = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)  # Convert the frame to RGB format
        self.most_recent_capture_pil = Image.fromarray(img_)  # Convert the frame to a PIL image
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)  # Convert the PIL image to an ImageTk object
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)  # Update the label with the new frame

        self._label.after(10, self.process_webcam)  # Schedule the next frame update

    # Method to handle the login process
    def login(self):
        unknown_img_path = "./.tmp.jpg"  # Temporary file to store the captured frame
        cv2.imwrite(unknown_img_path, self.most_recent_capture_arr)  # Save the frame to the temporary file

        # Run face recognition to match the captured face with the database
        output = str(subprocess.check_output(['face_recognition', self.db_dir, unknown_img_path]))
        name = output.split(',')[1][:-5]  # Extract the name from the output

        # Check if the face is recognized
        if name in ['unknown_person', 'no_persons_found']:
            util.msg_box('Ups...', 'Unknown user. Please register new user or try again.')
        else:
            util.msg_box('Welcome !', f'Welcome , {name}.')  # Display a welcome message
            with open(self.log_path, 'a') as f:
                current_time = datetime.datetime.now()
                formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')  # Format the current time
                f.write(f'{name},{formatted_time}\n')  # Log the user's name and time
                f.close()

        # Note: Temporary file removal is commented out
        # os.remove(unknown_img_path)

    # Method to open the register new user window
    def register_new_user(self):
        self.register_new_user_window = tk.Toplevel(self.main_window)  # Create a new window
        self.register_new_user_window.geometry("1200x520+370+120")  # Set the size and position of the window

        # Add "Accept" button to save the new user's data
        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)  # Position the button

        # Add "Try Again" button to close the window
        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Try again', 'red', self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)  # Position the button

        # Add a label to display the captured image
        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)  # Position the label

        # Display the current webcam frame in the label
        self.add_img_to_label(self.capture_label)

        # Add an entry box for the username
        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=150)  # Position the entry box

        # Add a text label to prompt for the username
        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, 'Please, \ninput username:')
        self.text_label_register_new_user.place(x=750, y=70)  # Position the text label

    # Method to update the label with the captured frame
    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)  # Convert the frame to ImageTk
        label.imgtk = imgtk
        label.configure(image=imgtk)  # Update the label with the frame

        self.register_new_user_capture = self.most_recent_capture_arr.copy()  # Save the frame for registration

    # Method to close the register new user window
    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    # Method to save the new user's data
    def accept_register_new_user(self):
        name = self.entry_text_register_new_user.get(1.0, "end-1c")  # Get the username from the entry box
        cv2.imwrite(os.path.join(self.db_dir, f'{name}.jpg'), self.register_new_user_capture)  # Save the image

        util.msg_box('Success!', 'User was registered successfully !')  # Display success message
        self.register_new_user_window.destroy()  # Close the window

    # Method to start the application
    def start(self):
        self.main_window.mainloop()  # Start the Tkinter main loop

# Run the application if the script is executed
if __name__ == "__main__":
    app = App()
    app.start()

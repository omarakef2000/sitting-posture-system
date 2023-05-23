import face_recognition
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

import subprocess
# Initialize tkinter
root = tk.Tk()

# Create arrays to store user data
user_names = []
user_image_paths = []

# Function to add user
def add_user():
    name = entry_name.get()
    image_path = entry_image_path.get()
    user_names.append(name)
    user_image_paths.append(image_path)
    entry_name.delete(0, tk.END)
    entry_image_path.delete(0, tk.END)
    print("User added successfully.")

# Function to delete user
def delete_user():
    name = entry_name.get()
    if name in user_names:
        index = user_names.index(name)
        user_names.pop(index)
        user_image_paths.pop(index)
        entry_name.delete(0, tk.END)
        print("User deleted successfully.")
    else:
        print("User not found.")

# Function to update user image path
def update_image_path():
    name = entry_name.get()
    new_image_path = entry_image_path.get()
    if name in user_names:
        index = user_names.index(name)
        user_image_paths[index] = new_image_path
        entry_name.delete(0, tk.END)
        entry_image_path.delete(0, tk.END)
        print("Image path updated successfully.")
    else:
        print("User not found.")

# Function to display all users
def display_users():
    if len(user_names) > 0:
        print("User List:")
        for i, name in enumerate(user_names):
            print(f"{i+1}. {name}: {user_image_paths[i]}")
    else:
        print("No users found.")

# Function to perform face recognition
def recognize_faces():
    video_capture = cv2.VideoCapture(0)

    # Load known face encodings and names
    known_face_encodings = []
    known_face_names = []
    for image_path in user_image_paths:
        image = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
    known_face_names = user_names

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Resize frame for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color to RGB color
        rgb_small_frame = small_frame[:, :, ::-1]

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face matches any known face
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"

            # Use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with the name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Exit condition
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and destroy the windows
    video_capture.release()
    cv2.destroyAllWindows()
def run_python_file():
    # Replace "path_to_script.py" with the actual path to your Python file
    script_path = "C:/Users/20109/Desktop/hci project/GazeTracking-master/example.py"
    
    # Execute the Python file
    subprocess.run(["python", script_path])
def end_process():
    # Replace "path_to_script.py" with the actual path to your Python file
    script_path = "C:/Users/20109/Desktop/scenario/second thing.py"
    
    # Execute the Python file
    subprocess.run(["python", script_path])
def scenario():
    # Replace "path_to_script.py" with the actual path to your Python file
    script_path = "C:/Users/20109/Desktop/hci project/import cv22.py"
    
    # Execute the Python file
    subprocess.run(["python", script_path])
def time_to_play():
    # Replace "path_to_script.py" with the actual path to your Python file
    script_path = "C:/Users/20109/Desktop/hci project/red balls.py"
    
    # Execute the Python file
    subprocess.run(["python", script_path])

# Create GUI

root.title("Face Recognition with CRUD Operations")
root.geometry("400x400")

# Create labels
label_name = tk.Label(root, text="Name:")
label_name.pack()
label_image_path = tk.Label(root, text="Image Path:")
label_image_path.pack()

# Create entry fields
entry_name = tk.Entry(root)
entry_name.pack()
entry_image_path = tk.Entry(root)
entry_image_path.pack()

# Create buttons
button_add_user = tk.Button(root, text="Add User", command=add_user)
button_add_user.pack()
button_delete_user = tk.Button(root, text="Delete User", command=delete_user)
button_delete_user.pack()
button_update_image_path = tk.Button(root, text="Update Image Path", command=update_image_path)
button_update_image_path.pack()
button_display_users = tk.Button(root, text="Display Users", command=display_users)
button_display_users.pack()
button_recognize_faces = tk.Button(root, text="Recognize Faces", command=recognize_faces)
button_recognize_faces.pack()
button_facegazing = tk.Button(root, text="face gazing", command=run_python_file)
button_facegazing.pack()
button_scenario = tk.Button(root, text="scenario", command=scenario)
button_scenario.pack()
button_endexp = tk.Button(root, text="end experiment", command=end_process)
button_endexp.pack()
button_play = tk.Button(root, text="time to play", command=time_to_play)
button_play.pack()
# Start the tkinter event loop
root.mainloop()

# Import necessary libraries
import cv2  # For webcam and image handling
import numpy as np  # For numerical operations
import face_recognition  # For face recognition functions
import os  # For directory handling
from datetime import datetime  # For recording time

# --- Load known images ---
path = 'imageattendance'  # Folder where known images are stored
images = []  # List to store image data
classnames = []  # List to store corresponding names

# Read all image files from the folder
mylist = os.listdir(path)
print("Found images:", mylist)

for cls in mylist:
    curImg = cv2.imread(f'{path}/{cls}')  # Read each image
    if curImg is not None:
        images.append(curImg)  # Add image to list
        classnames.append(os.path.splitext(cls)[0])  # Save filename without extension as class name
    else:
        print(f"Warning: Unable to load image {cls}")

print("Class names:", classnames)

# --- Function to find encodings for all known images ---
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
        encode = face_recognition.face_encodings(img)[0]  # Get encoding
        encodeList.append(encode)
    return encodeList

# --- Function to mark attendance in CSV ---
def markAttendance(name):
    with open('attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.strip().split(',')  # Added .strip() to avoid issues
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')  # Current time
            f.writelines(f'\n{name},{dtString}')  # Write new entry

# --- Generate known encodings ---
encodeListKnown = findEncodings(images)
print(f"Total encodings created: {len(encodeListKnown)}")

# --- Start live webcam feed ---
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()  # Capture frame
    if not success:
        print("Failed to capture frame")
        break

    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)  # Resize for faster processing
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)  # Convert to RGB

    facesCurFrame = face_recognition.face_locations(imgS)  # Locate faces in current frame
    encodeCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)  # Get encodings

    for encodeFace, faceloc in zip(encodeCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)  # Check matches
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)  # Calculate distances

        matchIndex = np.argmin(faceDis)  # Index of best match (smallest distance)

        if matches[matchIndex]:  # If match is true
            name = classnames[matchIndex].upper()  # Get the name and capitalize
            print(name)

            # Coordinates of face location
            y1, x2, y2, x1 = faceloc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4  # Scale back up to original size

            # Draw rectangle around face
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            # Draw filled rectangle below face
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0,255,0), cv2.FILLED)
            # Put name text
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

            # Mark attendance
            markAttendance(name)

    # Show the webcam output
    cv2.imshow('Webcam', img)

    # Break loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()


# Import required libraries
import cv2  # OpenCV for image handling
import numpy as np  # Numpy for array handling (not heavily used here)
import face_recognition  # Face recognition library
from face_recognition import face_distance  # Import specific function (optional, not necessary here)

# Load the image of Elon Musk
imgElon = face_recognition.load_image_file('imagebasics/Elon Musk.jpg.jpg')
# Convert image from BGR (OpenCV default) to RGB (face_recognition needs RGB)
imgElon = cv2.cvtColor(imgElon, cv2.COLOR_BGR2RGB)

# Load the test image (Bill Gates)
imgTest = face_recognition.load_image_file('imagebasics/Bill Gtes.jpg')
# Convert test image from BGR to RGB
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# Find face location in the Elon image
faceloc = face_recognition.face_locations(imgElon)[0]  # returns top, right, bottom, left
# Generate 128-d face encoding for Elon
encodeElon = face_recognition.face_encodings(imgElon)[0]
# Draw rectangle around Elon's face
cv2.rectangle(imgElon, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (255, 0, 255), 2)

# Find face location in the Test image
faceTest = face_recognition.face_locations(imgTest)[0]
# Generate 128-d face encoding for Test image
encodeTest = face_recognition.face_encodings(imgTest)[0]
# Draw rectangle around face in Test image
cv2.rectangle(imgTest, (faceTest[3], faceTest[0]), (faceTest[1], faceTest[2]), (255, 0, 255), 2)

# Compare the faces: check if Elon and Test image are same
results = face_recognition.compare_faces([encodeElon], encodeTest)
# Find the face distance (lower = more similar)
faceDis = face_recognition.face_distance([encodeElon], encodeTest)

# Print whether match found and distance
print(results, faceDis)

# Put the result and distance on the Test image
cv2.putText(imgTest, f'{results} {round(faceDis[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)

# Show the original Elon Musk image with rectangle
cv2.imshow('Elon Musk', imgElon)
# Show the Test image with rectangle and match result
cv2.imshow('Elon Test', imgTest)

# Wait until a key is pressed
cv2.waitKey(0)

📸 Smart Face Recognition Attendance System

# 📸 Face Recognition + Attendance System
**A Real-Time Face Recognition Attendance System built using Python, OpenCV, and the face_recognition library.**

---

## 🔥 Project Overview

This project uses computer vision techniques to:
- Detect faces in real-time from a webcam.
- Recognize faces by matching them against pre-saved images.
- Mark attendance automatically by storing names and timestamps into a CSV file.

No manual input required — just show your face to the camera and get marked present! ✅

---

## 🛠️ Tech Stack
- **Python 3**
- **OpenCV** (for image processing and webcam feed)
- **face_recognition** (for face encoding and matching)
- **NumPy** (for numerical operations)
- **Datetime** (for timestamp generation)
- **CSV** file (for attendance records)

---

## 📂 Project Structure

```
Face-Recognition-Attendance/
├── imageattendance/      # Folder containing known faces (images)
│    ├── Elon Musk.jpg
│    ├── Bill Gates.jpg
│    └── Your Images...
├── attendance.csv        # CSV file where attendance is stored
├── attendanceproject.py  # Main Python script
└── README.md              # Project documentation
```

---

## 🚀 How to Run the Project

1. **Clone the repository**  
   ```
   git clone https://github.com/your-username/Face-Recognition-Attendance.git
   ```

2. **Install the required libraries**  
   ```
   pip install opencv-python face_recognition numpy
   ```

3. **Prepare known images**  
   - Add clear images of faces you want to recognize inside the `imageattendance/` folder.

4. **Create an empty `attendance.csv` file**  
   - Just create a file named `attendance.csv` with a header like:
     ```
     Name,Time
     ```

5. **Run the script**  
   ```
   python attendanceproject.py
   ```

6. **Show your face to the webcam! 🎥**  
   - If your face matches a known face, your name and timestamp will be saved in `attendance.csv`.

---

## ✨ Features
- Real-time face detection and recognition.
- Attendance marked instantly with date and time.
- Very fast and efficient face matching.
- Automatically ignores repeated entries for the same person.
- Simple and clean code structure (easy to understand and modify).

---

## 📸 Example

| Webcam Feed | Attendance CSV |
|:-----------:|:--------------:|
| ![Webcam Screenshot](https://via.placeholder.com/300x200.png?text=Webcam+Feed) | ![CSV Screenshot](https://via.placeholder.com/300x200.png?text=Attendance+CSV) |

*(You can replace above placeholders with real screenshots after running.)*

---

## 🧠 Future Improvements
- Add **Date** column along with time.
- Add **GUI interface** (using Tkinter or PyQt).
- Send real-time **email notifications** when attendance is marked.
- Deploy this system for **classroom or office use**.

---

## 🤝 Contributions
Contributions are always welcome!  
Feel free to fork this repo, make your changes, and create a pull request.

---

## 📄 License
This project is open-source and free to use under the [MIT License](LICENSE).

---

# 👨‍💻 Made with ❤️ by Kavya GR


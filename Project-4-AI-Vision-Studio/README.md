# 🧠 AI Vision Studio

AI Vision Studio is a full-stack **AI-powered image classification web application** built as the final project of my AI internship at DecodeLabs.

The application allows users to upload an image and uses a pre-trained **ResNet-50 deep learning model** to identify the most likely objects or categories in the image.

Unlike a basic Streamlit prototype, this project uses a separate **Flask backend** and a custom **HTML, CSS, and JavaScript frontend** to demonstrate how an AI model can be integrated into a complete web application.

---

## ✨ Features

* 📤 Image upload
* 🖱️ Drag-and-drop image support
* 🖼️ Instant image preview
* 🤖 AI-powered image classification
* 📊 Top 5 predictions
* 📈 Confidence scores
* ⚡ Processing time measurement
* 📝 Prediction history during the session
* 📥 Downloadable AI analysis report
* 🔍 Image type and file-size validation
* ⚠️ User-friendly error handling
* 📱 Responsive modern interface
* ❤️ Clean AI dashboard design

---

## 🧠 AI Model

The application uses **ResNet-50**, a deep convolutional neural network available through PyTorch's torchvision library.

### Model

**ResNet-50**

### Dataset

**ImageNet**

### Task

**Image Classification**

The model returns the five most probable classes for the uploaded image along with their confidence scores.

---

## 🏗️ Project Architecture

```text
User
 │
 │ Upload Image
 ▼
HTML / CSS / JavaScript Frontend
 │
 │ POST /predict
 ▼
Flask Backend
 │
 │ Image Validation
 ▼
Image Preprocessing
 │
 ▼
ResNet-50 Model
 │
 │ AI Inference
 ▼
Top 5 Predictions
 │
 ▼
JSON Response
 │
 ▼
Interactive Results Dashboard
```

---

## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript
* Responsive UI
* Drag & Drop API
* Fetch API

### Backend

* Python
* Flask
* REST API

### AI / Machine Learning

* PyTorch
* Torchvision
* ResNet-50
* ImageNet

### Other

* Pillow
* Git
* GitHub

---

## 📂 Project Structure

```text
Project-4-AI-Vision-Studio/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    │
    ├── css/
    │   └── style.css
    │
    └── js/
        └── script.js
```

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Abeeha-13/DecodeLabs-Internship.git
```

### 2. Open the project folder

```bash
cd DecodeLabs-Internship/Project-4-AI-Vision-Studio
```

### 3. Create a virtual

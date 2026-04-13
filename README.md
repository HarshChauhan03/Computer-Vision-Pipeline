# 🚀 Computer Vision Pipeline – Image Classification

## 📌 Overview

This project demonstrates a complete **Computer Vision pipeline** for image classification using Convolutional Neural Networks (CNN).

The pipeline follows a structured approach used in real-world computer vision systems, including data collection, preprocessing, model building, training, evaluation, and deployment.

The final model is deployed using a **Streamlit web application**, allowing users to upload images and get real-time predictions.

---

## 🎯 Objective

The objective of this project is to:

- Build an end-to-end Computer Vision pipeline  
- Process and prepare image data  
- Develop a CNN-based model  
- Train and evaluate the model  
- Improve model performance  
- Deploy the model using a web interface  

---

## 🧠 Computer Vision Pipeline


Problem Definition
↓
Data Collection
↓
Data Annotation (Labeling)
↓
Data Preprocessing
↓
Data Augmentation
↓
Model Building (CNN)
↓
Model Training
↓
Model Evaluation
↓
Model Optimization
↓
Model Saving
↓
Deployment (Streamlit App)


---

## 📂 Project Structure


Computer-Vision-Project/

├── dataset/
│ ├── train/
│ └── test/

├── 01_load_dataset.py
├── 02_preprocessing.py
├── 03_visualization.py
├── 04_model_building.py
├── 05_model_training.py
├── 06_model_evaluation.py
├── 07_model_saving.py
├── app.py

├── model.h5
├── requirements.txt
└── README.md


---

## ⚙️ Pipeline Steps

### 1️⃣ Problem Definition
- Define computer vision task  
- Example: Image Classification  

---

### 2️⃣ Data Collection
- Collect image dataset  
- Organize into class-based folders  

---

### 3️⃣ Data Annotation
- Assign labels to images  
- Folder-based labeling (class = folder)  

---

### 4️⃣ Data Preprocessing
- Resize images to fixed size (224x224)  
- Normalize pixel values (0–255 → 0–1)  
- Convert images to numerical format  

---

### 5️⃣ Data Augmentation
- Apply transformations (flip, rotate, zoom)  
- Improve model generalization  

---

### 6️⃣ Model Building (CNN)
- Build Convolutional Neural Network  
- Use Conv2D, MaxPooling, Flatten layers  
- Add Dense layers for classification  

---

### 7️⃣ Model Training
- Train model using training dataset  
- Validate using test dataset  
- Monitor accuracy and loss  

---

### 8️⃣ Model Evaluation
- Analyze performance using accuracy and loss  
- Detect overfitting and underfitting  

---

### 9️⃣ Model Optimization
- Improve model using tuning techniques  
- Apply dropout, augmentation, or transfer learning  

---

### 🔟 Model Saving
- Save trained model  
- Output file: `model.h5`  

---

### 1️⃣1️⃣ Deployment
- Build Streamlit web application  
- Upload image → model prediction  
- Display result  

---

## 🛠 Technologies Used

- Python  
- OpenCV  
- TensorFlow / Keras  
- NumPy  
- Matplotlib  
- Pillow (PIL)  
- Streamlit  

---

## 💻 Installation

Install required libraries:


pip install tensorflow opencv-python numpy matplotlib pillow streamlit


---

## ▶️ Running the Pipeline

Run scripts in order:

```bash
python 01_load_dataset.py
python 02_preprocessing.py
python 03_visualization.py
python 04_model_building.py
python 05_model_training.py
python 06_model_evaluation.py
python 07_model_saving.py
▶️ Run Application
streamlit run app.py

Open in browser:

http://localhost:8501
``` id="cv-url"

---

## 📊 Dataset

The dataset is structured as:


dataset/
├── train/
│ ├── class1/
│ └── class2/
├── test/
│ ├── class1/
│ └── class2/


Example:
- Cat  
- Dog  

---

## 🌍 Applications

- Image classification systems  
- Object detection  
- Face recognition  
- Medical image analysis  
- Autonomous driving systems  

---

## 🎓 Learning Outcomes

- Computer Vision pipeline understanding  
- Image preprocessing techniques  
- CNN model development  
- Model training and evaluation  
- Deployment using Streamlit  

---

## 👨‍💻 Author

Harsh Chauhan  
AI & Data Science

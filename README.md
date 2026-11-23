# 👤 Face Recognition and Verification

**Face Recognition using MTCNN, FaceNet and KNN**

Built with Python and Deep Learning

---

##  Overview

This project implements an end-to-end face recognition and verification system using **MTCNN for face detection, FaceNet for feature extraction and KNN for identity recognition**.

It processes facial images, generates numerical embeddings and identifies individuals by comparing facial features. Cosine similarity is additionally used for identity verification.

---

## 🎯 Problem Statement

Identifying and verifying individuals from large image datasets can be challenging without an automated recognition system.

This project addresses the problem by combining deep learning-based facial feature extraction with machine learning classification to create a structured face recognition pipeline.

---

## ✨ Key Features

- 📋 Automated metadata generation with timestamps.
- 🗂️ Structured dataset organization using constituency and voter ID.
- 👤 Face detection and cropping using MTCNN.
- 🧠 Facial feature extraction using FaceNet.
- 🔢 128-dimensional facial embedding generation.
- 🤖 Identity recognition using KNN classification.
- 🔍 Identity verification using cosine similarity.
- 🖥️ Interactive interface using Streamlit.

---

## 🏗️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming |
| OpenCV | Image processing |
| MTCNN | Face detection |
| FaceNet | Facial feature extraction |
| NumPy | Numerical computations |
| Pandas | Dataset and metadata management |
| Scikit-learn | KNN classification |
| Streamlit | User interface |

---

## 🧩 System Architecture

```text
       Input Images
             |
             v
     Metadata Generation
             |
             v
       Face Detection
           (MTCNN)
             |
             v
       Face Cropping
             |
             v
     Feature Extraction
          (FaceNet)
             |
             v
     Facial Embeddings
             |
             v
      KNN Classification
             |
             v
    Cosine Similarity
             |
             v
   Identity Verification
```

---

## ⚙️ Methodology

1. **Metadata Generation:** Extracts image information and organizes records into a CSV file.
2. **Face Detection:** Uses MTCNN to detect and crop faces from images.
3. **Feature Extraction:** Uses FaceNet to generate 128-dimensional facial embeddings.
4. **Recognition:** Trains a KNN classifier using the extracted embeddings.
5. **Verification:** Uses cosine similarity to compare embeddings and determine identity matches.

---

## 📂 Project Structure

```text
Face-Recognition-and-Verification/
│
├── Fake vote detection.ipynb
├── SIMULATING.ipynb
├── UI(streamlit).py
├── originaldataset.zip
├── LICENSE
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Required Python libraries

### 1. Clone the Repository

```bash
git clone https://github.com/diyadineep/Face-Recognition-and-Verification-using-MTCNN-FaceNet-and-KNN.git
cd Face-Recognition-and-Verification-using-MTCNN-FaceNet-and-KNN
```

### 2. Install Dependencies

```bash
pip install opencv-python mtcnn numpy pandas scikit-learn streamlit
```

Install any additional dependencies required by the FaceNet implementation.

### 3. Run the Main Notebook

Open `Fake vote detection.ipynb` using Jupyter Notebook or Google Colab and execute the cells in sequence.

### 4. Launch the Streamlit Interface

```bash
streamlit run "UI(streamlit).py"
```

---

## 🛣️ Future Scope

- Real-time face recognition through webcam input.
- Improved recognition performance on varied lighting and facial conditions.
- Optimization for larger image datasets.
- Enhanced verification and user interface capabilities.

# CIFAR-10 Image Classification using CNN — Project Brief

## 1. Project Title

**CIFAR-10 Image Classification Using Convolutional Neural Network (CNN)**

---

## 2. Project Overview

This project is an AI/Deep Learning image classification system developed using Python and PyTorch. The system is trained on the CIFAR-10 dataset to automatically classify images into one of 10 predefined categories.

The trained CNN model is integrated with a Streamlit web interface, where users can upload an image and receive the predicted class along with its confidence score.

**Live Demo:**
[CIFAR-10 Image Classifier — Streamlit App](https://cifar10-image-classifier.streamlit.app)

---

## 3. Objective

The main objectives of this project are:

- To understand the complete CNN image-classification pipeline.
- To preprocess and prepare CIFAR-10 image data.
- To build and train a custom CNN using PyTorch.
- To evaluate model performance using test data.
- To analyze performance using a confusion matrix and class-wise accuracy.
- To save the trained model.
- To deploy the model through a user-friendly Streamlit UI.

---

## 4. Dataset

The project uses the **CIFAR-10 dataset**.

It contains **10 image classes**:

| Class | Description |
|-------|-------------|
| ✈️ | Airplane |
| 🚗 | Automobile |
| 🐦 | Bird |
| 🐱 | Cat |
| 🦌 | Deer |
| 🐶 | Dog |
| 🐸 | Frog |
| 🐴 | Horse |
| 🚢 | Ship |
| 🚚 | Truck |

- Each image has a resolution of **32 × 32 pixels** with **3 RGB channels**.
- For the training performed in this project, **40,000 training images** were used, with **10,000 test images** used for evaluation.

---

## 5. Data Preprocessing

The original CIFAR-10 data was stored in serialized batch files.

The preprocessing pipeline included:

```
Raw CIFAR-10 Data
       ↓
Load Pickle Batches
       ↓
Separate Images & Labels
       ↓
Reshape to 32 × 32 × 3
       ↓
Convert to Float32
       ↓
Normalize Pixel Values
0–255 → 0–1
       ↓
Convert to PyTorch Tensor
       ↓
DataLoader
```

The images were converted into the PyTorch format: **3 × 32 × 32**

---

## 6. CNN Architecture

A custom CNN was developed for classification.

### Convolution Layers

**Input: 3 × 32 × 32**

```
Conv2D: 3 → 32
ReLU
MaxPool

Conv2D: 32 → 64
ReLU
MaxPool

Conv2D: 64 → 128
ReLU
MaxPool
```

After the convolution layers: **128 × 4 × 4** which gives **2048 features**

### Fully Connected Layers

```
Linear: 2048 → 256
ReLU
Linear: 256 → 10
```

The final 10 outputs correspond to the 10 CIFAR-10 classes.

---

## 7. Training

The model was trained using:

| Parameter | Value |
|-----------|-------|
| Framework | PyTorch |
| Optimizer | Adam |
| Loss Function | CrossEntropyLoss |
| Epochs | 10 |
| Batch Size | 64 initially; 128 in the T4 GPU training version |
| Hardware | NVIDIA Tesla T4 GPU |

The training process follows:

```
Input Image
     ↓
Forward Pass
     ↓
Prediction
     ↓
Cross-Entropy Loss
     ↓
Backpropagation
     ↓
Adam Optimizer
     ↓
Updated Weights
```

---

## 8. Model Evaluation

After training, the model was evaluated using the CIFAR-10 test set.

Evaluation included:
- Overall test accuracy
- Confusion matrix
- Class-wise accuracy
- Best-performing class
- Weakest-performing class

The model achieved approximately **72.92% test accuracy**.

### Class-wise Results

| Class | Accuracy |
|-------|----------|
| Airplane | 73.80% |
| Automobile | 85.40% |
| Bird | 64.20% |
| Cat | 65.80% |
| Deer | 68.80% |
| Dog | 49.40% |
| Frog | 79.30% |
| Horse | 82.40% |
| Ship | 82.80% |
| Truck | 77.30% |

**Best Class:** Automobile — 85.40%
**Weakest Class:** Dog — 49.40%

> Note: If you later retrained the model with the T4 version, use the new final accuracy/results from that run in the final report rather than these earlier figures.

---

## 9. Confusion Matrix

A confusion matrix was generated to understand where the model makes classification mistakes.

It helped identify that some visually similar classes are harder for the model to distinguish, particularly classes such as:

- Cat ↔ Dog
- Bird ↔ Deer
- Dog ↔ Cat

This analysis provides more information than overall accuracy alone.

---

## 10. Model Saving

After training, the trained model weights were saved as:

```
cifar10_cnn.pth
```

This allows the trained CNN to be reused later without retraining it from scratch.

---

## 11. Streamlit UI

A web-based interface was developed using Streamlit.

The user can:

```
Open Web App
      ↓
Upload Image
      ↓
Image Preprocessing
      ↓
CNN Model
      ↓
Prediction
      ↓
Confidence Score
      ↓
Class Probabilities
```

The interface provides:
- Image upload
- Uploaded-image preview
- Predicted class
- Confidence percentage
- Class probability visualization
- Information about the project and CIFAR-10 classes

---

## 12. Deployment

The application was successfully deployed online using Streamlit.

**Live Project:**
[Open Live CIFAR-10 Classifier](https://cifar10-image-classifier.streamlit.app)

This makes the project accessible through a web browser without requiring the user to run the Python code locally.

---

## 13. Technologies Used

- Python
- PyTorch
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Pillow
- Streamlit
- Google Colab
- NVIDIA Tesla T4 GPU
- GitHub

---

## 14. Project Workflow

```
CIFAR-10 Dataset
       ↓
Data Loading
       ↓
Data Exploration
       ↓
Image Preprocessing
       ↓
PyTorch Tensor Conversion
       ↓
DataLoader
       ↓
CNN Construction
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Accuracy
       ↓
Confusion Matrix
       ↓
Class-wise Analysis
       ↓
Save Model (.pth)
       ↓
Streamlit UI
       ↓
Online Deployment
       ↓
Live Image Classification
```

---

## 15. Final Outcome

The project successfully demonstrates an end-to-end deep-learning image classification system:

**Dataset → Preprocessing → CNN → Training → Evaluation → Model Saving → Streamlit UI → Online Deployment**

The final application allows a user to upload an image and interact with the trained CNN through a simple web interface.

---

### One-line project summary

> "A PyTorch-based CNN image classification system trained on CIFAR-10 and deployed as an interactive Streamlit web application for real-time image prediction."

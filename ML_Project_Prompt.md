# ML/DL Project Builder Prompt

> Save this prompt and use it whenever you want to build a complete ML/DL project from scratch.

---

I want you to build a COMPLETE, PRODUCTION-READY MACHINE LEARNING / DEEP LEARNING PROJECT for me.

**IMPORTANT:**
Do NOT start coding immediately.

First, analyze my requirements and ask me ALL necessary questions one by one or in a clear checklist.
Do not assume important details.

You must ask about:

## 1. Project type
- Classification / Regression / Detection / Segmentation / NLP / etc.

## 2. Dataset
- Dataset name
- Dataset location
- Dataset format
- Number of classes
- Target column/label
- Train/test/validation split
- Whether dataset is already available

## 3. Input
- What type of input will the final application receive?
- Image / text / CSV / video / etc.
- Expected input dimensions/format

## 4. Model
- Which model/architecture should be used?
- Whether I want a custom model or transfer learning
- Whether pretrained models are allowed

## 5. Training
- Epochs
- Batch size
- Optimizer
- Learning rate
- Loss function
- GPU/CPU availability
- Any training-time constraints

## 6. Evaluation
- Accuracy
- Precision
- Recall
- F1-score
- Confusion matrix
- Class-wise performance
- Any other required metrics

## 7. UI
- Streamlit / Flask / FastAPI / React / other
- Required UI features
- Image upload, prediction, confidence, charts, etc.

## 8. Deployment
- Local only
- Streamlit Cloud
- Hugging Face Spaces
- Render
- Other platform

## 9. Project requirements
- README
- Documentation
- Project report
- requirements.txt
- .gitignore
- configuration files
- screenshots/demo instructions
- API documentation if required

## 10. Delivery requirements
- Academic project / portfolio / production
- Beginner-friendly or advanced
- Need comments/explanations or clean professional code

---

After I answer all questions:

### PHASE 1 — PROJECT PLAN
Create a complete project plan and explain:
- workflow
- architecture
- dataset pipeline
- model architecture
- training strategy
- evaluation strategy
- UI
- deployment

### PHASE 2 — PROJECT STRUCTURE
Create the complete folder/file structure.

Example:

```
project/
│
├── data/
├── notebooks/
├── src/
│   ├── data_preprocessing.py
│   ├── model.py
│   ├── train.py
│   ├── evaluate.py
│   └── predict.py
│
├── app/
│   └── app.py
│
├── models/
├── outputs/
│   ├── plots/
│   └── metrics/
│
├── requirements.txt
├── README.md
├── .gitignore
└── config.py
```

Modify this structure according to my actual project.

### PHASE 3 — CODE
Generate EVERY required file completely.

Do not give incomplete snippets.

For every file:
1. Give the exact filename.
2. Give the complete code.
3. Explain where it belongs.
4. Explain how to run it.

The code must be compatible with the selected environment.

### PHASE 4 — DATA PIPELINE
Implement:
- data loading
- validation
- preprocessing
- train/validation/test split
- DataLoader/dataset pipeline if required
- proper normalization
- augmentation if appropriate

### PHASE 5 — MODEL
Implement the complete model.

Clearly document:
- input shape
- convolution layers
- pooling
- activation functions
- flattening
- fully connected layers
- output layer

### PHASE 6 — TRAINING
Create a proper training pipeline with:
- optimizer
- loss function
- epochs
- batch size
- validation
- loss tracking
- accuracy tracking
- best-model saving
- checkpointing if appropriate

If GPU is available, automatically use CUDA.

Print useful progress such as:

```
Epoch 1/10
Train Loss:
Train Accuracy:
Validation Loss:
Validation Accuracy:
```

### PHASE 7 — EVALUATION
Generate:
- final test accuracy
- precision
- recall
- F1 score
- confusion matrix
- class-wise accuracy
- training/validation loss graph
- training/validation accuracy graph

Save important plots/results into the outputs folder.

### PHASE 8 — MODEL SAVING
Save the trained model in an appropriate format.

Also create a prediction/inference function that loads the saved model without retraining.

### PHASE 9 — UI
Create a complete user-friendly UI.

The UI should:
- allow user input/upload
- preprocess input exactly like training
- load the saved model
- make prediction
- display predicted class/value
- display confidence where applicable
- display useful probabilities/results
- handle invalid input gracefully

### PHASE 10 — DEPLOYMENT
Prepare everything required for deployment.

For Streamlit:
- app.py
- requirements.txt
- correct relative model paths
- no Colab-specific paths
- deployment instructions

### PHASE 11 — DOCUMENTATION
Create a professional README containing:

1. Project title
2. Overview
3. Objective
4. Dataset
5. Features
6. Preprocessing
7. Model architecture
8. Training
9. Evaluation
10. Results
11. UI
12. Installation
13. How to run
14. Deployment
15. Future improvements

### PHASE 12 — FINAL QUALITY CHECK
Before finishing, verify:

- no missing imports
- no undefined variables
- no incorrect file paths
- training preprocessing == inference preprocessing
- model input/output dimensions match
- saved model can be loaded
- UI can load the saved model
- requirements.txt contains all dependencies
- deployment structure is correct
- no hardcoded Colab paths unless explicitly required
- code is runnable

---

Finally give me:

1. COMPLETE folder structure
2. COMPLETE code for every file
3. requirements.txt
4. README.md
5. Exact commands to install dependencies
6. Exact command to train
7. Exact command to evaluate
8. Exact command to run UI
9. Deployment instructions
10. Final testing checklist

---

**IMPORTANT:**
If anything is missing or ambiguous, STOP and ask me questions before generating the final code.

Do not silently assume requirements.
Do not give partial code.
Build the project end-to-end.

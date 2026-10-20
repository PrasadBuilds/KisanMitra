# KisanMitra — Day 30: First AI Model Milestone

## 1. Project Goal

Build an AI-powered application that classifies tomato leaf images into three categories:

- Early Blight
- Healthy
- Late Blight

The project aims to demonstrate how image classification can support preliminary tomato leaf disease identification.

## 2. Dataset

- Total images: 4,500
- Training images: 3,600
- Validation images: 900
- Input image size: 224 × 224 pixels
- Classes: Early Blight, Healthy, Late Blight

## 3. Baseline Model

- Architecture: Convolutional Neural Network (CNN)
- Trainable parameters: 23,779
- Validation accuracy: 78.78%
- Saved model: `kisanmitra_tomato_cnn_best.keras`

## 4. Baseline Class Recall

| Class | Recall |
|---|---:|
| Early Blight | 51% |
| Healthy | 99% |
| Late Blight | 77% |

Recall measures the proportion of actual examples of a class that the model correctly identifies.

## 5. Class-Weighted Experiment

| Metric | Result |
|---|---:|
| Validation accuracy | 75.56% |
| Early Blight recall | 75% |
| Healthy recall | 99% |
| Late Blight recall | 58% |

### Finding

Class weighting improved Early Blight recall but reduced overall validation accuracy and Late Blight recall. The experiment demonstrates a trade-off between class-specific performance and overall performance.

## 6. Model Selection

The baseline model was retained as the selected model because it achieved higher overall validation accuracy in the recorded experiments.

The class-weighted model should not replace it without further evaluation on a separate test dataset.

## 7. Application Integration

The trained model is integrated into the Streamlit KisanMitra application.

Current application features include:

- Tomato leaf image upload and preview
- Prediction among the three supported classes
- Class-wise probability scores
- Basic disease-related guidance
- Hindi and Marathi text-to-speech output

## 8. Testing and Limitations

Preliminary individual-image testing has revealed both correct and incorrect predictions. The recorded results are documented in `testing_results.md`.

The validation results are not a guarantee of performance on real farm images. Further evaluation with independent, correctly labelled images is required.

The displayed model probability is not a guarantee that a prediction is correct. KisanMitra is an educational prototype and should not be used as the sole basis for crop-treatment decisions.

## 9. Next Steps

- Evaluate the model on an independent test dataset.
- Investigate Early Blight and Late Blight misclassifications.
- Test with diverse images captured under real field conditions.
- Improve documentation and prepare a project demonstration.
- Continue testing Hindi and Marathi voice output.

## 10. Milestone Summary

By Day 30, the project has progressed from dataset preparation to a trained CNN model and a Streamlit application with prediction and voice-output features.

The next phase focuses on evaluation, reliability, documentation, and user-friendly presentation.

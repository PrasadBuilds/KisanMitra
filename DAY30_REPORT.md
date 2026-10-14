
# KisanMitra — Day 30: First AI Model Milestone

## Project Goal
Build an AI model that classifies tomato leaf images into:
- Early Blight
- Healthy
- Late Blight

## Dataset
- Total images: 4,500
- Training images: 3,600
- Validation images: 900
- Input image size: 224 x 224 pixels

## Baseline Model
- Architecture: Convolutional Neural Network (CNN)
- Trainable parameters: 23,779
- Validation accuracy: 78.78%

## Baseline Class Recall
- Early Blight: 51%
- Healthy: 99%
- Late Blight: 77%

## Class-Weighted Experiment
- Validation accuracy: 75.56%
- Early Blight recall: 75%
- Healthy recall: 99%
- Late Blight recall: 58%

## Findings
Class weighting improved Early Blight recall but reduced overall accuracy and Late Blight recall.

## Model Selection
Keep `kisanmitra_tomato_cnn_best.keras` as the saved baseline. Do not replace it with the class-weighted experiment without further evaluation.

## Limitations
These results are from a validation dataset. Independent testing and real-world evaluation are still required.

## Next Steps
- Review the model and evaluation code.
- Test predictions on individual leaf images.
- Integrate the model into the KisanMitra application.
- Add farmer-friendly disease information and Hindi/Marathi voice support.

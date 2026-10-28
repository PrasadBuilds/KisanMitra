# KisanMitra - Final Testing Report

## 1. Project Overview
KisanMitra is an educational AI prototype for tomato leaf disease detection. It is built using Python, Streamlit, and TensorFlow.

The application predicts one of three classes:
- Healthy
- Early Blight
- Late Blight

It also provides disease information, basic care suggestions, and Hindi and Marathi voice output.

## 2. Independent Testing Results

A total of 28 images were evaluated using the independent test results CSV.

| Metric | Result |
|---|---:|
| Total test images | 28 |
| Correct predictions | 24 |
| Incorrect predictions | 4 |
| Overall test accuracy | 85.71% |

### Class-wise Results

| Class | Correct | Total | Accuracy |
|---|---:|---:|---:|
| Early Blight | 18 | 22 | 81.82% |
| Healthy | 5 | 5 | 100.00% |
| Late Blight | 1 | 1 | 100.00% |

Note: The Healthy and Late Blight test samples are very limited. Their 100% results should not be treated as proof of reliable performance for those classes.

## 3. Functional Testing

| Feature | Status |
|---|---|
| Streamlit app opens | Passed |
| AI model loads | Passed |
| Image upload works | Passed |
| Disease prediction displays | Passed |
| Hindi voice output | Passed |
| Marathi voice output | Passed |
| Low-confidence warning | Observed |

## 4. Limitations
- Only 28 images are included in this independent test summary.
- The class distribution is imbalanced.
- Predictions may be incorrect, even when confidence is high.
- Results on this test set do not guarantee performance on real farm images.
- More verified and independently labelled images are needed for a stronger evaluation.

## 5. Conclusion
The main application workflow has been tested successfully. KisanMitra loads the trained model, accepts a tomato leaf image, displays a predicted class, provides disease information, and supports Hindi and Marathi voice output.

The independent test set achieved 85.71% accuracy on 28 images. Further testing with a larger, balanced, verified dataset is required to assess reliability.

**Project:** KisanMitra  
**Type:** Educational AI prototype

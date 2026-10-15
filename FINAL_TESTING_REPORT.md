# KisanMitra — Final Testing Report

## 1. Project Overview
KisanMitra is an AI-based tomato leaf disease detection prototype built using Python, Streamlit, and TensorFlow.

The app predicts one of three classes:
- Healthy
- Early Blight
- Late Blight

It also provides disease information, basic care suggestions, and Hindi/Marathi voice output.

## 2. Testing Results

| Test | Result | Confidence |
|---|---|---:|
| Test 1 | Early Blight predicted | 98.23% |
| Test 2 | Late Blight predicted | 46.13% |
| Test 3 | Early Blight predicted | 58.44% |

**Note:** These are model predictions, not verified correct classifications. The actual labels of the images have not been independently confirmed.

## 3. Functional Testing

| Feature | Status |
|---|---|
| Streamlit app opens | Passed |
| AI model loads | Passed |
| Image upload works | Passed |
| Disease prediction displays | Passed |
| Hindi voice output | Passed |
| Marathi voice output | Passed |
| Low-confidence warning displays | Observed |

## 4. Limitations
- Predictions may be incorrect, even when confidence is high.
- Some predictions have low confidence and require verification.
- Google Images test images were not independently labelled.
- Real field performance and model accuracy require further evaluation using verified test data.

## 5. Conclusion
The main application workflow has been tested successfully. KisanMitra can load the trained model, accept a tomato leaf image, display a prediction, provide disease information, and generate Hindi/Marathi voice output.

Further testing with correctly labelled images is required to evaluate prediction accuracy reliably.

**Project:** KisanMitra  
**Type:** Educational AI prototype

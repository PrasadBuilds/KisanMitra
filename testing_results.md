# KisanMitra — Testing Results

## 1. Test Results

| Image ID | Actual Class | Predicted Class | Early Blight | Healthy | Late Blight | Result |
|---|---|---|---:|---:|---:|---|
| Image 1 | Healthy | Early Blight | 98.23% | 0.01% | 1.77% | Incorrect |
| Image 2 | Healthy | Early Blight | 58.44% | 0.14% | 41.42% | Incorrect |
| Image 3 | Late Blight | Late Blight | 42.52% | 11.35% | 46.13% | Correct |
| Image 4 | Unknown | Early Blight | 99.78% | 0.00% | 0.22% | Pending |
| Image 5 | Healthy | Healthy | 0.88% | 97.36% | 1.77% | Correct |
| Image 6 | Early Blight | Late Blight | 23.46% | 0.12% | 76.43% | Incorrect |
| Image 7 | Late Blight | Late Blight | 45.26% | 2.26% | 52.48% | Correct |

*Note: Percentages are the model's displayed class scores. Minor differences in row totals can occur because of rounding.*

## 2. Summary

- Total images tested: 7
- Images with confirmed actual classes: 6
- Correct predictions among confirmed images: 3
- Incorrect predictions among confirmed images: 3
- Pending verification: 1
- Accuracy among confirmed images: 50.00% (3 out of 6)

## 3. Observations

- The model correctly classified the two confirmed Late Blight examples.
- Both confirmed Healthy examples in this small test were misclassified as Early Blight or correctly classified as Healthy, respectively: Image 1 was incorrect and Image 5 was correct.
- The confirmed Early Blight example was misclassified as Late Blight.
- Image 4 cannot be evaluated until its actual class is verified.

## 4. Limitations

This is a small preliminary test and does not provide a reliable estimate of overall model performance.

The displayed class score is not a guarantee that a prediction is correct. Further evaluation should use a larger, independent, correctly labelled test dataset, including images captured under real-world field conditions.

KisanMitra is an educational prototype and should not be used as the sole basis for crop-treatment decisions.

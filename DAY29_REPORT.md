
# KisanMitra — Day 29 Model Evaluation

## Objective
Evaluate the saved baseline tomato disease classification model.

## Dataset
- Total validation images: 900
- Early Blight: 204
- Healthy: 300
- Late Blight: 396

## Results
- Validation accuracy: 78.78%
- Correct predictions: 709
- Incorrect predictions: 191

## Class-wise Recall
- Early Blight: 51%
- Healthy: 99%
- Late Blight: 77%

## Confusion Matrix
```text
[[105, 21, 78],
 [1, 298, 1],
 [38, 52, 306]]
```

## Main Finding
Early Blight is the weakest class. Many Early Blight images are confused with Late Blight.

## Conclusion
The baseline model needs further improvement and independent testing before practical use. These results are from a validation dataset, not real-world testing.

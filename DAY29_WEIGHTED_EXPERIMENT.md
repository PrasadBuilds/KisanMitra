
# KisanMitra — Day 29 Class-Weighted Experiment

## Objective
Improve Early Blight detection using class weights.

## Baseline Model
- Validation accuracy: 78.78%
- Early Blight recall: 51%
- Healthy recall: 99%
- Late Blight recall: 77%

## Class-Weighted Model
- Validation accuracy: 75.56%
- Early Blight recall: 75%
- Healthy recall: 99%
- Late Blight recall: 58%

## Confusion Matrix
```text
[[154, 15, 35],
 [1, 298, 1],
 [111, 57, 228]]
```

## Conclusion
Class weighting improved Early Blight recall but reduced overall accuracy and Late Blight recall. Further experiments are required before selecting a final model.

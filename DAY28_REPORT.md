
# KisanMitra — Day 28 Error Analysis

## Objective
Analyze the tomato disease classification model's errors.

## Validation Results
- Overall validation accuracy: 78.11%
- Early Blight: 94 correct, 106 incorrect out of 200
- Healthy: 318 correct, 0 incorrect out of 318
- Late Blight: 291 correct, 91 incorrect out of 382

## Main Finding
Early Blight is the weakest class. The model predicted 81 Early Blight images as Late Blight.

## Conclusion
The error analysis identified confusion between Early Blight and Late Blight. Further model improvement and testing are needed before practical use.

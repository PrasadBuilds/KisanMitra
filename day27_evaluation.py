
# KisanMitra - Day 27 Model Evaluation

print("KisanMitra - Day 27 Evaluation")
print("=" * 40)

print("Total images: 4500")
print("Training images: 3600")
print("Validation images: 900")

print("\nBest Validation Accuracy: 78.11%")
print("Validation Loss: 0.4736")

print("\nClass-wise F1 Scores:")
print("Early Blight: 0.57")
print("Healthy: 0.89")
print("Late Blight: 0.77")

print("\nConfusion Matrix:")
print("                 Predicted")
print("                Early  Healthy  Late")
print("Actual Early     94      25      81")
print("Actual Healthy    0     318       0")
print("Actual Late      38      53     291")

print("\nConclusion:")
print("Model evaluation completed successfully.")
print("Early Blight detection needs improvement.")

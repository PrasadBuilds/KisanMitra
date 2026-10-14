
classes = ["Early_blight", "Healthy", "Late_blight"]

confusion_matrix = [
    [94, 25, 81],
    [0, 318, 0],
    [38, 53, 291]
]

print("KisanMitra - Day 28 Error Analysis")
print("=" * 50)

for i, class_name in enumerate(classes):
    total = sum(confusion_matrix[i])
    correct = confusion_matrix[i][i]
    incorrect = total - correct

    recall = correct / total * 100

    print(f"\nClass: {class_name}")
    print(f"Total images: {total}")
    print(f"Correct predictions: {correct}")
    print(f"Incorrect predictions: {incorrect}")
    print(f"Class-wise recall: {recall:.2f}%")

print("\nMain finding:")
print("Early Blight has the most classification errors.")
print("81 Early Blight images were predicted as Late Blight.")
print("The model needs further improvement.")

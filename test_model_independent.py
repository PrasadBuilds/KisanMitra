
from pathlib import Path
import csv
import numpy as np
from PIL import Image
import tensorflow as tf

# Model path
MODEL_PATH = Path("kisanmitra_tomato_cnn_balanced_experiment.keras")

# Independent test dataset path
TEST_FOLDER = Path(
    r"C:\Users\lenovo\Desktop\KisanMitra_Independent_Test"
)

# Class names must match the model's training order
CLASS_NAMES = ["Early_Blight", "Healthy", "Late_Blight"]

# Image size used during model training
IMAGE_SIZE = (224, 224)

# CSV report path
REPORT_PATH = Path("independent_test_results.csv")


def main():
    if not MODEL_PATH.exists():
        print("ERROR: Model file not found:", MODEL_PATH.resolve())
        return

    if not TEST_FOLDER.exists():
        print("ERROR: Test folder not found:", TEST_FOLDER)
        return

    print("Loading KisanMitra model...")
    model = tf.keras.models.load_model(MODEL_PATH)
    print("Model loaded successfully!\n")

    results = []
    correct = 0
    total = 0

    for class_name in CLASS_NAMES:
        class_folder = TEST_FOLDER / class_name

        if not class_folder.exists():
            print("WARNING: Folder not found:", class_folder)
            continue

        image_paths = sorted(
            path
            for path in class_folder.iterdir()
            if path.is_file()
            and path.suffix.lower() in {".jpg", ".jpeg", ".png"}
        )

        if not image_paths:
            print("WARNING: No images found in:", class_folder)
            continue

        for image_path in image_paths:
            try:
                with Image.open(image_path) as image:
                    image = image.convert("RGB")
                    image = image.resize(IMAGE_SIZE)
                    image_array = np.asarray(image, dtype=np.float32)

                # Do not divide by 255 here.
                # The saved model already has a Rescaling layer.
                image_array = np.expand_dims(image_array, axis=0)

                prediction = model.predict(image_array, verbose=0)[0]

                predicted_index = int(np.argmax(prediction))
                predicted_class = CLASS_NAMES[predicted_index]
                confidence = float(prediction[predicted_index]) * 100

                actual_class = class_name
                is_correct = predicted_class == actual_class

                if is_correct:
                    correct += 1

                total += 1

                results.append({
                    "image": str(image_path.relative_to(TEST_FOLDER)),
                    "actual_class": actual_class,
                    "predicted_class": predicted_class,
                    "confidence_percent": round(confidence, 2),
                    "result": "CORRECT" if is_correct else "INCORRECT",
                })

                print(
                    f"Image: {image_path.name} | "
                    f"Actual: {actual_class} | "
                    f"Predicted: {predicted_class} | "
                    f"Confidence: {confidence:.2f}% | "
                    f"{'CORRECT' if is_correct else 'INCORRECT'}"
                )

            except Exception as error:
                print(f"ERROR processing {image_path.name}: {error}")

    print("\n" + "=" * 55)
    print("KISANMITRA INDEPENDENT TEST SUMMARY")
    print("=" * 55)

    print("Total images tested:", total)
    print("Correct predictions:", correct)
    print("Incorrect predictions:", total - correct)

    if total > 0:
        accuracy = (correct / total) * 100
        print(f"Candidate-set accuracy: {accuracy:.2f}%")
    else:
        print("No images were tested. Please check the dataset folders.")

    print("\nCLASS-WISE RESULTS")
    print("-" * 55)

    for class_name in CLASS_NAMES:
        class_results = [
            result for result in results
            if result["actual_class"] == class_name
        ]

        class_total = len(class_results)
        class_correct = sum(
            result["result"] == "CORRECT"
            for result in class_results
        )

        if class_total > 0:
            class_accuracy = (class_correct / class_total) * 100
            print(
                f"{class_name}: {class_correct}/{class_total} "
                f"correct ({class_accuracy:.2f}%)"
            )
        else:
            print(f"{class_name}: No images tested")

    # Save all image-level predictions to CSV
    fieldnames = [
        "image",
        "actual_class",
        "predicted_class",
        "confidence_percent",
        "result",
    ]

    with REPORT_PATH.open(
        "w", newline="", encoding="utf-8"
    ) as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("\nCSV report saved successfully:")
    print(REPORT_PATH.resolve())

    print(
        "\nNote: This is a small candidate test set. "
        "It is not a verified independent benchmark."
    )


if __name__ == "__main__":
    main()

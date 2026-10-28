import pandas as pd
from pathlib import Path

csv_file = Path("independent_test_results.csv")

if not csv_file.exists():
    print("ERROR: independent_test_results.csv file not found.")
else:
    df = pd.read_csv(csv_file)

    errors = df[df["result"].astype(str).str.upper() == "INCORRECT"]

    print("\n===== KISANMITRA MODEL ERRORS =====")
    print("Total images tested:", len(df))
    print("Incorrect predictions:", len(errors))

    print("\n===== INCORRECT PREDICTIONS =====")

    for _, row in errors.iterrows():
        print("\nImage:", row["image"])
        print("Actual class:", row["actual_class"])
        print("Predicted class:", row["predicted_class"])
        print("Confidence:", row["confidence_percent"], "%")

    print("\n===== ERROR COUNT BY ACTUAL CLASS =====")
    print(errors["actual_class"].value_counts())
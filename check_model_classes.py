
from pathlib import Path
import tensorflow as tf

model_path = Path("kisanmitra_tomato_cnn_balanced_experiment.keras")

if not model_path.exists():
    print("Model file not found:", model_path)
else:
    model = tf.keras.models.load_model(model_path)

    print("Model loaded successfully.")
    print("Output shape:", model.output_shape)
    print("\nModel output classes:", model.output_shape[-1])

    print("\nCheck the class_names used in your training notebook.")
    print("Expected class order may be:")
    print("0 = Early_blight")
    print("1 = Healthy")
    print("2 = Late_blight")

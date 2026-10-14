
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

st.set_page_config(
    page_title="KisanMitra",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 KisanMitra")
st.subheader("AI Tomato Leaf Disease Detection")

MODEL_PATH = "kisanmitra_tomato_cnn_best.keras"

# Load the trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

try:
    model = load_model()
    st.success("AI model loaded successfully!")
except Exception as e:
    st.error("AI model load nahi hua.")
    st.code(str(e))
    st.stop()

# Class order used during training
class_names = [
    "Early Blight",
    "Healthy",
    "Late Blight"
]

st.info(
    "Tomato leaf ki JPG, JPEG ya PNG image upload karein."
)

uploaded_file = st.file_uploader(
    "Upload a tomato leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Tomato Leaf",
            use_container_width=True
        )

        if st.button("Detect Disease", type="primary"):
            with st.spinner("AI image check kar raha hai..."):

                # Prepare image for model
                resized_image = image.resize((224, 224))
                image_array = np.array(
                    resized_image,
                    dtype=np.float32
                )
                
                image_array = np.expand_dims(
                    image_array,
                    axis=0
                )

                # Predict class probabilities
                predictions = model.predict(
                    image_array,
                    verbose=0
                )[0]

            # Check model output
            if len(predictions) != len(class_names):
                st.error(
                    "Model output aur class names match nahi kar rahe."
                )
                st.stop()

            predicted_index = int(np.argmax(predictions))
            confidence = float(
                predictions[predicted_index]
            ) * 100

            predicted_class = class_names[predicted_index]

            # Show diagnostic probabilities
            st.subheader("🔬 AI Probability Check")

            for name, probability in zip(
                class_names,
                predictions
            ):
                st.write(
                    f"{name}: {float(probability) * 100:.6f}%"
                )

            # Show prediction
            st.subheader("🔍 Prediction Result")
            st.write("**Detected class:**", predicted_class)
            st.write(f"**Model confidence:** {confidence:.2f}%")

            if predicted_class == "Healthy":
                st.success("Model ne leaf ko Healthy classify kiya.")
            elif predicted_class == "Early Blight":
                st.warning("Possible Early Blight detected.")
            else:
                st.warning("Possible Late Blight detected.")

            st.caption(
                "Yeh AI prediction hai, final diagnosis nahi. "
                "Real field conditions mein result alag ho sakta hai."
            )

    except Exception as e:
        st.error("Image process nahi ho payi.")
        st.code(str(e))

import streamlit as st
from PIL import Image

st.title("🌱 KisanMitra")

st.subheader("AI Crop Disease Detection")

uploaded_file = st.file_uploader(
    "Upload a crop leaf image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Crop Leaf"
    )

    st.success("Image uploaded successfully!")
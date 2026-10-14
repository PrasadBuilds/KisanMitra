
import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image
from gtts import gTTS
from io import BytesIO

st.set_page_config(
    page_title="KisanMitra",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 KisanMitra")
st.subheader("AI Tomato Leaf Disease Detection")
st.write("Upload a tomato leaf image to check its possible condition.")

MODEL_PATH = "kisanmitra_tomato_cnn_best.keras"

class_names = [
    "Early Blight",
    "Healthy",
    "Late Blight"
]

# Disease information in English, Hindi and Marathi
disease_info = {
    "Early Blight": {
        "English": {
            "symptoms": "Brown spots, often with ring-like patterns, usually on older leaves.",
            "care": [
                "Remove badly affected leaves carefully.",
                "Avoid wetting leaves while watering.",
                "Keep enough space between plants for airflow.",
                "Ask a local agricultural officer about suitable treatment."
            ]
        },
        "Hindi": {
            "title": "टमाटर में अर्ली ब्लाइट",
            "symptoms": "पत्तियों पर भूरे धब्बे दिखाई दे सकते हैं। धब्बों में गोल छल्ले जैसे निशान हो सकते हैं।",
            "care": [
                "ज्यादा प्रभावित पत्तियों को सावधानी से हटाएँ।",
                "पत्तियों पर पानी डालने से बचें।",
                "पौधों के बीच उचित दूरी रखें।",
                "उपयुक्त उपचार के लिए कृषि अधिकारी से सलाह लें।"
            ]
        },
        "Marathi": {
            "title": "टोमॅटोवरील अर्ली ब्लाइट",
            "symptoms": "पानांवर तपकिरी डाग दिसू शकतात. काही डागांमध्ये गोलाकार वलय दिसतात.",
            "care": [
                "जास्त बाधित पाने काळजीपूर्वक काढा.",
                "पानांवर पाणी पडणार नाही याची काळजी घ्या.",
                "झाडांमध्ये पुरेशी जागा ठेवा.",
                "योग्य उपचारासाठी कृषी अधिकाऱ्यांचा सल्ला घ्या."
            ]
        }
    },
    "Healthy": {
        "English": {
            "symptoms": "The model classified this leaf as healthy. This does not guarantee that the plant is disease-free.",
            "care": [
                "Inspect leaves regularly.",
                "Water near the soil rather than over the leaves.",
                "Maintain good airflow around plants.",
                "Monitor new growth for unusual spots or yellowing."
            ]
        },
        "Hindi": {
            "title": "स्वस्थ टमाटर का पत्ता",
            "symptoms": "मॉडल ने इस पत्ते को स्वस्थ बताया है। फिर भी पौधे में बीमारी होने की संभावना पूरी तरह समाप्त नहीं होती।",
            "care": [
                "पत्तियों की नियमित जाँच करें।",
                "पत्तियों के बजाय मिट्टी के पास पानी दें।",
                "पौधों के बीच हवा आने-जाने की जगह रखें।",
                "नए पत्तों पर धब्बे या पीलापन दिखाई दे तो जाँच करें।"
            ]
        },
        "Marathi": {
            "title": "निरोगी टोमॅटोचे पान",
            "symptoms": "मॉडेलने हे पान निरोगी म्हणून ओळखले आहे. तरीही झाड रोगमुक्त आहे याची पूर्ण खात्री होत नाही.",
            "care": [
                "पानांची नियमित तपासणी करा.",
                "पानांवर पाणी टाकण्याऐवजी मातीजवळ पाणी द्या.",
                "झाडांमध्ये हवा खेळती राहील याची काळजी घ्या.",
                "नवीन पानांवर डाग किंवा पिवळेपणा दिसल्यास तपासणी करा."
            ]
        }
    },
    "Late Blight": {
        "English": {
            "symptoms": "Water-soaked-looking dark patches may develop on leaves and can spread rapidly in cool, wet conditions.",
            "care": [
                "Inspect the plant and nearby plants promptly.",
                "Avoid overhead watering and unnecessary leaf wetness.",
                "Keep affected plant material away from healthy plants.",
                "Seek prompt advice from an agricultural officer because this disease can spread quickly."
            ]
        },
        "Hindi": {
            "title": "टमाटर में लेट ब्लाइट",
            "symptoms": "पत्तियों पर गहरे, पानी से भीगे जैसे धब्बे दिखाई दे सकते हैं। ठंडे और नम मौसम में रोग तेजी से फैल सकता है।",
            "care": [
                "पौधे और आसपास के पौधों की तुरंत जाँच करें।",
                "पत्तियों को गीला करने से बचें।",
                "प्रभावित पौधों की सामग्री को स्वस्थ पौधों से दूर रखें।",
                "रोग तेजी से फैल सकता है, इसलिए कृषि अधिकारी से जल्द सलाह लें।"
            ]
        },
        "Marathi": {
            "title": "टोमॅटोवरील लेट ब्लाइट",
            "symptoms": "पानांवर पाण्याने भिजल्यासारखे गडद डाग दिसू शकतात. थंड आणि दमट हवेत रोग वेगाने पसरू शकतो.",
            "care": [
                "झाडाची आणि जवळच्या झाडांची त्वरित तपासणी करा.",
                "पानांवर पाणी पडणे टाळा.",
                "बाधित झाडांचा कचरा निरोगी झाडांपासून दूर ठेवा.",
                "रोग वेगाने पसरू शकतो; कृषी अधिकाऱ्यांचा लवकर सल्ला घ्या."
            ]
        }
    }
}


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


@st.cache_data
def make_audio(text, language):
    audio_buffer = BytesIO()
    tts = gTTS(text=text, lang=language)
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)
    return audio_buffer.getvalue()


try:
    model = load_model()
    st.success("AI model loaded successfully!")
except Exception as e:
    st.error("AI model load nahi hua.")
    st.code(str(e))
    st.stop()


language = st.selectbox(
    "Choose your language / भाषा चुनें / भाषा निवडा",
    ["English", "Hindi", "Marathi"]
)

language_codes = {
    "Hindi": "hi",
    "Marathi": "mr"
}

st.info("Tomato leaf ki JPG, JPEG ya PNG image upload karein.")

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
                # Resize image. The model already includes Rescaling(1/255).
                resized_image = image.resize((224, 224))
                image_array = np.array(
                    resized_image,
                    dtype=np.float32
                )
                image_array = np.expand_dims(image_array, axis=0)

                predictions = model.predict(
                    image_array,
                    verbose=0
                )[0]

            if len(predictions) != len(class_names):
                st.error("Model output aur class names match nahi kar rahe.")
                st.stop()

            predicted_index = int(np.argmax(predictions))
            confidence = float(predictions[predicted_index]) * 100
            predicted_class = class_names[predicted_index]

            st.subheader("🔍 Prediction Result")
            st.write("**Detected class:**", predicted_class)
            st.write(f"**Model confidence score:** {confidence:.2f}%")

            if confidence < 60:
                st.warning(
                    "Low confidence: result uncertain hai. "
                    "Clear image upload karein aur expert se verify karayein."
                )
            elif predicted_class == "Healthy":
                st.success("Model ne leaf ko Healthy classify kiya.")
            else:
                st.warning(f"Possible {predicted_class} detected.")

            st.caption(
                "Confidence score model ka estimate hai, "
                "diagnosis ki guarantee nahi."
            )

            st.subheader("📋 Disease Information")

            details = disease_info[predicted_class]

            if language == "English":
                st.write("**Possible symptoms:**", details["English"]["symptoms"])
                st.write("**Basic care suggestions:**")
                for item in details["English"]["care"]:
                    st.markdown(f"- {item}")
                voice_text = (
                    f"Prediction: {predicted_class}. "
                    f"Model confidence score: {confidence:.0f} percent. "
                    f"Possible symptoms: {details['English']['symptoms']} "
                    f"Basic care suggestions: "
                    + " ".join(details["English"]["care"])
                )
            else:
                localized = details[language]
                st.write("**" + localized["title"] + "**")
                st.write("**लक्षण / लक्षणे:**", localized["symptoms"])
                st.write("**देखभाल / काळजी:**")
                for item in localized["care"]:
                    st.markdown(f"- {item}")

                voice_text = (
                    localized["title"] + ". "
                    + localized["symptoms"] + " "
                    + " ".join(localized["care"])
                    + f" मॉडल का विश्वास स्कोर {confidence:.0f} प्रतिशत है।"
                    if language == "Hindi"
                    else localized["title"] + ". "
                    + localized["symptoms"] + " "
                    + " ".join(localized["care"])
                    + f" मॉडेलचा विश्वास स्कोअर {confidence:.0f} टक्के आहे."
                )

            if language in language_codes:
                st.subheader("🔊 Listen to the Result")
                try:
                    audio_bytes = make_audio(
                        voice_text,
                        language_codes[language]
                    )
                    st.audio(audio_bytes, format="audio/mp3")
                except Exception:
                    st.warning(
                        "Voice audio nahi ban paya. Internet connection "
                        "check karke dobara try karein."
                    )
            else:
                st.info("Hindi ya Marathi select karein to voice audio sun sakte hain.")

            st.warning(
                "Important: This is an educational AI prototype. "
                "Leaf images alone may not confirm a disease. "
                "For treatment decisions, consult a local agricultural expert. "
                "Do not apply pesticides without checking the product label "
                "and local agricultural guidance."
            )

    except Exception as e:
        st.error("Image process nahi ho payi.")
        st.code(str(e))

# KisanMitra 🌱

## AI Tomato Leaf Disease Detection

KisanMitra is an AI-based educational project that predicts possible tomato leaf diseases from uploaded images.

### Features
- Tomato leaf image upload (JPG, JPEG, PNG)
- Detection of Healthy, Early Blight, and Late Blight classes
- Prediction confidence score
- Disease symptoms and basic care suggestions
- Hindi and Marathi voice assistance

### Technologies Used
- Python
- TensorFlow and Keras
- Streamlit
- NumPy
- Pillow (PIL)
- gTTS

### How to Run

1. Open the KisanMitra project folder in the terminal.
2. Activate the virtual environment:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies if `requirements.txt` is available:

   ```powershell
   pip install -r requirements.txt
   ```

4. Run the application:

   ```powershell
   python -m streamlit run app.py
   ```

5. Open the local URL shown in the terminal.

### Important Disclaimer
This is an educational prototype. Predictions may be incorrect and are not a confirmed diagnosis. Consult an agricultural expert before making treatment decisions.

### Developer
Prasad Chandgude
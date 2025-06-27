import streamlit as st
import joblib
import os


model_path = "modells1.pkl"

# Loading the model
@st.cache_resource(show_spinner="Loading model...")
def load_model():
    if not os.path.exists(model_path):
        st.error(f"❌ Model file '{model_path}' not found.")
        st.stop()
    try:
        return joblib.load(model_path)
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        st.stop()

model = load_model()

# UI
st.markdown("""
   <h1 style='color:#53299F;'>📰 Fake News Detection</h1>
""", unsafe_allow_html=True)

st.markdown("<h5 style='color: teal;'>Enter a short news snippet to check if it's real or fake</h5>", unsafe_allow_html=True)
input_text = st.text_area("")

if st.button("Predict"):
    if input_text.strip() == "":
        st.warning("⚠️ Please enter some text")
    else:
        prediction = model.predict([input_text])
        if prediction[0] == 1:
            st.success("✅ This is Real News")
        else:
            st.error("❌ This is Fake News")

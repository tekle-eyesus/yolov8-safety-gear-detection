import streamlit as st
from PIL import Image
from utils.inference import SafetyModel
from utils.ui import set_modern_ui

set_modern_ui()

model = SafetyModel()

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.markdown("### 🔍 Input Image")
    image = Image.open(uploaded_file)
    st.image(image, use_column_width=True)

    if st.button("Run Detection"):
        with st.spinner("Detecting safety equipment..."):
            output = model.predict(image)

        st.markdown("### ✅ Detection Result")
        st.image(output, use_column_width=True)

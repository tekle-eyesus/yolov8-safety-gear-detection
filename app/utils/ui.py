import streamlit as st

def set_modern_ui():
    st.set_page_config(
        page_title="Safety Gear Detection",
        page_icon="🦺",
        layout="wide"
    )

    st.markdown(
        """
        <style>
            .main {
                background-color: #F7F9FC;
            }
            .title {
                font-size: 40px;
                font-weight: 700;
                text-align: center;
                color: #1E3A8A;
            }
            .sub {
                text-align: center;
                color: #475569;
                font-size: 18px;
            }
            .upload-box {
                border: 2px dashed #4F46E5;
                padding: 20px;
                border-radius: 15px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='title'>🦺 Safety Gear Detection App</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub'>Upload an image to detect helmets and safety vests using YOLOv8.</p>",
                unsafe_allow_html=True)

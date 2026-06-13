import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About HemoTrace")

# =====================================================
# Introduction
# =====================================================

st.header("🩸 What is HemoTrace?")

st.write("""
HemoTrace is a deep learning-based research project that
investigates whether fingerprint patterns can be used to
predict an individual's blood group.

The project combines computer vision and transfer learning
techniques to classify fingerprint images into eight blood
group categories.
""")

# =====================================================
# Objective
# =====================================================

st.header("🎯 Project Objective")

st.write("""
Traditional blood-group determination requires laboratory
testing and invasive procedures.

HemoTrace explores the possibility of predicting blood groups
from fingerprint images using artificial intelligence,
providing a non-invasive and rapid alternative for research.
""")

# =====================================================
# Technologies
# =====================================================

st.header("⚙️ Technologies Used")

st.markdown("""
- Python
- TensorFlow
- Keras
- Streamlit
- NumPy
- Matplotlib
- Seaborn
- Pillow
""")

# =====================================================
# Methodology
# =====================================================

st.header("🔬 Methodology")

st.markdown("""
1. Collection of fingerprint image dataset.
2. Image preprocessing and resizing.
3. Transfer learning using EfficientNetB0.
4. Model training and validation.
5. Performance evaluation using accuracy and confusion matrix.
6. Deployment using Streamlit.
""")

# =====================================================
# Future Scope
# =====================================================

st.header("🚀 Future Scope")

st.markdown("""
- Larger and more diverse datasets
- Advanced feature extraction techniques
- Hybrid CNN architectures
- Ensemble learning approaches
- Mobile application deployment
- Clinical validation studies
""")

# =====================================================
# Developer
# =====================================================

st.header("👨‍💻 Developer")

st.write("""
**HemoTrace**

Fingerprint-Based Blood Group Classification Using Deep Learning

Developed as a research-oriented machine learning project
exploring biometric analysis and medical AI applications.
""")

# =====================================================
# Disclaimer
# =====================================================

st.warning("""
This application is intended for research and educational
purposes only.

It should not be used for medical diagnosis or clinical
decision-making.
""")
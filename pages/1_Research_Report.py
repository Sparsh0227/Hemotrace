import streamlit as st

st.set_page_config(
    page_title="Research Report",
    page_icon="📊",
    layout="wide"
)

st.title("📊 HemoTrace Research Report")

st.markdown("""
This page summarizes the experiments, evaluation metrics,
and findings obtained during the development of HemoTrace.
""")

# =====================================================
# Dataset Overview
# =====================================================

st.header("📁 Dataset Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Images", "8000")

with col2:
    st.metric("Blood Groups", "8")

with col3:
    st.metric("Input Size", "224 × 224")

st.markdown("""
**Blood Group Classes**

- A+
- A-
- AB+
- AB-
- B+
- B-
- O+
- O-
""")

# =====================================================
# Experiment Comparison
# =====================================================

st.header("🧪 Experiment Comparison")

experiment_data = {
    "Experiment": [
        "EfficientNetB0",
        "Fine Tuning",
        "CLAHE Preprocessing",
        "Gabor Filter",
        "MobileNetV2",
        "MobileNetV2 + Grayscale"
    ],
    "Accuracy": [
        "50.6%",
        "47.0%",
        "45.5%",
        "34.0%",
        "49.5%",
        "48.9%"
    ]
}

st.table(experiment_data)

# =====================================================
# Accuracy Curve
# =====================================================

st.header("📈 Training & Validation Accuracy")

st.image(
    "accuracy_curve.png",
    caption="Training vs Validation Accuracy"
)

# =====================================================
# Confusion Matrix
# =====================================================

st.header("🎯 Confusion Matrix")

st.image(
    "confusion_matrix.png",
    caption="Model Confusion Matrix"
)

# =====================================================
# Findings
# =====================================================

st.header("🔍 Key Findings")

st.success("""
• EfficientNetB0 achieved approximately 50.6% validation accuracy.

• MobileNetV2 achieved approximately 49.5% test accuracy.

• CLAHE preprocessing reduced performance.

• Gabor filtering significantly reduced performance.

• The model learned meaningful fingerprint features but still
  exhibits confusion between certain blood-group classes.

• Raw fingerprint images produced the best overall results.
""")

# =====================================================
# Conclusion
# =====================================================

st.header("✅ Conclusion")

st.info("""
HemoTrace demonstrates the feasibility of using deep learning
for fingerprint-based blood-group classification.

While the model does not achieve clinical-level accuracy,
the project successfully explores a novel and research-oriented
application of computer vision and transfer learning.
""")
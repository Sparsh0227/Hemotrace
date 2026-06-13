# import streamlit as st
# import numpy as np
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import img_to_array
# from PIL import Image, UnidentifiedImageError
# import tflite_runtime.interpreter as tflite

# # =====================================================
# # PAGE CONFIG
# # =====================================================

# st.set_page_config(
#     page_title="HemoTrace",
#     page_icon="🩸",
#     layout="centered"
# )

# # =====================================================
# # LOAD MODEL
# # =====================================================

# @st.cache_resource
# interpreter = tflite.Interpreter(model_path="best_hemotrace.tflite")
# interpreter.allocate_tensors()

# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# model = load_hemo_model()

# st.markdown(
#     """
#     <h1 style='text-align:center;'>
#         🩸 HemoTrace
#     </h1>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(
#     """
#     <p style='text-align:center;
#               font-size:22px;
#               color:gray;'>
#     Fingerprint-Based Blood Group Classification
#     </p>
#     """,
#     unsafe_allow_html=True
# )

# st.image(
#     "banner.png",
#     use_container_width=True
# )

# st.markdown("""
# ### Research-Oriented Deep Learning Project

# HemoTrace investigates whether fingerprint patterns can be used
# to predict blood groups using computer vision and deep learning.
# """)

# # =====================================================
# # LABELS
# # =====================================================

# labels = [
#     "A+",
#     "A-",
#     "AB+",
#     "AB-",
#     "B+",
#     "B-",
#     "O+",
#     "O-"
# ]



# # =====================================================
# # METRICS
# # =====================================================

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.metric("🩸 Classes", "8")

# with col2:
#     st.metric("📁 Dataset", "8000")

# with col3:
#     st.metric("🎯 Accuracy", "50.6%")

# st.info(
#     "📌 Explore the **Research Report** and **About Project** pages from the sidebar."
# )

# st.markdown(
#     "<hr style='border:2px solid #C62828;'>",
#     unsafe_allow_html=True
# )

# # =====================================================
# # UPLOAD SECTION
# # =====================================================

# st.subheader("📤 Upload Fingerprint")

# uploaded_file = st.file_uploader(
#     "Choose a BMP fingerprint image",
#     type=["bmp"]
# )

# # =====================================================
# # PREDICTION
# # =====================================================

# if uploaded_file is not None:

#     try:

#         image = Image.open(uploaded_file).convert("RGB")

#         st.image(
#             image,
#             caption="Uploaded Fingerprint",
#             use_container_width=True
#         )

#         # SAME PREPROCESSING USED DURING TRAINING

#         image = image.resize((224, 224))

#         img_array = img_to_array(image)

#         img_array = np.expand_dims(
#             img_array,
#             axis=0
#         )

#         with st.spinner("Analyzing fingerprint..."):

#             prediction = model.predict(
#                 img_array,
#                 verbose=0
#             )

#         predicted_index = np.argmax(
#             prediction[0]
#         )

#         predicted_label = labels[
#             predicted_index
#         ]

#         confidence = float(
#             np.max(prediction[0]) * 100
#         )

#         # =====================================================
#         # RESULT CARD
#         # =====================================================

#         st.markdown(
#     f"""
#     <div style="
#         background-color:#FFEBEE;
#         padding:20px;
#         border-radius:12px;
#         border-left:8px solid #C62828;
#     ">
#     <h2 style="color:#C62828;">
#     Predicted Blood Group: {predicted_label}
#     </h2>
#     </div>
#     """,
#     unsafe_allow_html=True
# )
#         st.write(
#             f"### Confidence Score: {confidence:.2f}%"
#         )

#         if confidence >= 70:

#             st.success(
#                 "High Confidence Prediction"
#             )

#         elif confidence >= 40:

#             st.warning(
#                 "Moderate Confidence Prediction"
#             )

#         else:

#             st.error(
#                 "Low Confidence Prediction"
#             )

#         # =====================================================
#         # PROBABILITIES
#         # =====================================================

#         st.subheader(
#             "📊 Prediction Probabilities"
#         )

#         probability_dict = {}

#         for label, prob in zip(
#             labels,
#             prediction[0]
#         ):

#             probability_dict[label] = float(prob)

#         st.bar_chart(probability_dict)

#         # =====================================================
#         # TOP 3
#         # =====================================================

#         st.subheader(
#             "🏆 Top 3 Predictions"
#         )

#         top3 = np.argsort(
#             prediction[0]
#         )[-3:][::-1]

#         for i in top3:

#             st.write(
#                 f"**{labels[i]}** : "
#                 f"{prediction[0][i] * 100:.2f}%"
#             )

#     except UnidentifiedImageError:

#         st.error(
#             "Invalid BMP image. Please upload a valid fingerprint image."
#         )

#     except Exception as e:

#         st.error(
#             f"Error: {str(e)}"
#         )

# # =====================================================
# # ABOUT HEMOTRACE
# # =====================================================

# with st.expander("ℹ️ About HemoTrace"):

#     st.write("""
#     HemoTrace is a research-oriented deep learning project
#     that investigates whether fingerprint patterns can be
#     used to predict blood groups.

#     Dataset Size: 8000 fingerprint images

#     Blood Groups:
#     A+, A-, AB+, AB-, B+, B-, O+, O-

#     Model:
#     EfficientNetB0

#     The project explores transfer learning and computer
#     vision techniques for non-invasive blood-group
#     classification.
#     """)

# # =====================================================
# # SIDEBAR
# # =====================================================

# st.sidebar.image(
#     "logo.png",
#     use_container_width=True
# )

# st.sidebar.title("🩸 HemoTrace")
# st.sidebar.write("Model: EfficientNetB0")
# st.sidebar.write("Input Size: 224 × 224")
# st.sidebar.write("Classes: 8")
# st.sidebar.write("Dataset: 8000 Images")

# st.sidebar.markdown("---")

# st.sidebar.success(
#     "Research-Oriented Deep Learning Project"
# )

# st.sidebar.markdown("---")

# st.sidebar.warning(
#     "For research and educational purposes only.\n\n"
#     "Not intended for medical diagnosis."
# )

# # =====================================================
# # FOOTER
# # =====================================================

# st.markdown("---")

# st.caption(
#     "🩸 HemoTrace © 2026 | Fingerprint-Based Blood Group Classification using Deep Learning"
# )
import streamlit as st
import numpy as np
from PIL import Image, UnidentifiedImageError
import tflite_runtime.interpreter as tflite

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="HemoTrace",
    page_icon="🩸",
    layout="centered"
)

# =====================================================
# LOAD TFLITE MODEL
# =====================================================

@st.cache_resource
def load_interpreter():
    interpreter = tflite.Interpreter(
        model_path="best_hemotrace.tflite"
    )
    interpreter.allocate_tensors()
    return interpreter

interpreter = load_interpreter()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
    <h1 style='text-align:center;'>
        🩸 HemoTrace
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align:center;
              font-size:22px;
              color:gray;'>
    Fingerprint-Based Blood Group Classification
    </p>
    """,
    unsafe_allow_html=True
)

st.image(
    "banner.png",
    use_container_width=True
)

st.markdown("""
### Research-Oriented Deep Learning Project

HemoTrace investigates whether fingerprint patterns can be used
to predict blood groups using computer vision and deep learning.
""")

# =====================================================
# LABELS
# =====================================================

labels = [
    "A+",
    "A-",
    "AB+",
    "AB-",
    "B+",
    "B-",
    "O+",
    "O-"
]

# =====================================================
# METRICS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🩸 Classes", "8")

with col2:
    st.metric("📁 Dataset", "8000")

with col3:
    st.metric("🎯 Accuracy", "50.6%")

st.info(
    "📌 Explore the **Research Report** and **About Project** pages from the sidebar."
)

st.markdown(
    "<hr style='border:2px solid #C62828;'>",
    unsafe_allow_html=True
)

# =====================================================
# UPLOAD SECTION
# =====================================================

st.subheader("📤 Upload Fingerprint")

uploaded_file = st.file_uploader(
    "Choose a BMP fingerprint image",
    type=["bmp"]
)

# =====================================================
# PREDICTION
# =====================================================

if uploaded_file is not None:

    try:

        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Uploaded Fingerprint",
            use_container_width=True
        )

        image = image.resize((224, 224))

        img_array = np.array(
            image,
            dtype=np.float32
        )

        img_array = np.expand_dims(
            img_array,
            axis=0
        )

        with st.spinner("Analyzing fingerprint..."):

            interpreter.set_tensor(
                input_details[0]["index"],
                img_array
            )

            interpreter.invoke()

            prediction = interpreter.get_tensor(
                output_details[0]["index"]
            )

        predicted_index = np.argmax(
            prediction[0]
        )

        predicted_label = labels[
            predicted_index
        ]

        confidence = float(
            np.max(prediction[0]) * 100
        )

        st.markdown(
            f"""
            <div style="
                background-color:#FFEBEE;
                padding:20px;
                border-radius:12px;
                border-left:8px solid #C62828;
            ">
            <h2 style="color:#C62828;">
            Predicted Blood Group: {predicted_label}
            </h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write(
            f"### Confidence Score: {confidence:.2f}%"
        )

        if confidence >= 70:
            st.success(
                "High Confidence Prediction"
            )

        elif confidence >= 40:
            st.warning(
                "Moderate Confidence Prediction"
            )

        else:
            st.error(
                "Low Confidence Prediction"
            )

        # =====================================================
        # PROBABILITIES
        # =====================================================

        st.subheader(
            "📊 Prediction Probabilities"
        )

        probability_dict = {}

        for label, prob in zip(
            labels,
            prediction[0]
        ):
            probability_dict[label] = float(prob)

        st.bar_chart(probability_dict)

        # =====================================================
        # TOP 3
        # =====================================================

        st.subheader(
            "🏆 Top 3 Predictions"
        )

        top3 = np.argsort(
            prediction[0]
        )[-3:][::-1]

        for i in top3:

            st.write(
                f"**{labels[i]}** : "
                f"{prediction[0][i] * 100:.2f}%"
            )

    except UnidentifiedImageError:

        st.error(
            "Invalid BMP image. Please upload a valid fingerprint image."
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

# =====================================================
# ABOUT HEMOTRACE
# =====================================================

with st.expander("ℹ️ About HemoTrace"):

    st.write("""
    HemoTrace is a research-oriented deep learning project
    that investigates whether fingerprint patterns can be
    used to predict blood groups.

    Dataset Size: 8000 fingerprint images

    Blood Groups:
    A+, A-, AB+, AB-, B+, B-, O+, O-

    Model:
    EfficientNetB0

    The project explores transfer learning and computer
    vision techniques for non-invasive blood-group
    classification.
    """)

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.image(
    "logo.png",
    use_container_width=True
)

st.sidebar.title("🩸 HemoTrace")
st.sidebar.write("Model: EfficientNetB0")
st.sidebar.write("Input Size: 224 × 224")
st.sidebar.write("Classes: 8")
st.sidebar.write("Dataset: 8000 Images")

st.sidebar.markdown("---")

st.sidebar.success(
    "Research-Oriented Deep Learning Project"
)

st.sidebar.markdown("---")

st.sidebar.warning(
    "For research and educational purposes only.\n\n"
    "Not intended for medical diagnosis."
)

# =====================================================
# FOOTER
# =====================================================

st.markdown("---")

st.caption(
    "🩸 HemoTrace © 2026 | Fingerprint-Based Blood Group Classification using Deep Learning"
)
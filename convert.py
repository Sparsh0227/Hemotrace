import tensorflow as tf

print("Loading model...")

model = tf.keras.models.load_model("best_hemotrace.keras")

print("Converting model...")

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

with open("best_hemotrace.tflite", "wb") as f:
    f.write(tflite_model)

print("Saved as best_hemotrace.tflite")
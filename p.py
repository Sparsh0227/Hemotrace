import tensorflow as tf

interpreter = tf.lite.Interpreter(
    model_path="best_hemotrace.tflite"
)

interpreter.allocate_tensors()

print(interpreter.get_input_details())
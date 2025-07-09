import tensorflow as tf
import numpy as np

print("🧠 Generating text...")

# Load the trained model and vocab files
model = tf.keras.models.load_model('char_rnn_model.h5')
char2idx = np.load('char2idx.npy', allow_pickle=True).item()
idx2char = np.load('idx2char.npy')

# Text generation function
def generate_text(model, start_string, num_generate=300):
    # Convert input string to numbers (vectorization)
    input_eval = [char2idx.get(s, 0) for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []
    temperature = 1.0  # Higher = more random; Lower = more predictable

    for _ in range(num_generate):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0)  # remove batch dimension

        # Apply temperature to predictions
        predictions = predictions / temperature

        # Get next character index
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1, 0].numpy()

        # Use predicted character as next input
        input_eval = tf.expand_dims([predicted_id], 0)

        # Append predicted character
        text_generated.append(idx2char[predicted_id])

    return start_string + ''.join(text_generated)

# Run generation
output = generate_text(model, start_string="The sky")

print("\n📝 Generated Text:\n")
print(output)

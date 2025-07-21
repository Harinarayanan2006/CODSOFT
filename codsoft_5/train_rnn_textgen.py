import tensorflow as tf
import numpy as np

print("🧠 You are running the correct and updated script ✅")
print("🚀 Training started...")

# Load your cleaned text data
with open("data.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Create character-level mapping
vocab = sorted(set(text))
char2idx = {u: i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)
text_as_int = np.array([char2idx[c] for c in text])

# Create training sequences
seq_length = 100
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)
sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)

def split_input_target(chunk):
    return chunk[:-1], chunk[1:]

dataset = sequences.map(split_input_target)
dataset = dataset.shuffle(10000).batch(64, drop_remainder=True).take(100)

# Model parameters
vocab_size = len(vocab)
embedding_dim = 256
rnn_units = 512

# ✅ Fixed build_model (no batch_input_shape!)
def build_model(vocab_size, embedding_dim, rnn_units):
    return tf.keras.Sequential([
        tf.keras.layers.Input(shape=(None,)),
        tf.keras.layers.Embedding(vocab_size, embedding_dim),
        tf.keras.layers.GRU(rnn_units, return_sequences=True),
        tf.keras.layers.Dense(vocab_size)
    ])

# Build and train
model = build_model(vocab_size, embedding_dim, rnn_units)
model.compile(optimizer='adam', loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True))
model.fit(dataset, epochs=20)

# Save everything
model.save('char_rnn_model.h5')
np.save('char2idx.npy', char2idx)
np.save('idx2char.npy', idx2char)

print("✅ Model trained and saved!")

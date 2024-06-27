import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dot, Flatten, Dense
import numpy as np

# Sample dataset creation
def create_dataset(num_users, num_items):
    user_ids = np.random.randint(0, num_users, size=1000)
    item_ids = np.random.randint(0, num_items, size=1000)
    interactions = np.random.randint(0, 2, size=1000)  # 0 or 1 indicating no interaction or interaction
    return user_ids, item_ids, interactions

# Create a simple collaborative filtering model
def create_recommendation_model(num_users, num_items, embedding_size=50):
    user_input = Input(shape=(1,))
    item_input = Input(shape=(1,))
    
    user_embedding = Embedding(num_users, embedding_size)(user_input)
    item_embedding = Embedding(num_items, embedding_size)(item_input)
    
    dot_product = Dot(axes=2)([user_embedding, item_embedding])
    dot_product = Flatten()(dot_product)
    
    output = Dense(1, activation='sigmoid')(dot_product)
    
    model = Model([user_input, item_input], output)
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Example usage
num_users = 100
num_items = 100
user_ids, item_ids, interactions = create_dataset(num_users, num_items)

model = create_recommendation_model(num_users, num_items)
model.fit([user_ids, item_ids], interactions, epochs=5, batch_size=32)

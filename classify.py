# classify.py
import tensorflow as tf
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.resnet_v2 import preprocess_input
import numpy as np

# Path to the saved model
MODEL_PATH = '/Users/harshil/Development/ComputerVisionAPP_Harshil/firstModel_harshil.h5'
model = load_model(MODEL_PATH)

# Define class names based on the training dataset
CLASS_NAMES = {
    0: 'building',
    1: 'forest',
    2: 'glacier',
    3: 'mountain',
    4: 'sea',
    5: 'street'
}

def preprocess_image(image_path):
    """
    Preprocess the image to the format the model expects.
    This matches the preprocessing used during training but without augmentation.
    """
    img = image.load_img(image_path, target_size=(150, 150))  # Resize image
    img_array = image.img_to_array(img)  # Convert image to array
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return preprocess_input(img_array_expanded_dims)  # Preprocess the image

def classify_image(image_path):
    """
    Classify an image using the loaded model.
    Returns the predicted class name and confidence.
    """
    preprocessed_image = preprocess_image(image_path)
    predictions = model.predict(preprocessed_image)
    
    # Find the index of the class with the highest probability
    class_index = np.argmax(predictions, axis=1)[0]
    # Find the highest probability
    class_confidence = np.max(predictions, axis=1)[0]

    # Map the index to the class name
    class_name = CLASS_NAMES.get(class_index, "Unknown")
    
    return class_name, float(class_confidence)  # Convert numpy float to Python float

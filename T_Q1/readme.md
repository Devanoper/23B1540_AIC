* In the failed file , I tried multi-bboxes and multi-class labels , but couldn't make the custom loss function properly
* In the normal file , I have simplified the task to only detect labels in images with one object

NOTE: For some reason these files are refusing to show properly in github , you may need to download them to view properly

## HOW-TO-USE

The model can be used to classify a single object within an image.

**Requirements:**

* Python 3.x
* TensorFlow 2.x
* TensorFlow Datasets
* NumPy
* Matplotlib

**Installation:**

1. Install the required packages:
```bash
pip install tensorflow tensorflow-datasets numpy matplotlib
```

**Usage:**

1. **Download the model:**
Download the model file `voc2007_single_object_model.keras` from this repository.

2. **Load the model:**
```python
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('voc2007_single_object_model.keras')

# Load the VOC 2007 test dataset
(test_dataset, test_info) = tfds.load('voc/2007', split='test', with_info=True)

# Filter and preprocess the test dataset (same as the training code)
test_dataset = test_dataset.filter(filter_single_object)
test_dataset = test_dataset.map(preprocess).batch(32).prefetch(tf.data.experimental.AUTOTUNE)

# Evaluate the model (optional)
test_loss, test_accuracy = model.evaluate(test_dataset)
print(f'Test Accuracy: {test_accuracy:.2f}')
```

3. **Make predictions:**
```python
import numpy as np
from PIL import Image

# Load your image
image = Image.open('your_image.jpg')

# Resize the image to the model's input size (256x256)
image = image.resize((256, 256))

# Convert the image to a NumPy array
image_np = np.array(image) / 255.0

# Expand the dimensions of the array to match the model input
image_np = np.expand_dims(image_np, axis=0)

# Make predictions
predictions = model.predict(image_np)

# Get the predicted class
predicted_class = np.argmax(predictions, axis=1)[0]

# Get the class name
class_names = test_info.features['objects']['label'].names
predicted_class_name = class_names[predicted_class]

print(f'Predicted Class: {predicted_class_name}')
```

**Notes:**

* This model is trained on the VOC 2007 dataset, which contains 20 classes.
* The model expects an input image of size 256x256 pixels.
* The model will predict a single object class

**Example:**

```python
# Predict the class of an image
predicted_class_name = predict_class('your_image.jpg')
```

**Output:**

```
Predicted Class: person
```

This indicates that the model predicted the image contains a person.

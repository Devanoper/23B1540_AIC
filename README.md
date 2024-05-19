## T_Q1
### Prerequisites

* Python 3.x
* TensorFlow 2.x
* TensorFlow Datasets
* Matplotlib
* Scikit-learn
* NumPy

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/your-username/voc2007-singleobject-detection.git
cd voc2007-single-object-detection
```

2. **Install required packages:**
```bash
pip install tensorflow tensorflow-datasets matplotlib scikit-learn numpy
```

### Loading the Model

1. **Download the saved model:**
* Ensure that the `voc2007_single_object_model.h5` file is in your working directory.
* If not, download it from the provided link or location.

2. **Load the model in your script:**
```python
import tensorflow as tf

model = tf.keras.models.load_model('voc2007_single_object_model.h5')
```

### Preparing Your Data

1. **Preprocess images:**
* Ensure your images are in a suitable format and size.
* Resize them to 256x256 pixels and normalize the pixel values.

```python
import tensorflow as tf

IMG_SIZE = 256

def preprocess_image(image_path):
image = tf.io.read_file(image_path)
image = tf.image.decode_jpeg(image, channels=3)
image = tf.image.resize(image, (IMG_SIZE, IMG_SIZE)) / 255.0
return image

# Example usage:
image = preprocess_image('path/to/your/image.jpg')
image = tf.expand_dims(image, axis=0) # Add batch dimension
```

### Making Predictions

1. **Make predictions with the model:**
```python
predictions = model.predict(image)
predicted_label = tf.argmax(predictions, axis=1).numpy()[0]

# Map the numeric label to the class name
class_names = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
predicted_class = class_names[predicted_label]

print(f'Predicted class: {predicted_class}')
```

### Visualizing Results

1. **Visualize the predictions:**
```python
import matplotlib.pyplot as plt

def display_image(image, predicted_class):
plt.imshow(image[0])
plt.title(f'Predicted class: {predicted_class}')
plt.axis('off')
plt.show()

# Example usage:
display_image(image, predicted_class)
```

**Remember to replace `'path/to/your/image.jpg'` with the actual path to your image.**



## T_Q2
* a how-to-use.md file is attached
* an improvements.md file is attached



## References
* Basic ML : Hands-On Machine Learning by Geron Aurelien 
           Chapters 1 & 2
           
* Neural Networks (NN) : https://youtube.com/playlist?list=PL_h2yd2CGtBHEKwEH5iqTZH85wLS-eUzv&feature=shared

* Convulational Neural Networks (CNN) : Hands-On Machine Learning by Geron Aurelien 
                                      Chapters 10, 11 and 14
* https://machinelearningspace.com/coco-dataset-a-step-by-step-guide-to-loading-and-visualizing/
* Transformers : https://www.youtube.com/watch?v=wjZofJX0v4M
* Attention : https://www.youtube.com/watch?v=eMlx5fFNoYc
* LangChain docs

# Dogs vs Cats Image Classification

This project uses a **Convolutional Neural Network (CNN)** to classify images as either a dog or a cat, based on the **Dogs vs Cats** dataset from Kaggle.

## Approach

- The dataset is preprocessed by scaling images to 256x256 pixels.
- A CNN model with 3 convolutional layers is implemented using TensorFlow and Keras.
- The model uses `Conv2D`, `MaxPooling2D`, `BatchNormalization`, and `Dropout` layers, followed by dense layers for classification.
- The output is a binary classification (dog or cat) with a **sigmoid activation function**.

## Usage

1. **Dataset**: Download the dataset from Kaggle.
2. **Preprocessing**: Images are scaled to `[0,1]` range for training.
3. **Model**: The CNN is built and trained on the preprocessed images, achieving around 81% accuracy on validation data.
4. **Prediction**: The model can predict whether a given image is a dog or a cat.

## Tools Used

- Python
- TensorFlow / Keras
- OpenCV for image handling
- Matplotlib for plotting training results

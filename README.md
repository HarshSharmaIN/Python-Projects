# Bird Species Classification Using VGG16

This project aims to classify 100 species of birds using a pre-trained VGG16 model, which is fine-tuned for this specific task. The model is trained on a dataset of bird images and then used to predict the species of a given bird image.

## Table of Contents

- [Installation](#installation)
- [Dataset](#dataset)
- [Model Architecture](#model-architecture)
- [Training](#training)
- [Evaluation](#evaluation)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [References](#references)

## Installation

1. Install TensorFlow and Keras using `pip`:

   ```bash
   pip install tensorflow keras
   ```

2. Install the necessary libraries for image preprocessing:

   ```bash
   pip install numpy matplotlib
   ```

## Dataset

The dataset used for this project contains images of 100 different bird species. The dataset is divided into three directories:

- **Train**: Contains 38,518 images across 270 classes.
- **Validation**: Contains 1,350 images across 270 classes.
- **Test**: Similar to the validation dataset for testing purposes.

The dataset should be placed in the following structure:

```
../input/100-bird-species/
  ├── train/
  ├── valid/
  └── test/
```

Each class folder contains images for a specific bird species.

## Model Architecture

The model uses a **VGG16** pre-trained on ImageNet, with the top layers removed. A custom classifier is added on top:

- **Flatten layer**: Converts the output of the convolutional layers into a flat vector.
- **Dense layer**: A fully connected layer with `softmax` activation for classifying into 270 bird species.

### Key Details:

- Input shape: `(224, 224, 3)`
- Pre-trained weights: `imagenet`
- Classifier output: 270 classes (birds)

The pre-trained layers are frozen to retain their knowledge, and only the classifier layers are trained on the bird species dataset.

## Training

1. The model is compiled with:

   - Loss: `categorical_crossentropy`
   - Optimizer: `adam`
   - Metrics: `accuracy`

2. **Image Augmentation** is applied to the training data using `ImageDataGenerator` for rescaling, zoom, shear, and horizontal flipping.

3. Model is trained for **5 epochs** using the following:

   ```python
   r = model.fit_generator(
       training_set,
       validation_data=test_set,
       epochs=5,
       steps_per_epoch=len(training_set),
       validation_steps=len(test_set)
   )
   ```

4. The training and validation loss and accuracy are plotted using `matplotlib`.

## Evaluation

After training, the model achieves a **training accuracy** of around 78% and a **validation accuracy** of around 76%. The performance metrics include both loss and accuracy.

## Usage

1. **Saving the Model**:
   The trained model is saved as `BC.h5` using the `model.save()` function.

2. **Prediction**:
   A custom function `output()` is created to predict the species of a given bird image. It accepts an image path as input, preprocesses the image, and outputs the predicted species.

   Example usage:

   ```python
   img='../input/100-bird-species/valid/BARN OWL/1.jpg'
   print(output(img))  # Outputs: 'BARN OWL'
   ```

3. **Plotting Results**:
   After training, the loss and accuracy curves can be visualized with `matplotlib`:

   ```python
   plt.plot(r.history['loss'], label='train loss')
   plt.plot(r.history['val_loss'], label='val loss')
   plt.legend()
   plt.show()
   ```

## Dependencies

- TensorFlow: 2.3.1
- Keras: 2.4.3
- Numpy
- Matplotlib

You can install all dependencies using:

```bash
pip install tensorflow keras numpy matplotlib
```

## References

1. **VGG16**: [Simonyan, K., & Zisserman, A. (2014). Very deep convolutional networks for large-scale image recognition. arXiv preprint arXiv:1409.1556.](https://arxiv.org/abs/1409.1556)

2. Dataset: The bird species dataset is from a publicly available collection. Make sure to properly organize your dataset before training.
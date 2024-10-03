import numpy as np
import tensorflow.keras.preprocessing.image as ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Activation, Dropout, Flatten, Dense


TRAINING_DIR = 'path_to_training_data'
VALIDATION_DIR = 'path_to_validation_data'


number_of_gestures = 10

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2)

validation_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    TRAINING_DIR,
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical')

validation_generator = validation_datagen.flow_from_directory(
    VALIDATION_DIR,
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical')

# Model Definition
model = Sequential([
    Conv2D(32, (3, 3), input_shape=(64, 64, 3)),
    Activation('relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(32, (3, 3)),
    Activation('relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Conv2D(64, (3, 3)),
    Activation('relu'),
    MaxPooling2D(pool_size=(2, 2)),

    Flatten(),
    Dense(64),
    Activation('relu'),
    Dropout(0.5),
    Dense(number_of_gestures),
    Activation('softmax')
])


model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=25,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size)

# Save Model
model.save('gesture_model.h5')

# Evaluate Model
eval_result = model.evaluate(validation_generator)
print(f"Test Loss: {eval_result[0]}, Test Accuracy: {eval_result[1]}")

import cv2
import mediapipe as mp
import numpy as np
import tensorflow as tf

# Replace this with the path to your trained model
MODEL_PATH = 'path_to_your_trained_model.h5'
model = tf.keras.models.load_model(MODEL_PATH)

# Initialize MediaPipe Hands model
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Function to preprocess the image
def preprocess_image(image, target_size=(28, 28)):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, target_size, interpolation=cv2.INTER_AREA)
    image = image / 255.0
    image = np.expand_dims(image, axis=[0, -1])
    return image

# Function to process frames and detect hands
def process_frame(image):
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            h, w, _ = image.shape
            x_min = int(min([landmark.x for landmark in hand_landmarks.landmark]) * w)
            x_max = int(max([landmark.x for landmark in hand_landmarks.landmark]) * w)
            y_min = int(min([landmark.y for landmark in hand_landmarks.landmark]) * h)
            y_max = int(max([landmark.y for landmark in hand_landmarks.landmark]) * h)

            hand_image = image[y_min:y_max, x_min:x_max]
            if hand_image.size == 0:
                return image
            preprocessed_image = preprocess_image(hand_image)
            prediction = model.predict(preprocessed_image)
            class_id = np.argmax(prediction)

            # TODO: Replace this with your labels
            class_name = f'Class {class_id}'

            cv2.putText(image, class_name, (x_min, y_min - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

    return image

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    processed_image = process_frame(image)
    cv2.imshow('Gesture Recognition', processed_image)

    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

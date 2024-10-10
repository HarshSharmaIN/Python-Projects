# LSTM Text Prediction Project

## Overview
This project implements a text prediction model using Long Short-Term Memory (LSTM) networks. LSTMs are a type of recurrent neural network (RNN) that are particularly effective for sequence prediction problems due to their ability to retain long-term dependencies. This model takes a sequence of text as input and predicts the next word in the sequence, allowing for natural language text generation.

## What is LSTM?
Long Short-Term Memory (LSTM) networks are designed to address the limitations of traditional RNNs, such as the vanishing gradient problem. LSTMs maintain a memory cell that can store information over long periods, using gates to control the flow of information. This architecture allows LSTMs to learn complex patterns in sequential data, making them ideal for tasks such as language modeling, text generation, and speech recognition.

## Project Description
This project uses an LSTM model to predict the next word in a given text based on previously provided words. The input text is tokenized and converted into sequences of numerical representations, which are then used to train the LSTM model. Once trained, the model can generate text predictions based on a given seed text.

## How It Works

### 1. Data Preparation
- **Tokenization**: The text data is tokenized to convert words into numerical representations using Keras' `Tokenizer`.
- **Sequence Creation**: Input sequences are created from the tokenized data. Each sequence consists of a series of words leading to the prediction of the next word.

### 2. Model Architecture
The model consists of the following layers:
- **Embedding Layer**: Transforms input sequences into dense vector representations.
- **LSTM Layers**: Two LSTM layers capture temporal dependencies in the data.
- **Dense Layer**: A Dense output layer with softmax activation predicts the next word from the vocabulary.

### 3. Training
- The model is trained on the prepared sequences using categorical crossentropy loss and the Adam optimizer.

### 4. Prediction
- After training, the model can take a seed text as input and iteratively predict subsequent words, creating a complete text sequence.

## Example Usage
To generate text predictions, provide a seed sentence:

```python
text = "what is the fee"

- Sample Output
  - what is the fee for car service

# DEEP LEARNING

## 🧠 Deep Learning

### Artificial Neural Network (ANN)
- A machine learning model inspired by the human brain
- Consists of interconnected neurons that learn patterns from data

---

### Neuron
- The basic building block of a neural network
- Receives inputs, performs calculations, and produces an output

---

### Equation of a Line
- Mathematical representation of a neuron before activation
- Commonly written as `y = mx + c` or `z = wx + b`

---

### Sigmoid Function
- Activation function that converts any value into a range between 0 and 1
- Often used to represent probabilities

---

### Linear Model + Sigmoid = Neuron
- A neuron first calculates a linear equation (`wx + b`)
- The result is passed through a sigmoid function
- Produces a probability-like output between 0 and 1

---

### Neural Network
- Network of interconnected neurons

### Input Layer
- Receives input data

### Hidden Layer
- Learns patterns from data

### Output Layer
- Produces predictions

### Flow
- Input → Hidden Layer(s) → Output

## 🏗️ Building an ANN with Keras

### Image Flattening
- `reshape()` → converts a 2D image into a 1D array
- `Flatten()` layer automatically performs image flattening before training

---

### Sequential Model
- `keras.Sequential()` → creates a neural network by stacking layers sequentially

---

### Input Layer
- `Flatten(input_shape=(28,28))`
- Accepts a 28×28 image and converts it into a single vector

---

### Hidden Layer
- `Dense(100, activation='relu')`
- Contains 100 neurons
- Uses ReLU activation to learn complex patterns

---

### Output Layer
- `Dense(10, activation='sigmoid')`
- Contains 10 neurons representing digits (0–9)
- Produces prediction probabilities

---

### Model Compilation
- `optimizer='adam'` → adjusts network weights efficiently
- `loss='sparse_categorical_crossentropy'` → loss function for multi-class classification
- `metrics=['accuracy']` → tracks prediction accuracy

---

### Model Training
- `fit(X_train, y_train, epochs=5)`
- Trains the neural network using training data
- `epochs` → number of times the model sees the entire dataset

---

### Model Evaluation
- `evaluate(X_test, y_test)`
- Measures model performance on unseen test data
- Returns loss and accuracy

---

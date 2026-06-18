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
- Mathematical representation of a neuron
- Commonly written as `y = mx + c` or `z = wx + b`

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

---

## ⚡ Activation Functions

### Why Activation Functions?
- Introduce non-linearity into neural networks
- Help neural networks learn complex patterns
- Convert neuron output into a useful form

---

### Step Function
- Produces either 0 or 1
- Simple but rarely used in modern neural networks

---

### Sigmoid Function
- Converts values to a range between 0 and 1
- Often interpreted as probabilities
- Common in binary classification output layers

---

### Tanh Function
- Outputs values between -1 and 1
- Zero-centered version of sigmoid
- Often performs better than sigmoid

---

### ReLU (Rectified Linear Unit)
- Returns 0 for negative values
- Returns input value for positive values
- Most commonly used activation function in hidden layers

---

### Leaky ReLU
- Similar to ReLU but allows small negative values
- Helps reduce the "dying ReLU" problem

---

### Softmax
- Converts outputs into probability distribution
- Sum of all outputs equals 1
- Commonly used in multi-class classification output layers

---

### Which Activation Function to Use?

| Layer | Common Choice |
|---------|---------------|
| Hidden Layer | ReLU |
| Hidden Layer (ReLU issues) | Leaky ReLU |
| Binary Classification Output | Sigmoid |
| Multi-Class Classification Output | Softmax |
| Rarely Used Today | Step, Tanh |


### Derivative
- Measures how fast a function changes with respect to a variable
- Indicates the slope of a curve at a specific point
- Used to determine the direction of optimization

---

### Partial Derivative
- Measures the change of a function with respect to one variable while keeping other variables constant
- Used when a function depends on multiple variables

---

### Applications in Deep Learning
- Calculates how changes in weights affect prediction error
- Helps determine how weights should be updated
- Fundamental to Backpropagation
- Used by Gradient Descent to minimize loss and improve model accuracy

### Matrix
- A collection of numbers arranged in rows and columns
- Used to represent data and weights in neural networks

---

### Basic Operations
- Addition
- Subtraction
- Multiplication
- Transpose

---

### Applications in Deep Learning
- Stores input data
- Stores weights and biases
- Used for calculations between layers
- Makes neural network computations faster and more efficient

---

### Key Idea
- Data → Matrix
- Weights → Matrix
- Neural Network → Matrix Operations
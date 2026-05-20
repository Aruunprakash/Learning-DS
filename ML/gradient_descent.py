import numpy as np

# Function to perform Gradient Descent
def gradient_descent(x,y):

    # Initialize slope (m) and intercept (b) to 0
    m_curr = b_curr = 0

    # Number of times algorithm will update values
    iterations = 100

    # Controls step size while moving towards minimum error
    learning_rate = 0.01

    # Total number of data points
    n = len(x)

    # Loop through specified iterations
    for i in range(iterations):

        # Prediction function of linear regression
        # y = mx + b
        y_predicted = m_curr * x + b_curr

        # Calculate cost (Mean Squared Error)
        # Measures difference between actual and predicted values
        cost = (1/n) * sum(val**2 for val in y-y_predicted)

        # Partial derivative with respect to m (slope)
        # Shows direction and amount of slope change needed
        m_derivative = -(2/n) * sum(x*(y-y_predicted))

        # Partial derivative with respect to b (intercept)
        # Shows direction and amount of intercept change needed
        b_derivative = -(2/n) * sum((y-y_predicted))

        # Update slope using Gradient Descent formula
        # New m = Old m - learning_rate × derivative
        m_curr = m_curr - learning_rate * m_derivative

        # Update intercept using Gradient Descent formula
        b_curr = b_curr - learning_rate * b_derivative

        # Print updated values after each iteration
        print("m {} , b {} , cost {} , iteration {}".format(
            m_curr,
            b_curr,
            cost,
            i
        ))

# Input feature values
x = np.array([1,2,3,4,5])

# Actual target values
y = np.array([5,7,9,11,13])

# Call function
gradient_descent(x,y)
# 🤖 Machine Learning

## 📌 Overview
Machine Learning enables systems to learn from data and make predictions using mathematical models and algorithms.

---

## 🧠 Fundamentals
- Machine Learning  
- Deep Learning  
- Mathematical Models  

---

## 📈 Simple Linear Regression
- Linear Model (`y = mx + c`)  
- `LinearRegression()`  
- `fit()`  
- `predict()`  
- `coef_` & `intercept_`  
- Prediction & Visualization  

---

## 🧰 Libraries
- Scikit-Learn (`sklearn`)  
- Linear Model  


## 📈 Multiple Linear Regression

- Multiple Input Variables  
- Missing Value Handling (`fillna()`, `median()`)  
- Features (`X`) passed as 2-D array [[]] & Target (`y`)  
- `fit()` & `predict()` passed [[]]  values inside it  
- DataFrame / 2D Array Prediction  
- `word2number`  

---

## 📉 Error & Optimization

### 🎯 Prediction Function
- Predicts output using trained data  

---

### 📉 Mean Squared Error (MSE)
- Measures prediction error  
- Lower value → better model performance  

---

### 📈 Gradient Descent
- Minimizes error by updating model parameters step by step  

### ⚙️ Learning Rate & Iterations
- Learning Rate → controls update step size  
- Small → slower but stable  
- Large → faster but may overshoot  
- Iterations → number of updates performed  
- Increase gradually for better convergence  

## 🔍 Convergence Check

- `math.isclose()` → checks if two values are nearly equal  
- `rel_tol` → sets relative tolerance level  
- `rel_tol=1e-20` → very small tolerance for precise comparison  
- Useful for checking if Gradient Descent has converged  

---

## 💾 Model Saving & Loading

### 📦 Pickle
- `pickle.dump()` → saves trained model into a file  
- `pickle.load()` → loads saved model back into program  
- `'wb'` → write binary mode  
- `'rb'` → read binary mode  

---

### ⚡ Joblib
- `joblib.dump()` → saves model efficiently  
- Faster and preferred for large ML models  

---
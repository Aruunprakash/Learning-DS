# 🤖 Machine Learning

## 📌 Overview
Machine Learning enables systems to learn patterns from data and make predictions using mathematical models and algorithms.

---

## 🧠 Fundamentals
- Machine Learning  
- Deep Learning  
- Mathematical Models  

---

## 🧰 Libraries
- Scikit-Learn (`sklearn`)  
- Linear Models  

---

## 📈 Simple Linear Regression
- Linear Equation (`y = mx + c`)  
- `LinearRegression()`  
- `fit()` & `predict()`  
- `coef_` & `intercept_`  
- Prediction & Visualization  

---

## 📈 Multiple Linear Regression
- Multiple Input Variables  
- Missing Value Handling (`fillna()`, `median()`)  
- Features (`X`) & Target (`y`)  
- DataFrame / 2D Array Prediction  
- `word2number`  

---

## 🔢 Categorical Data Handling

### 📦 Encoding
- Label Encoding (`LabelEncoder`)  
- `fit_transform()`  
- One Hot Encoding (`OneHotEncoder`)  

### 🔄 Feature Transformation
- `ColumnTransformer()`  
- `transformers`  
- `drop='first'`  
- `dtype=int`  
- `remainder='passthrough'`  

### 🐼 Pandas Utilities
- Dummy Variables  
- `pd.get_dummies()`  
- `df.drop()`  

---

## 📉 Model Optimization

### 🎯 Prediction
- Prediction Function  

### 📉 Error Measurement
- Mean Squared Error (MSE)  

### 📈 Optimization
- Gradient Descent  
- Learning Rate  
- Iterations  

### 🔍 Convergence
- `math.isclose()`  
- `rel_tol`  

---

## 💾 Model Persistence
- Pickle (`dump()`, `load()`)  
- Joblib (`dump()`)  

---

## 📊 Model Evaluation
- `model.score()`  

---

## 🧪 Train-Test Split & Evaluation

### 📂 Data Splitting
- `train_test_split()` → splits data into training and testing sets  
- `test_size` → defines proportion of test data  
- `random_state` → ensures consistent/random reproducible split
-  Compare predictions with `X_test` / actual values 
-  Score to check accuracy

---

## 📊 Logistic Regression

### 📌 Introduction
- Logistic Regression → classification algorithm used to predict categories/classes  
- Used for binary outcomes such as Yes/No, Pass/Fail, Spam/Not Spam

---

### 📈 Probability Prediction
- `predict_proba()` → returns probability for each class  
- Helps understand prediction confidence  

---
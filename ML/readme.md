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

## 📈 Regression

### Simple Linear Regression
- Linear Equation (`y = mx + c`)
- `LinearRegression()`
- `fit()` & `predict()`
- `coef_` & `intercept_`
- Prediction & Visualization

### Multiple Linear Regression
- Multiple Input Variables
- Missing Value Handling (`fillna()`, `median()`)
- Features (`X`) & Target (`y`)
- DataFrame / 2D Array Prediction
- `word2number`

---

## 🔢 Categorical Data Handling

### Encoding
- Label Encoding (`LabelEncoder`)
- `fit_transform()`
- One Hot Encoding (`OneHotEncoder`)

### Feature Transformation
- `ColumnTransformer()`
- `transformers`
- `drop='first'`
- `dtype=int`
- `remainder='passthrough'`

### Pandas Utilities
- Dummy Variables
- `pd.get_dummies()`
- `df.drop()`

---

## 📉 Model Optimization

### Prediction
- Prediction Function

### Error Measurement
- Mean Squared Error (MSE)

### Optimization
- Gradient Descent
- Learning Rate
- Iterations

### Convergence
- `math.isclose()`
- `rel_tol`

---

## 💾 Model Persistence
- Pickle (`dump()`, `load()`)
- Joblib (`dump()`)

---

## 🧪 Model Evaluation

### Train-Test Split
- `train_test_split()`
  - `test_size`
  - `random_state`

### Performance
- Compare Predictions vs Actual Values
- `model.score()`

---

## 🎯 Classification

### Logistic Regression
- Binary Classification
- `predict()`
- `predict_proba()`

### Multi-Class Classification
- Multi-Class Prediction
- `dir()`
- `matshow()`
- `confusion_matrix()`
- `sns.heatmap()`

### Decision Trees
- `DecisionTreeClassifier()`
- Tree-Based Classification
  - `criterion='gini'`
  -  `criterion='entropy'`

---
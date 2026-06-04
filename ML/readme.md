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
  - linear_model
  - preprocessing
  - model_selection
  - compose

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

### Support Vector Machines (SVM)
- SVM Classification
- Feature Transformation (`apply()`)
- Hyperparameter Tuning (`C`, `kernel`, `gamma`)

---

### Random Forest
- Ensemble Methods 
- Random Forest :- decision tree ensemble
- `n_estimators` :- no of trees
## 🔄 Model Validation & Hyperparameter Tuning

---


### 📌 K-Fold Cross Validation
- Splits dataset into multiple folds
- Trains and tests model on different data partitions
- Provides more reliable performance evaluation

---

### ⚙️ Parameters
- `n_splits` → number of folds to create

---

### 🔀 KFold
- `KFold()` → creates K-Fold validator
- `kf.split()` → generates train-test indices for each fold

---

### 🎯 Stratified K-Fold
- `StratifiedKFold()` → preserves class distribution across folds
- Useful for classification problems

---

### 📊 Cross Validation Score
- `cross_val_score()` → evaluates model across all folds
- Returns performance scores for each fold

---

### 🔧 Hyperparameter Tuning
- Adjusts model parameters to improve performance
- Helps find the best model configuration

---
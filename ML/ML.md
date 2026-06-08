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
  - `linear_model`
  - `preprocessing`
  - `model_selection`
  - `compose`

---

# 🎯 Supervised Learning

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

### Optimization
- Mean Squared Error (MSE)
- Gradient Descent
- Learning Rate
- Iterations
- `math.isclose()`
- `rel_tol`

---

## 🛠️ Data Preprocessing

### Missing Values
- `fillna()`
- `median()`

### Encoding
- Label Encoding (`LabelEncoder`)
- `fit_transform()`
- One Hot Encoding (`OneHotEncoder`)
- Dummy Variables

### Feature Transformation
- `ColumnTransformer()`
- `transformers`
- `drop='first'`
- `dtype=int`
- `remainder='passthrough'`

### Pandas Utilities
- `pd.get_dummies()`
- `df.drop()`

---

## 🎯 Classification

### Logistic Regression
- Binary Classification
- `predict()`
- `predict_proba()`

### Multi-Class Classification
- `dir()`
- `matshow()`
- `confusion_matrix()`
- `sns.heatmap()`

### Decision Trees
- `DecisionTreeClassifier()`
- `criterion='gini'`
- `criterion='entropy'`

### Support Vector Machines (SVM)
- Feature Transformation (`apply()`)
- Hyperparameter Tuning
  - `C`
  - `kernel`
  - `gamma`

### Random Forest
- Ensemble Learning
- `RandomForestClassifier()`
- `n_estimators`

---

### Naive Bayes
- Gaussian Naive Bayes (`GaussianNB`)
- Probabilistic Classification
- `predict()` & `predict_proba()`

---

## 🧪 Model Evaluation & Validation

### Train-Test Split
- `train_test_split()`
- `test_size`
- `random_state`

### Model Evaluation
- Compare Predictions vs Actual Values
- `model.score()`

### Cross Validation
- K-Fold Cross Validation
- `n_splits`
- `KFold()`
- `kf.split()`
- Stratified K-Fold
- `cross_val_score()`

### Hyperparameter Tuning
- Parameter Optimization
- Model Selection

---

## 💾 Model Persistence
- Pickle (`dump()`, `load()`)
- Joblib (`dump()`)

---

## 📝 Text Processing & Pipelines

### 🔤 Count Vectorizer
- `CountVectorizer()` → converts text into numerical feature vectors
- Counts occurrence of words in documents
- Used for text classification and NLP tasks

---

### 🔄 Pipeline
- `Pipeline()` → combines multiple preprocessing and modeling steps
- Automates workflow from input data to prediction
- Helps keep code clean and organized

---

### ⚙️ Common Usage
- `CountVectorizer()` → text preprocessing
- ML Model (`GaussianNB`, `LogisticRegression`, etc.) → classification
- `Pipeline()` → connects both into a single workflow

---

# 🔍 Unsupervised Learning

## 🎯 K-Means Clustering
- K-Means Algorithm
- `MinMaxScaler`
- `fit()` & `transform()`
- `fit_predict()`
- `inertia_`
- `cluster_centers_`

---


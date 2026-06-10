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

## 👥 K-Nearest Neighbors (KNN)

### 📌 Introduction
- Supervised learning algorithm for classification and regression
- Predicts based on nearest data points

---

### ⚙️ Parameters
- `n_neighbors` → number of nearest neighbors considered

---

### 📊 Evaluation

#### `classification_report()`
- Summarizes classification performance
- Includes:
  - Precision
  - Recall
  - F1-Score
  - Support

---

### ✅ Characteristics
- Distance-based learning
- Simple and easy to implement
- Sensitive to feature scaling

---

## 🎒 Bagging (Bootstrap Aggregating)

### 📌 Introduction
- Ensemble technique that combines predictions from multiple models
- Reduces variance and helps prevent overfitting

---

### 🌳 Bagged Trees
- Multiple Decision Trees trained on different random subsets of data
- Final prediction is based on voting (classification) or averaging (regression)

---

### 📊 Data Distribution
- `df.Outcome.value_counts()` → shows count of each class
- Useful for checking class balance before training

---

### 🧪 Stratified Split
- `stratify=y` → preserves class distribution during train-test split
- Useful for imbalanced datasets

---

### 🧰 Scikit-Learn
- `from sklearn.ensemble import BaggingClassifier`
- `BaggingClassifier()` → creates bagging model

---

### ⚙️ Parameters

- `n_estimators=100` → number of base models/trees
- `max_samples=0.8` → uses 80% of training samples for each model
- `oob_score=True` → evaluates model using out-of-bag samples
- `random_state=0` → ensures reproducible results

---

### 📈 Evaluation
- `oob_score_` → out-of-bag performance score
- Alternative to validation set for model evaluation

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

## 🔧 Hyperparameter Tuning

### 📂 Train-Test Split
- `train_test_split()` → separates training and testing data
- `test_size` → controls test data proportion
- `random_state` → ensures reproducible results

---

### ⚙️ SVM Tuning
- `C` → controls misclassification penalty
- `kernel` → defines decision boundary type
- `gamma` → controls influence of data points

---

### 🔄 K-Fold Validation
- `cross_val_score(model, X, y, cv)` → evaluates model across multiple folds
- `cv` → number of folds

---

### 🔍 Grid Search
- `GridSearchCV()` → tests all parameter combinations
- Finds best hyperparameters automatically

---

### 🎲 Random Search
- `RandomizedSearchCV()` → tests random parameter combinations
- Faster than Grid Search on large parameter spaces

---

### 📈 Logistic Regression Tuning
- `solver='lbfgs'` → optimization algorithm
- `max_iter=1000` → maximum training iterations

---

## ⚖️ Bias & Variance

### 📉 Bias
- Error caused by overly simple assumptions in the model
- High Bias → Underfitting
- Model fails to capture important patterns in data

---

### 📈 Variance
- Error caused by excessive sensitivity to training data
- High Variance → Overfitting
- Model learns noise instead of general patterns

---

### 🎯 Bias-Variance Tradeoff
- Good models balance bias and variance
- Goal is to achieve strong performance on unseen data

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

## 📉 Principal Component Analysis (PCA)

### 📌 Introduction
- Unsupervised dimensionality reduction technique
- Reduces the number of features while preserving important information
- Helps simplify data and improve model performance

---

### 📊 Feature Scaling

#### `StandardScaler()`
- Standardizes data before applying PCA
- Transforms features to have mean = 0 and standard deviation = 1
---

### ⚙️ Parameters

#### `n_components`
- Number of principal components to keep
- Can be a fixed number or variance ratio

---

### 🎯 Methods & Attributes
- `explained_variance_ratio_` → shows variance captured by each component

---

### ✅ Benefits
- Reduces dimensionality
- Removes redundancy between features
- Speeds up model training

---


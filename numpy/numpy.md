## 🧮 NumPy – Basics & Operations

### 📦 Arrays
- NumPy arrays store multiple values efficiently  
- Supports N-dimensional arrays  

---

### 🔍 Indexing & Accessing
- Elements accessed using indices  
- Supports multi-dimensional indexing  

---

### ✂️ Slicing & Range Access
- Extract subarrays using slicing  
- `:` selects all elements in a dimension  
- Supports accessing values using ranges  

---

### 🔗 Concatenation
- Combines multiple arrays  
- Can join along rows or columns  

---

### 📐 Dimensions & Shape
- `ndim` → number of dimensions  
- `reshape()` → changes array shape  
- `ravel()` → flattens array into 1D  

---

### 🧾 Data Type & Memory
- `dtype` → data type of elements  
- `size` → total number of elements  
- `itemsize` → memory used per element  

---

### 🔢 Array Initialization
- `zeros()` / `ones()` → initialize arrays  
- `arange()` → generate values in range  
- `linspace()` → evenly spaced values  

---

### ➕ Arithmetic Operations
- Supports basic arithmetic operations  
- Vectorized computations  
- Element-wise operations between arrays  

---

### ⚖️ Comparison Operations
- Compare elements using relational operators  
- Returns boolean arrays  

---

### 📡 Broadcasting
- Performs operations on arrays of different shapes  
- Automatically aligns compatible dimensions  

---

### 📊 Aggregate Functions
- `min()` / `max()` → smallest & largest values  
- `sum()` → total sum across array or axis  

---

### 🎯 Filtering
- Boolean filtering for conditional selection  
- Supports AND / OR conditions  

---

### 🔀 where() Function
- Returns values based on conditions  
- Useful for conditional replacement/filtering  

---

### 🎲 Random Number Generator
- Generates random values and arrays  
- Used for simulations and sampling  

---

## 🚀 NumPy Mini Projects

### 🏥 The Healthcare Data "Healer"

**The Core:**  
Data Cleaning and Imputation  

**Brief Explanation:**  
Created a synthetic dataset of patient health metrics (Age, BP, Heart Rate) and intentionally corrupted it with missing values (`-1`). Used Boolean Masking and Mean Imputation to "heal" the data and applied Min-Max Normalization to prepare it for a Machine Learning model.

---

### 🛰️ The Satellite Coverage Optimizer

**The Core:**  
Spatial Analysis and Broadcasting  

**Brief Explanation:**  
Simulated 50 satellites at random coordinates across a map. Using Vectorized Math and the Pythagorean theorem, calculated the distance from a specific user to every satellite in one line of code, used `np.argmin` to find the nearest provider, and applied Boolean Indexing to detect signal "dead zones."

---

### ❤️ The Weighted Health Risk Scorer

**The Core:**  
Feature Engineering and Aggregation  

**Brief Explanation:**  
After normalizing health data, applied a Weighting Vector to signify that certain columns (like Blood Pressure) were more critical than others. Used Matrix-Vector Multiplication and `axis=1` Summation to collapse the matrix into a single "Risk Score" for every patient.

---
# PANDAS

## 🐼 Pandas – DataFrames

### 📊 DataFrame
- Tabular data structure in Pandas  
- Organizes data into rows and columns  

---

### 🧱 Creating DataFrame
- Can be created from:
  - CSV files  
  - Excel files  
  - Python dictionaries  
  - Tuple lists  
  - List of dictionaries  

- Keys become columns and values become data  

---

### 👀 head()
- Displays first few rows of dataset  
- Useful for quick inspection  

---

### 🔍 Filtering & Conditions
- Data can be filtered using conditions  
- Example: `df[df.temperature < 32]`  

---

### 📈 Basic Operations
- `mean()` → average value  
- `min()` → minimum value  
- `max()` → maximum value  

---

### 🧾 describe()
- Provides statistical summary of dataset  
- Includes count, mean, std, min, max, etc.  

---

### 📄 CSV Handling
- `read_csv` → loads CSV file into DataFrame  
- `to_csv` → exports DataFrame to CSV  
- `header` → defines column title row  
- `index` → include/exclude row labels  
- `tail()` → displays last few rows  
- `na_values` → treats specific values as NaN  
- `nrows` → reads limited number of rows  

---

### 📊 Excel Handling
- `read_excel` → loads Excel file  
- `to_excel` → saves DataFrame to Excel  
- `sheet_name` → specifies worksheet  
- `startrow` / `startcol` → defines write position  
- `pd.ExcelWriter` → writes multiple sheets in one file  

---

### 🛠️ Data Cleaning
- `NaN` → represents missing values
---

### 🔄 Missing Value Handling & Date Utilities
- `parse_dates` → converts date columns while loading data  
- `inplace` → modifies original DataFrame directly  
- `fillna()` → fills missing values  
- `ffill` → forward fill using previous value  
- `bfill` → backward fill using next value  
- `method` → specifies filling strategy in `fillna()`  
- `interpolate()` → estimates missing numeric values  
- `dropna()` → removes missing values  
- `limit` → restricts number of fills/removals  
- `thresh` → minimum non-NaN values required  
- `date_range()` → generates sequence of dates  

---

## 🐼 Pandas – Replace & Mapping

- `replace()` → replaces existing values  
- Replace using Lists → replace multiple values together  
- Replace using Dictionary → map old values to new values  
- Value Mapping → transform values using key-value mapping  
- Multiple Value Replacement → replace values using two lists  

---
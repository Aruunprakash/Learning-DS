# 🕒 Pandas – Time Series

- Time Series → data indexed by date and time  
- `parse_dates` → converts date columns while loading data  
- `index_col` → sets date column as DataFrame index  

---

### 📅 Accessing Time Series Data
- `df.loc[]` → access rows using date labels  
- `df["2017-01-01":"2017-01-07"]` → access date ranges  

---

### 📊 Resampling & Plotting
- `resample()` → changes data frequency (daily, weekly, monthly, etc.)  
- Common frequencies:
  - `"ME"` → month end  
  - `"W"` → weekly  
- Often used with aggregation functions like `mean()` or `sum()`  
- Resampled data can be visualized using plots  

---

## 🕒 Pandas – Date Range & Frequency

- `date_range()` → generates sequence of dates/timestamps  
- `start` → starting date  
- `end` / `periods` → ending date or number of periods  
- `freq` → defines frequency of dates  
  - `"D"` → daily  
  - `"B"` → business days  
  - `"H"` → hourly  
  - `"W"` → weekly  

---

### 📌 Indexing with Dates
- `set_index()` → sets column as DataFrame index  
- `inplace=True` → modifies original DataFrame directly  

---

### 🔄 Frequency Conversion
- `asfreq()` → converts data to specified frequency  
- `method="pad"` → fills missing values using previous value  
- Common frequencies:
  - `"D"` → daily  
  - `"H"` → hourly  
  - `"W"` → weekly  

---

### 🎲 Time Series Creation
- `pd.Series()` → creates time series data  
- `np.random.randint()` → generates random integer values  
- Date ranges can be used as index for time series  

---
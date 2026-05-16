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

## 🕒 Pandas – Holiday Handling in Time Series

### 📅 Federal Holiday Calendars
- `USFederalHolidayCalendar` → provides predefined U.S. federal holidays  
- `CustomBusinessDay` → creates business-day frequency excluding holidays  

---

### 🏢 Custom Business Days
- `calendar` → applies holiday calendar to business days  
- Useful for financial and business time-series analysis  

---

### 🎉 Creating Custom Holidays
- `month` → specifies holiday month  
- `day` → specifies holiday date  
- `observance` → adjusts holiday observation rules  
- `weekmask` → defines working days in a week  
- `holidays=["YYYY-MM-DD"]` → manually defines holiday dates  

---

### 📊 Use Cases
- Skip weekends and holidays in analysis  
- Generate holiday-aware date ranges  
- Improve accuracy in business/time-series datasets  

---

## 🕒 Pandas – DateTime Conversion

- `to_datetime()` → converts data into datetime format  
- `format="mixed"` → handles multiple date formats  
- `dayfirst=True` → interprets day before month  

- `pd.to_datetime('5$1$2017', format="%d$%m$%Y")`
  → converts custom formatted date strings  

---

### ⚠️ Error Handling
- `errors` → controls invalid date handling  
  - `"raise"` → throws error  
  - `"coerce"` → converts invalid values to `NaT`  
  - `"ignore"` → keeps original values  

- `NaT` → represents missing/invalid datetime values  

---

### ⏱️ Epoch Time
- `unit` → defines epoch time unit  
  - `"s"` → seconds  
  - `"ms"` → milliseconds  
  - `"us"` → microseconds  

---

## 🕒 Pandas – Period & PeriodIndex

- `Period` → represents a span of time instead of a specific timestamp  
- `dir(y)` → displays available properties and methods of period object  

---

### 📅 Period Properties
- `start_time` → starting timestamp of period  
- `end_time` → ending timestamp of period  
- `month` → extracts month value  
- `day` → extracts day value  
- `hour` → extracts hour value  

---

### ➕ Arithmetic Operations & Offsets
- Arithmetic operations (`+`, `-`) → shift periods forward or backward  
- Offsets → move periods by specified frequency units  

---

### 📊 Frequency Conversion
- Quarterly periods → represent data by quarter (`Q`)  
- `asfreq()` → converts period frequency  
- Convert to:
  - Month (`M`)  
  - Day (`D`)  

---
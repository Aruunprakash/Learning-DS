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

## 🐼 Pandas – GroupBy

- `groupby()` → groups data based on column values  
- GroupBy Arguments → define grouping columns and behavior  
- Access Groups using `for` loop → iterate through grouped data  
- `get_group()` → retrieves a specific group  
- `numeric_only` → used when operations should apply only to numeric columns  

---

## 🐼 Pandas – Concat & Series

- `concat()` → combines DataFrames or Series  
- `ignore_index` → resets index after concatenation  
- `keys` → adds labels to concatenated objects  
- `axis` → defines row-wise or column-wise concatenation  
- Index in DataFrame Creation → maintains order and accurate alignment  
- `Series` → one-dimensional labeled data structure  

---

## 🐼 Pandas – Merge & Join

- `merge()` → combines DataFrames based on common columns  
- Inner Join → returns matching records from both DataFrames  
- Outer Join → returns all records with NaN for non-matches  
- Left Join → keeps all rows from left DataFrame  
- Right Join → keeps all rows from right DataFrame  
- `indicator` → shows source of merged rows  
- `suffixes` → differentiates same column names after merge  

---

## 🐼 Pandas – Pivot & Pivot Table

- `pivot()` → reshapes data using index, columns, and values  
- `index` → defines row grouping  
- `columns` → defines column categories  
- `values` → specifies data values to display  

---

- `pivot_table()` → creates summarized pivot tables  
- `aggfunc` → defines aggregation function (sum, mean, count, etc.)  
- `margins` → adds total rows and columns  
- `Grouper` → groups data dynamically (commonly dates/time)  
- `freq` → sets grouping frequency (daily, monthly, yearly, etc.)  
- Supports grouping and summarization for different cases  

---

## 🐼 Pandas – Melt

- `melt()` → transforms wide-format data into long-format  
- `id_vars` → columns kept fixed during transformation  
- `var_name` → name assigned to variable column  
- Useful for reshaping and organizing data  

---

## 🐼 Pandas – Crosstab

- `pd.crosstab()` → generates frequency table between columns  
- `pd.crosstab(df.row_name, df.column_name)` → compares categorical data  
- `margins=True` → adds row/column totals  
- `normalize="index"` → normalizes values row-wise into proportions  
- `values` → specifies data for aggregation  
- `aggfunc = np.average` → applies average aggregation in crosstab  

---

### 📓 Notebook Utility
- `Shift + Tab` → displays function documentation and parameter help in notebooks  

---

## 🕒 Pandas – Time Series

- Time Series → date/time indexed data  
- `parse_dates` → converts columns into datetime format  
- `index_col` → sets date column as index  
- `df.loc[]` → accesses rows using date labels  
- Date Range Access → filter data between dates  

---

### 📊 Resampling & Frequency
- `resample()` → changes time frequency of data  
- Frequencies:
  - `"D"` → daily  
  - `"W"` → weekly  
  - `"ME"` → month end  
  - `"H"` → hourly  

- `asfreq()` → converts data frequency  
- `method="pad"` → fills values using previous entry  

---

### 📅 Date Utilities
- `date_range()` → generates sequence of dates  
- `set_index()` → sets datetime index  
- `inplace=True` → modifies original DataFrame  

---

### 🎲 Time Series Creation
- `pd.Series()` → creates time series  
- `np.random.randint()` → generates random values  

---

### 🎉 Holiday Handling

- `USFederalHolidayCalendar` → predefined U.S. federal holidays  
- `CustomBusinessDay` → custom business-day frequency excluding holidays  
- `calendar` → applies holiday calendar to business dates  
- `month` / `day` → define custom holiday dates  
- `observance` → adjusts holiday observation rules  
- `weekmask` → defines working days of the week  
- `holidays=["YYYY-MM-DD"]` → manually specifies holiday dates  

---

## 🕒 Pandas – DateTime Handling

- `to_datetime()` → converts values into datetime format  
- `format` → specifies custom date format  
- `dayfirst=True` → treats day before month  
- `errors` → handles invalid datetime values  
- `NaT` → represents missing/invalid datetime  
- Epoch Time → datetime conversion using `unit`  

---

## 🕒 Pandas – Period & PeriodIndex

### 📅 Period
- `Period` → represents a span of time instead of a specific timestamp  
- `start_time` → beginning of period  
- `end_time` → end of period  
- `month`, `day`, `hour` → extracts period information  
- Arithmetic operations (`+`, `-`) → shifts periods  
- Offsets → moves periods based on frequency  
- Quarterly periods (`Q`) → represents quarter-based data  
- `asfreq()` → converts period frequency (Month, Day, etc.)  

---

### 📊 PeriodIndex
- `PeriodIndex` → index using time periods  
- Arguments:
  - `start`
  - `end`
  - `periods`
  - `freq`

- `period_range()` → generates sequence of periods  
- `np.random.randn()` → generates random values  
- `["start":"end"]` → slices period ranges  
- `df.index.map()` → applies functions to period index  
- `x.start_time` → extracts start time  
- `x.end_time` → extracts end time  

---

## 🕒 Pandas – Time Zone Handling

- `tz_localize()` → assigns timezone to datetime data  
- `tz_convert()` → converts data between time zones  
- `df.index` → accesses datetime index  
- `dateutil` → supports parsing and timezone handling  

---
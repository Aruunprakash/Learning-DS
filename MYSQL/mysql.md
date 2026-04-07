## 📊 Data Science – MySQL (Theory)

### 🧠 Introduction
MySQL is a relational database management system used to store, manage, and retrieve structured data.  
A **database** is a collection of tables, and each table consists of rows and columns.

---

### 🗂️ Core Concepts

**Database**
- Organized collection of data  
- Contains multiple tables  

**Table**
- Structure to store data in rows and columns  

**Column**
- Represents an attribute (e.g., name, rating)  

**Row**
- Represents a single record  

---

### 🔍 Data Retrieval Concepts

**SELECT**
- Used to retrieve data from a table  

**WHERE**
- Filters data based on conditions  

**DISTINCT**
- Returns unique values  

**COUNT**
- Gives the number of records  

**LIKE**
- Used for pattern matching in text  

---

### ⚙️ Conditional Logic

**AND / OR**
- Combine multiple conditions  

**BETWEEN**
- Filters values within a range  

**IN**
- Matches values from a given list  

**NULL**
- Represents missing or undefined values  

---

### 📊 Data Organization

**ORDER BY**
- Sorts data (ascending/descending)  

**LIMIT**
- Restricts number of results  

**OFFSET**
- Skips a certain number of records  


### 📈 Aggregation & Analysis

**MIN / MAX**
- Find smallest or largest values  

**AVG**
- Calculates average  

**ROUND**
- Controls decimal precision  

**GROUP BY**
- Groups data for aggregation  

**AS (Alias)**
- Renames columns for readability  

### 🚀 Key Insights
- MySQL is **case-insensitive** for queries  
- Efficient querying improves performance  
- Aggregations help in data analysis  
- Filtering reduces unnecessary data retrieval  

## 📊 MySQL – Advanced Concepts

### HAVING
- Used with GROUP BY  
- Filters aggregated data  
- Applied after grouping  

---

### Calculated Columns
- Create new values using expressions  
- Derived from existing columns  

---

### Date Functions & Formulas
- CURDATE() → current date  
- YEAR() → extract year  
- Used for calculations (like age, profit)  

---

### IF Condition
- Used for simple conditions  
- Returns value based on true/false  

---

### CASE Statement
- Used for multiple conditions  
- More flexible than IF  

## 📊 MySQL – Joins

### 🔗 INNER JOIN
- Returns only matching records from both tables  
- Rows included only when join condition is satisfied  

---

### ⬅️ LEFT JOIN
- Returns all records from left table  
- Matching records from right table  
- Non-matching values → NULL  

---

### ➡️ RIGHT JOIN
- Returns all records from right table  
- Matching records from left table  
- Non-matching values → NULL  

---

### 🔄 FULL JOIN
- Returns all records from both tables  
- Fills NULL where no match exists  
- Not directly supported in MySQL  
- Achieved using UNION of LEFT and RIGHT JOIN  

---


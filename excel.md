## Basics of Business Math & Statistics in Excel for Data Science

### 📅 Day 1

* Basics:

  * Conditional Formatting

    * Used to highlight important data based on conditions

---

* Formulas:

  * `=SUM()`

    * Select a column using left-click and drag to calculate total

  * `=UNIQUE()`

    * Used to extract unique values (grouping by category)

---

* Built-in Options / Functions:

  * Sort (built-in option)
  * AutoSum (quick calculation tool)
  * Filter (available in Insert → helps filter unique data)
  * Create Table (Insert → Table)
  * Slicer (Table Design → Insert Slicer for filtering data visually)

---

* Total, Average & Revenue:

  * Basic currency conversion using simple Excel formulas

  * Count:

    * `=COUNT(Table[column])`

  * CountIF:

    * `=COUNTIF(Table[column], "Bollywood")`

  * Sum:

    * `=SUM(Table[column])`

  * Average:

    * `=AVERAGE(Table[column])`

### 📅 Day 2

* Basics of Profit & Loss:

  * Profit and Loss concepts

  * P&L Percentage:

    * Profit / Budget

  * Market Share:

    * Example: Swiggy vs Zomato (service-based comparison)

  * Target:

    * Setting business goals and measuring performance

---

* Mean, Median & Mode:

  * Mean:

    * Average of all values

  * Median:

    * Used when outliers are present
    * Sort data and take midpoint

      * Even → Average of two middle values
      * Odd → Middle value

  * Mode:

    * Most frequently occurring value

---

* Variance & Standard Deviation:

  * Variance:

    * Measures how far data points are from the mean
    * Formula:

      * Variance = Sum of (squared differences from mean) / Number of values
    * Excel:

      * `=VAR.P()` (for entire population)

  * Standard Deviation:

    * Square root of variance
    * Shows spread of data
    * Excel:

      * `=STDEV.P()`

  * Real-life Use Case:

    * Stock market volatility

---

* Correlation:

  * Measures relationship between two variables

  * Types:

    * Positive Correlation:

      * Close to +1 → both variables increase together

    * Negative Correlation:

      * Close to -1 → one increases, other decreases

    * Zero Correlation:

      * No clear relationship

  * Excel Function:

    * `=CORREL(array1, array2)`

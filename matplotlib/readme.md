# MATPLOTLIB

## 📈 Matplotlib – Basics

- `matplotlib.pyplot` → plotting module for visualization  
- `plt.plot()` → creates line plots  
- `color` → defines plot color  
- `linewidth` → controls line thickness  
- `linestyle` → defines line pattern/style  
- `xlabel()` → labels x-axis  
- `ylabel()` → labels y-axis  
- `title()` → adds plot title  

---

## 📈 Matplotlib – Formatting & Styling

- Format Strings → shorthand styling (e.g., `"g--*"`)  
- Marker (`marker`) → defines point style  
- Linestyle (`linestyle`) → controls line pattern  
- Color (`color`) → supports named and hexadecimal colors  
- `markersize` → controls marker size  
- `alpha` → adjusts transparency level  
- Formatting can be passed directly as arguments in `plt.plot()`  

---

## 📈 Matplotlib – Multiple Lines & Legends

- Plot multiple lines in a single graph  
- Label lines for identification  
- `legend()` → displays labels on plot  
- `loc` → sets legend position (`best`, `upper right`, etc.)  
- `shadow` → adds shadow to legend  
- `fontsize` → controls legend text size  
- `grid()` → adds background grid for better readability  

---

## 📊 Matplotlib – Bar Graphs

- `plt.bar()` → creates vertical bar graph  
- `plt.barh()` → creates horizontal bar graph  
- `xticks()` → customizes x-axis labels and positions  
- `np.arange()` → generates index positions for bars  
- `width` → controls bar thickness/width  

---

## 📊 Matplotlib – Histogram

- `plt.hist()` → creates histogram for data distribution  
- `bins` → defines number/range of intervals  
- `rwidth` → controls relative bar width  
- `color` → sets histogram color  
- `histtype` → defines histogram style  
- `orientation` → sets vertical or horizontal layout  

---

## 🥧 Matplotlib – Pie Chart

- `plt.pie(values, labels=[...])` → creates pie chart with labeled slices  
- `plt.axis("equal")` → ensures the pie chart remains circular  
- `radius` → adjusts the overall size of the pie chart  

- `autopct="%0.2f%%"` → displays percentage values on slices  
  - `%0.2f` → formats value as float with 2 decimal places  
  - `%%` → displays the percentage symbol `%`  
  - Example → `12.45%`  

- `explode` → separates/highlights selected slices  
- `startangle` → rotates the starting position of the chart  

---

## 💾 Matplotlib – Saving Figures

- `plt.savefig()` → saves plot/figure as image file
- `bbox_inches="tight"` → removes extra surrounding whitespace  
- `pad_inches=1` → adds padding around saved figure  
- `transparent=True` → saves image with transparent background  

---
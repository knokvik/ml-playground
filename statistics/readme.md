# 📘 The Ultimate Handbook: Statistics & Probability for Data Science

A detailed roadmap from visualization to inferential testing.

[![Complete Statistics Course](https://img.youtube.com/vi/eF7HoC-cLRM/0.jpg)](https://www.youtube.com/watch?v=eF7HoC-cLRM)

**Source Video**: [Complete Statistics Course for Beginners | Data Science Tutorial](https://www.youtube.com/watch?v=eF7HoC-cLRM)

---

## 📊 Chapter 1: The Foundations of Data
*Before applying math, we must understand the structure of the information we hold.*

### 1.1 Data Tables and Variables
**[02:05](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=125s)**  
**Data Table**: A grid where horizontal lines are **Rows** and vertical lines are **Columns**.  
**[02:52](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=172s)** **Individuals**: The primary subject of the data (e.g., a person's Name).  
**[03:30](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=210s)** **Variables**: The characteristics of the individual (e.g., Age, Salary, Gender).  
**[03:59](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=239s)**  
- **One-Way Tables**: All variables depend on a single individual **[06:28](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=388s)**  
- **Two-Way Tables**: Data depends on two factors (e.g., "Year" and "Month" for revenue) **[19:40](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=1180s)**

### 1.2 Types of Variables
**[05:25](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=325s)**  
**Quantitative (Continuous)**: Numeric data like salary or height  
**Qualitative (Categorical)**: Data divided into groups like gender or movie genre **[05:34](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=334s)**

---

## 📈 Chapter 2: Visualizing Data
*Visualization turns raw numbers into intuitive stories.*

### 2.1 Basic Plots
**[01:50](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=110s)**  
- **Bar Graph**: Displays categorical data using a Frequency Table **[08:51](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=531s)**  
- **Pie Chart**: Shows percentage occurrence of every category **[11:02](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=662s)**  
- **Line Graph**: Identifies trends in continuous data over time **[15:23](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=923s)**  
- **Ogive**: Line graph using Cumulative Frequency **[16:34](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=994s)**

### 2.2 Advanced Visualization
**Histogram**: Groups continuous data into **Bins** (buckets) **[27:27](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=1667s)**  
**Bin Calculation**: `(Max - Min) ÷ desired number of bins`, round up **[31:05](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=1865s)**

---

## 📊 Chapter 3: Descriptive Statistics
*Descriptive stats summarize the data we have collected.*

### 3.1 Measures of Central Tendency
**[34:03](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=2043s)**  
- **Mean (\(\bar{x}\))**: "Balance point" where distances balance **[38:42](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=2322s)**  
- **Median**: Physical middle point, robust to outliers **[41:07](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=2467s)**  
- **Mode**: Most frequent value (**Bimodal** if multiple) **[42:58](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=2578s)**

### 3.2 Measures of Spread
- **Range**: `Max - Min` **[46:06](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=2766s)**  
- **IQR**: `Q3 - Q1` (middle 50% spread) **[52:43](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=3163s)**  
- **Variance (\(\sigma^2\))**: Average squared distances from mean **[01:20:22](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=4822s)**  
- **Std Dev (\(\sigma\))**: Square root of variance **[01:24:16](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=5056s)**

### 3.3 Outliers and Summaries
**Outliers**: Extreme values distorting mean **[54:25](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=3265s)**  
**Fences**: `[Q1 - 1.5×IQR]` to `[Q3 + 1.5×IQR]` **[59:31](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=3571s)**  
**Five-Number Summary**: `[Min, Q1, Median, Q3, Max]` → Box Plots **[01:04:45](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=3885s)**

---

## 📈 Chapter 4: Data Distribution and Z-Score
*Understanding data shape enables advanced analysis.*

### 4.1 Normal Distribution (Gaussian/Bell Curve)
**Symmetry**: Mean = Median = Mode **[01:29:29](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=4979s)**  
**Empirical Rule (68-95-99.7)**:  
- 68% within 1σ  
- 95% within 2σ  
- 99.7% within 3σ **[01:39:42](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=5382s)**

### 4.2 Z-Score
**Formula**: \(Z = \frac{x - \mu}{\sigma}\) **[01:47:49](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=5869s)**  
**Use**: Z-Tables give exact % above/below points **[01:50:25](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=6025s)**

---

## 🎲 Chapter 5: Probability Theory
*Measure uncertainty, link samples to populations.*

### 5.1 Event Types
- **Independent**: One doesn't affect other (coin flips) **[02:01:36](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=6096s)**  
- **Dependent**: One changes next probability (cards w/o replacement) **[02:05:12](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=6312s)**  
- **Mutually Exclusive**: Cannot happen together **[02:09:07](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=6547s)**

### 5.2 Probability Rules
- **Addition Rule**: "OR" questions (A or B) **[02:10:24](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=6624s)**  
- **Multiplication Rule**: "AND" questions (A and B) **[02:17:34](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=7054s)**  
- **Conditional**: P(A|B) **[02:20:57](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=7287s)**  
- **Bayes' Theorem**: Update probabilities with evidence **[02:38:27](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=8307s)**

---

## 🧪 Chapter 6: Inferential Statistics & Hypothesis Testing
*Core of Data Science: Population claims from samples.*

### 6.1 3-Step Process
1. **Null Hypothesis (H₀)**: "No change" **[02:53:25](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=10405s)**  
2. **Alternate Hypothesis (Hₐ)**: Claim to test  
3. **Test**: Calculate p-value **[02:54:14](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=10454s)**

### 6.2 Statistical Tests
| Test | When to Use | 
|------|-------------|
| **Z-Test** | n > 30, known σ **[03:08:34](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=11314s)** |  
| **T-Test** | Unknown σ or small n **[03:40:52](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=13252s)** |  
| **Chi-Square** | Categorical relationships **[04:15:01](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=15301s)** |  
| **ANOVA** | Compare >2 group means **[04:38:18](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=16698s)** |

---

## 🤖 Chapter 7: Machine Learning Connections

### 7.1 Covariance and Correlation
**Covariance**: Direction of relationship **[04:48:26](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=17306s)**  
**Correlation (r)**: Strength + direction **[04:53:11](https://www.youtube.com/watch?v=eF7HoC-cLRM&t=17591s)**  

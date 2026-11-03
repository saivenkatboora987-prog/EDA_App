# Micro EDA Dashboard

A Streamlit app that automates an 8-step exploratory data analysis (EDA) workflow on any uploaded CSV or Excel file, with AI-generated insights from Google Gemini.

## Problem
EDA on a new dataset means repeating the same checks every time: structure, data types, missing values, distributions, outliers. This app does them in one place without writing code.

## Dataset
Works with any user-uploaded `.csv` or `.xlsx` file. No fixed dataset is required.

## Approach
1. **Read data:** upload CSV or Excel
2. **Quick checks:** shape, size, and data preview
3. **Column types:** separates categorical and numerical columns
4. **Missing values:** detects them and fills with the mean (numerical) or "Unknown" (categorical)
5. **Categorical analysis:** value counts and bar chart
6. **Numerical analysis:** summary statistics and histogram
7. **Outlier analysis:** boxplot for any numerical column
8. **AI insights:** Gemini reads the summary statistics and missing-value counts and returns a plain-English summary, data quality issues, and suggestions for further analysis

## Results
<img width="977" height="718" alt="image" src="https://github.com/user-attachments/assets/6c961237-7d53-4b7a-a8ac-109ca1685917" />
<img width="955" height="338" alt="image" src="https://github.com/user-attachments/assets/5d714e44-3403-4fab-a70d-a7eb54b27b40" />


## How to run
```bash
git clone https://github.com/saivenkatboora987-prog/EDA_App.git
cd EDA_App
pip install streamlit pandas matplotlib openpyxl google-generativeai

# Windows
set Gemini_API_KEY=your_key_here
# Mac/Linux
export Gemini_API_KEY=your_key_here

streamlit run EDA_App.py
```

## Tech stack
Python, Streamlit, Pandas, Matplotlib, Google Gemini API

## Future improvements
- Correlation heatmap
- Duplicate row detection
- Downloadable cleaned dataset

import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from google import genai

st.set_page_config(page_title="Micro EDA Dashboard")
load_dotenv()

# Initialize Client
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("⚠️ GEMINI_API_KEY is missing! Check your .env file.")
    st.stop()
client = genai.Client(api_key=api_key)

st.title("Micro EDA Dashboard")
file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if file:
    df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)
    
    # Overview
    st.subheader("Data Overview")
    st.write(f"Shape: {df.shape} | Size: {df.size}")
    st.dataframe(df.head(3))
    
    cat, num = df.select_dtypes(include=['object', 'category']).columns.tolist(), df.select_dtypes(include=['number']).columns.tolist()
    st.write("**Categorical:**", cat, "**Numerical:**", num)

    # Missing Values
    if df.isnull().sum().sum() > 0 and st.button("Fill Missing (Mean/Mode)"):
        df = df.fillna(df.mean(numeric_only=True)).fillna("Unknown")
        st.success("Missing values filled!")

    # Charts
    st.subheader("Distributions")
    c1, c2 = st.columns(2)
    with c1:
        if cat and (c := st.selectbox("Categorical Column", cat, key="cat_sel")):
            fig, ax = plt.subplots()
            df[c].value_counts().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
            plt.xticks(rotation=45)
            st.pyplot(fig)
    with c2:
        if num and (n := st.selectbox("Numerical Column", num, key="num_sel")):
            fig, ax = plt.subplots()
            df[n].plot(kind='hist', bins=20, ax=ax, color='orange', edgecolor='black')
            st.pyplot(fig)

    # AI Summary
    st.subheader("AI-Generated Insights")
    if st.button("Generate AI Summary"):
        with st.spinner("Gemini is analyzing your data..."):
            prompt = f"Data Summary:\n{df.describe(include='all').to_string()}\n\nMissing:\n{df.isnull().sum().to_string()}\n\nGive key patterns, data quality issues, and 3 analysis suggestions."
            response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
            st.write(response.text)

    if st.button("Submit Data"):
        st.balloons()
        st.success("Successfully EDA Completed")

import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import google.generativeai as genai

import os



# Configure Gemini

genai.configure(api_key=os.environ.get("Gemini_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")



st.title("Micro EDA Dashboard")



# Step 1: Read data (CSV & XLSX)

file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])



if file:

    df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)

   

    # Step 2 & 3: Quick Checks & Column Types

    st.subheader("Step 2 & 3: Quick Checks & Column Types")

    st.write(f"Shape: {df.shape} | Size: {df.size}")

    st.dataframe(df.head())

   

    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    num_cols = df.select_dtypes(include=['number']).columns.tolist()

    st.write("**Categorical:**", cat_cols)

    st.write("**Numerical:**", num_cols)



    # Step 4: Missing Values

    st.subheader("Step 4: Missing Values")

    if df.isnull().sum().sum() > 0:

        st.write(df.isnull().sum())

        if st.button("Fill Missing (Mean/Mode)"):

            df = df.fillna(df.mean(numeric_only=True)).fillna("Unknown")

            st.success("Missing values filled!")

    else:

        st.info("No missing values found.")



    # Step 5 & 6: Categorical & Numerical Analysis

    st.subheader("Step 5 & 6: Data Distributions & Charts")

    col1, col2 = st.columns(2)

   

    with col1:

        if cat_cols:

            c = st.selectbox("Categorical Column", cat_cols)

            st.write(df[c].value_counts())

            fig, ax = plt.subplots()

            df[c].value_counts().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

            plt.xticks(rotation=45)

            st.pyplot(fig)

           

    with col2:

        if num_cols:

            n = st.selectbox("Numerical Column", num_cols)

            st.write(df[n].describe())

            fig, ax = plt.subplots()

            df[n].plot(kind='hist', bins=20, ax=ax, color='orange', edgecolor='black')

            st.pyplot(fig)



    # Step 7: Outliers (Boxplot)

    st.subheader("Step 7: Outlier Analysis")

    if num_cols:

        b_col = st.selectbox("Boxplot Column", num_cols, key="box")

        fig, ax = plt.subplots()

        ax.boxplot(df[b_col].dropna(), vert=True, patch_artist=True)

        ax.set_ylabel(b_col)

        st.pyplot(fig)

       # Step 8: AI Insights (Gemini)
    st.subheader("Step 8: AI-Generated Insights")
    if st.button("Generate AI Summary"):
        with st.spinner("Gemini is analyzing your data..."):
            summary = df.describe(include="all").to_string()
            prompt = (
                "You are a data scientist. Here are summary statistics of a dataset:\n\n"
                f"{summary}\n\n"
                f"Missing values per column:\n{df.isnull().sum().to_string()}\n\n"
                "Give a short plain-English summary: key patterns, possible data "
                "quality issues, and 3 suggestions for further analysis."
            )
            response = model.generate_content(prompt)
            st.write(response.text)

if st.button("Submit Data"):

    # Perform some action here

    st.balloons()

    st.success("Successfully EDA Completed")import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import google.generativeai as genai

import os



# Configure Gemini

genai.configure(api_key=os.environ.get("Gemini_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")



st.title("Micro EDA Dashboard")



# Step 1: Read data (CSV & XLSX)

file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])



if file:

    df = pd.read_csv(file) if file.name.endswith('.csv') else pd.read_excel(file)

   

    # Step 2 & 3: Quick Checks & Column Types

    st.subheader("Step 2 & 3: Quick Checks & Column Types")

    st.write(f"Shape: {df.shape} | Size: {df.size}")

    st.dataframe(df.head())

   

    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    num_cols = df.select_dtypes(include=['number']).columns.tolist()

    st.write("**Categorical:**", cat_cols)

    st.write("**Numerical:**", num_cols)



    # Step 4: Missing Values

    st.subheader("Step 4: Missing Values")

    if df.isnull().sum().sum() > 0:

        st.write(df.isnull().sum())

        if st.button("Fill Missing (Mean/Mode)"):

            df = df.fillna(df.mean(numeric_only=True)).fillna("Unknown")

            st.success("Missing values filled!")

    else:

        st.info("No missing values found.")



    # Step 5 & 6: Categorical & Numerical Analysis

    st.subheader("Step 5 & 6: Data Distributions & Charts")

    col1, col2 = st.columns(2)

   

    with col1:

        if cat_cols:

            c = st.selectbox("Categorical Column", cat_cols)

            st.write(df[c].value_counts())

            fig, ax = plt.subplots()

            df[c].value_counts().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')

            plt.xticks(rotation=45)

            st.pyplot(fig)

           

    with col2:

        if num_cols:

            n = st.selectbox("Numerical Column", num_cols)

            st.write(df[n].describe())

            fig, ax = plt.subplots()

            df[n].plot(kind='hist', bins=20, ax=ax, color='orange', edgecolor='black')

            st.pyplot(fig)



    # Step 7: Outliers (Boxplot)

    st.subheader("Step 7: Outlier Analysis")

    if num_cols:

        b_col = st.selectbox("Boxplot Column", num_cols, key="box")

        fig, ax = plt.subplots()

        ax.boxplot(df[b_col].dropna(), vert=True, patch_artist=True)

        ax.set_ylabel(b_col)

        st.pyplot(fig)



if st.button("Submit Data"):

    # Perform some action here

    st.balloons()

    st.success("Successfully EDA Completed")

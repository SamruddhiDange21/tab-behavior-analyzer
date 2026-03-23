import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Tab Behavior Analyzer")

st.write("Analyze your browsing habits and productivity.")

# Load data
df = pd.read_csv("data.csv")

st.subheader("Raw Data")
st.dataframe(df)

# Total time
total_time = df["time_spent_minutes"].sum()
st.metric("Total Time Spent (minutes)", total_time)

# Time per website
st.subheader("Time Spent per Website")
site_time = df.groupby("url")["time_spent_minutes"].sum()
st.bar_chart(site_time)

# Category analysis
st.subheader("Productive vs Distraction")

category_time = df.groupby("category")["time_spent_minutes"].sum()

fig, ax = plt.subplots()
ax.pie(category_time, labels=category_time.index, autopct='%1.1f%%')
st.pyplot(fig)

# Insight
productive_time = category_time.get("productive", 0)
distraction_time = category_time.get("distraction", 0)

if distraction_time > productive_time:
    st.warning("⚠️ You are spending more time on distractions.")
else:
    st.success("✅ Good job! You're more productive than distracted.")
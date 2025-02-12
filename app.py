import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Title
st.title("📊 Risk Assessment Matrix Generator")

# Upload CSV
uploaded_file = st.file_uploader("Upload your risk CSV file", type="csv")

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("### 📋 Risk Data", data)

    # Generate Heatmap
    heatmap_data = pd.crosstab(data['Impact'], data['Probability'])

    st.write("### 🔥 Risk Assessment Matrix")
    plt.figure(figsize=(8, 6))
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd', linewidths=0.5)
    plt.xlabel('Probability (1 - Low, 5 - High)')
    plt.ylabel('Impact (1 - Low, 5 - High)')
    st.pyplot(plt)

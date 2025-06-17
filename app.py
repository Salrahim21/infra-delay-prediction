import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---- Sidebar ----
st.sidebar.title("📊 Infra Delay ML Dashboard")
st.sidebar.markdown("Predicting High-Rise Construction Duration")

# ---- Title ----
st.title("🏗️ Infrastructure Delay Prediction")
st.markdown("This dashboard compares different ML models trained on global high-rise building data.")

# ---- Model Results ----
st.header("🔍 Model Evaluation Metrics")

# Define model results
results = {
    'Model': ['Random Forest', 'Linear Regression', 'XGBoost'],
    'MAE': [0.0613, 2.3943, 0.0447],
    'RMSE': [0.4229, 3.4031, 0.3466],
    'R² Score': [0.9977, 0.8524, 0.9985]
}

df_results = pd.DataFrame(results)

# Display table
st.dataframe(df_results.set_index('Model').style.format("{:.4f}"))

# ---- Visualization ----
st.subheader("📈 Metric Comparison")

metric = st.selectbox("Select a metric to compare", ['MAE', 'RMSE', 'R² Score'])

fig, ax = plt.subplots()
ax.bar(df_results['Model'], df_results[metric], color='skyblue')
ax.set_title(f"{metric} Comparison")
ax.set_ylabel(metric)
st.pyplot(fig)

# ---- Footer ----
st.markdown("---")
st.markdown("Crafted by [Ibrahim Salim] · Civil Engineering Meets Machine Learning")


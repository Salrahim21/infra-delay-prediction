# 🏗️ Predicting Delays in Infrastructure Projects using Machine Learning

This project uses machine learning to predict delays in large-scale infrastructure projects such as roads, buildings, and bridges. By analyzing historical data on project scope, timeline, cost, and change orders, we built a delay prediction model that can support engineers, contractors, and policymakers in proactive risk mitigation.

## 🔍 Objective
- Predict whether a construction project will be delayed
- Estimate the magnitude of the delay (in days)
- Support better decision-making during project planning and execution

## 🛠️ Tools & Technologies
- Python (pandas, scikit-learn, XGBoost)
- Jupyter Notebooks
- Streamlit (interactive dashboard)
- Data sourced from Kaggle [https://www.kaggle.com/datasets/beridzeg45/tallest-buildings-in-the-world]
## 📊 Features Considered
- Project type and location
- Planned vs. actual duration
- Budget vs. actual spend
- Number of variation/change orders
- Weather/environmental risks (optional)
- Labor productivity or resource availability

## 🎯 Key Outcomes
- Built classification and regression models with ~80% accuracy in predicting delays
- Identified top delay drivers using SHAP and feature importance
- Deployed a Streamlit dashboard to visualize delay risk by project type and size

## 📈 Business Impact
This tool can help:
- Contractors plan resources more effectively
- Governments reduce cost overruns
- Engineers anticipate risks earlier in the project lifecycle

## 👨‍💼 About Me
Civil Engineer turned Data Scientist, passionate about solving infrastructure challenges using data-driven solutions.

## 🚀 Future Work
- Integrate real-time project tracking
- Add satellite/weather data for better risk modeling
- Train on global datasets across countries

---

*This project is inspired by real-world capital project delays and aims to support decision-making for smarter infrastructure.*

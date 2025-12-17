
import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('best_model_for_customer_purchase.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title("Customer Purchase Behavior Prediction")
st.write("This application predicts whether a customer is a **High Spender** or **Low Spender** "
    "based on their purchase behavior.")

age = st.number_input("Age", min_value=18, max_value=80, value=21,step=1)
income = st.number_input("Income", min_value=0, value=50000,step=5000)
region = st.selectbox("Region", ["North", "South", "East", "West"])
satisfaction_score = st.number_input("Satisfaction Score", min_value=0, max_value=10, value=5)
promo_usage = st.number_input("Promo Usage", min_value=0, value=0)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education", ["HighSchool", "Masters", "College"])
loyalty = st.selectbox("Loyalty Status", ["Regular", "Silver", "Gold"])
purchase_freq = st.selectbox("Purchase Frequency", ["rare", "occasional", "frequent"])
product_category = st.selectbox(
    "Product Category",
    ["Books", "Clothing", "Electronics", "Food", "Health", "Home"]
)

if st.button('Predict Customer Type'):
  data = pd.DataFrame(0, index=[0], columns=model_columns)
  data['age'] = age
  data['income'] = income
  data["promotion_usage"] = promo_usage
  data["satisfaction_score"] = satisfaction_score

  # One-hot encoding manually
  data[f"gender_{gender}"] = 1
  data[f"education_{education}"] = 1
  data[f"region_{region}"] = 1
  data[f"loyalty_status_{loyalty}"] = 1
  data[f"purchase_frequency_{purchase_freq}"] = 1
  data[f"product_category_{product_category}"] = 1

  prediction = model.predict(data)

  if prediction[0] == 1:
    st.success("High Spender Customer")
  else:
    st.warning("Low Spender Customer")

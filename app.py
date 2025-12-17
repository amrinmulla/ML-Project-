
import streamlit as st
import joblib
import numpy as np
import pandas as pd

model = joblib.load('best_model_for_customer_purchase.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title("Customer Purchase Behavior Prediction")
st.write("This application predicts whether a customer is a **High Spender** or **Low Spender** "
    "based on their purchase behavior.")

age = st.number_input("Age",min_value=18,max_value=80,value=30,step=1,
    help="Age helps identify spending patterns at different life stages."
)

income = st.number_input("Annual Income",min_value=0,value=50000,
    help="Income represents purchasing power. Higher income usually increases spending potential."
)

region = st.selectbox("Region",["North", "South", "East", "West"],
    help="Region captures geographical differences in customer buying behavior."
)

satisfaction_score = st.number_input("Satisfaction Score",min_value=0,max_value=10,value=5,
    help="Customer satisfaction indicates likelihood of repeat purchases and higher spending."
)

promo_usage = st.number_input("Promotion Usage (%)",min_value=0,max_value=100,value=20,
    help="Shows how often the customer uses discounts or promotional offers."
)

gender = st.selectbox("Gender",["Male", "Female"],
    help="Gender is a demographic factor that may influence purchasing preferences."
)

education = st.selectbox("Education Level",["HighSchool", "College", "Bachelor", "Masters"],
    help="Education level may impact income level and purchasing decisions."
)

loyalty = st.selectbox("Loyalty Status",["Regular", "Silver", "Gold"],
    help="Loyalty status reflects customer engagement. Higher loyalty often leads to higher spending."
)

purchase_freq = st.selectbox("Purchase Frequency",["rare", "occasional", "frequent"],
    help="Indicates how often the customer makes purchases."
)

product_category = st.selectbox("Preferred Product Category",["Beauty","Books", "Clothing", "Electronics", "Food", "Health", "Home"],
    help="Primary category purchased by the customer, influencing spending behavior."
)

if st.button('Predict Customer Type'):
  data = pd.DataFrame(0, index=[0], columns=model_columns)
  data['age'] = age
  data['income'] = income
  data["promotion_usage"] = promo_usage
  data["satisfaction_score"] = satisfaction_score

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


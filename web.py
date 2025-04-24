import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Mock encoders (replace with your actual encodings)
housing_map = {'own': 0, 'for free': 1, 'rent': 2}
saving_accounts_map = {'little': 0, 'moderate': 1, 'quite rich': 2, 'rich': 3}
checking_account_map = {'little': 0, 'moderate': 1, 'rich': 2}
purpose_map = {'radio/TV': 280 , 'education': 59 ,'furniture/equipment': 181, 'car': 337, 'business': 97, 'domestic appliances': 12,  'repairs': 22, 'vacation/others' : 12}
sex_map = {'F':1,'M':0}
job_map = {'unskilled and non-resident': 0,'unskilled and resident': 1,'skilled': 2, 'highly skilled': 3}
# Streamlit app
st.title('Credit Risk Prediction')

# Input fields
age = st.number_input("Age", min_value=18, max_value=100)
job = st.selectbox("Job", options=list(job_map.keys()))
housing = st.selectbox("Housing", options=list(housing_map.keys()))
saving_accounts = st.selectbox("Saving Accounts", options=list(saving_accounts_map.keys()))
checking_account = st.selectbox("Checking Account", options=list(checking_account_map.keys()))
credit_amount = st.number_input("Credit Amount", min_value=100, max_value=500000)
duration = st.number_input("Duration (Months)", min_value=1, max_value=120)
purpose = st.selectbox("Purpose", options=list(purpose_map.keys()))  # ✅ This defines `purpose`
sex = st.selectbox("Sex", options=list(sex_map.keys()))  # ✅ This was the line that caused earlier issue

# Preprocess input
input_data = [
    age,
    job_map[job],
    housing_map[housing],
    saving_accounts_map[saving_accounts],
    checking_account_map[checking_account],
    credit_amount,
    duration,
    purpose_map[purpose],
    sex_map[sex]
]

# Prediction
if st.button("Predict"):
    prediction = model.predict([input_data])[0]
    st.success(f"Prediction: {'Good Credit' if prediction == 1 else 'Bad Credit'}")

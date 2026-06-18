import streamlit as st
import pickle 

st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🏥"
) 

st.markdown(
    "<h1 style='text-align:center;color:blue;'>🏥 Disease Prediction System</h1>",
    unsafe_allow_html=True
) 

st.subheader("🤒 Select Symptoms")

# Load Saved Model
model = pickle.load(open("/model.pkl", "rb"))

st.title("Disease Prediction System")

fever = st.checkbox("🤒 Fever")
cough = st.checkbox("😷 Cough")
headache = st.checkbox("🤕 Headache")
fatigue = st.checkbox("😴 Fatigue")

if st.button("🔍 Predict Disease"): 

    result = model.predict([[
        int(fever),
        int(cough),
        int(headache),
        int(fatigue)
    ]])  

    st.success(f"Predicted Disease: {result[0]}") 
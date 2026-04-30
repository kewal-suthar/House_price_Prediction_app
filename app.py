import streamlit as st
import pickle

reg=pickle.load(open("house_pred.pkl","rb"))

st.title("House Price Presdiction App")

area=st.number_input("Input Area in square feet",min_value=100)
bed=st.selectbox("Select bedrooms",options=[1,2,3,4,5,6])
location_score=st.number_input("Input location score",min_value=1.0)
bath_room=st.slider("Input number of bathrooms",1,4)
age=st.slider("Input age of the house",0,50)


if st.button("Predict Price"):
    input_data=[[area,bed,location_score,bath_room,age]]
    pred_price=reg.predict(input_data)
    st.success(f"The Estimated price for this house is: ${pred_price[0]}")
    
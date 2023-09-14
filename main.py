import pandas as pd 
import numpy as np
import pickle 
import streamlit as st 

pickle_in = open('house_price_prediction.pkl', 'rb')
model = pickle.load(pickle_in,encoding='latin1')

def prediction(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,sqft_lot15):
    if waterfront== "No":
        waterfront = 0
    else:
        waterfront = 1

    if condition == "Bad":
        condition = 0
    elif condition == "Average":
        condition = 1
    elif condition == "Good":
        condition = 2
    elif condition == "Very Good":
        condition == 3
    else: 
        condition == 4

    bedrooms = bedrooms
    bathrooms = bathrooms
    sqft_living = sqft_living
    sqft_lot = sqft_lot
    floors = floors
    view =view
    grade =grade
    sqft_above= sqft_above
    sqft_basement= sqft_basement
    yr_built= yr_built
    yr_renovated =yr_renovated
    zipcode= zipcode
    lat=lat
    long=long
    sqft_living15=sqft_living15
    sqft_lot15=sqft_lot15

    

    prediction = model.predict([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,sqft_lot15]])
    return prediction

def main():

    html_temp =  """ 
        <div style ="background-color:green;padding:15px"> 
        <h1 style ="color:black;text-align:center;">Automatic Loan Eligibility Prediction System</h1> 
        </div> 
        
        """
    
    st.markdown(html_temp, unsafe_allow_html= True)

  
    bedrooms = st.number_input("Number Of Bedrooms")
    bathrooms = st.number_input("Number Of Bathrooms")
    sqft_living=st.number_input("Total living space(Sqft)")
    sqft_lot=st.number_input("Total area of house (Sqft)")
    floors=st.number_input("Number Of Floors")
    waterfront=st.selectbox('Does it have waterfront', ('No', 'Yes'))
    view=st.number_input("Number Of Views")
    condition=st.selectbox('Whats its condition', ('Bad','Average', 'Good', 'Very Good', 'Perfect'))
    grade=st.number_input("Grade of house (On a scale of 1 to 10)")
    sqft_above=st.number_input("Ground floor space (Sqft)")
    sqft_basement=st.number_input("Basement floor space (Sqft)")
    yr_built=st.number_input("Year House was built")
    yr_renovated=st.number_input("Year which House was renovated (if not then '0')")
    zipcode=st.number_input("Zipcode")
    lat=st.number_input("Latitude")
    long=st.number_input("Longitude")
    sqft_living15=st.number_input("Total living space in the year 2015 (Sqft)")
    sqft_lot15=st.number_input("Total area of house in the year 2015 (Sqft)")
    result = ''
    if st.button("Predict"):
        result = prediction(bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,grade,sqft_above,sqft_basement,yr_built,yr_renovated,zipcode,lat,long,sqft_living15,sqft_lot15)
        st.success("Your House Price Would Be{}".format(result))

if __name__ == '__main__':
    main()


import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Title
def price_predictor_ui():
    st.markdown("""<h2 style='text-align: center; color: #4B8BBE;'> Let's Predict Price</h2> """, unsafe_allow_html=True)

    # read df.pkl and pipeline.pkl with error handling
    try:
        with open('df.pkl', 'rb') as file:
            df = pickle.load(file)
        with open('pipeline.pkl', 'rb') as file:
            pipeline = pickle.load(file)
    except Exception as e:
        st.error(f"Error loading model or data: {e}")
        return


    st.header('Enter your choices')

    # property_type input 
    property_type = st.selectbox('Property Type', ['flat', 'house'])

    # sector input 
    sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))

    bedrooms = float(st.selectbox('No. of Bedrooms', sorted(df['bedRoom'].unique().tolist())))

    bathrooms = float(st.selectbox('No. of Bathrooms', sorted(df['bathroom'].unique().tolist())))

    balconis = st.selectbox('No. of Balconies', sorted(df['balcony'].unique().tolist()))

    property_age = st.selectbox('Property age', sorted(df['agePossession'].unique().tolist()))

    built_up_area = float(st.number_input('Built Up Area'))

    servant_room = float(st.selectbox('Servant room',[0.0, 1.0]))

    store_room = float(st.selectbox('Store room',[0.0, 1.0]))

    furnishing_type = st.selectbox('Furnishing type', sorted(df['furnishing_type'].unique().tolist()))

    luxury_category = st.selectbox('Luxury category', sorted(df['luxury_category'].unique().tolist()))

    floor_category = st.selectbox('Floor category', sorted(df['floor_category'].unique().tolist()))


    if st.button('Predict'):

        # from a dataframe 
        data = [[property_type, sector, bedrooms, bathrooms, balconis, property_age, built_up_area, servant_room, store_room, furnishing_type, luxury_category, floor_category]]
        columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
            'agePossession', 'built_up_area', 'servant room', 'store room',
            'furnishing_type', 'luxury_category', 'floor_category']

        one_df = pd.DataFrame(data, columns = columns)

        # predict 
        base_price = np.expm1(pipeline.predict(one_df))[0]
        low = base_price - 0.22
        high = base_price + 0.22

        # display 
        #st.text(f"Price of a flat between ({low:.2f}) Cr to ({high:.2f}) Cr")
        st.markdown(f"""
        <div style='
            text-align: center;
            padding: 20px;
            background-color: #f0f2f6;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 20px;
        '>
            <h3 style='color: #4B8BBE;'>💰 Estimated Property Price Range</h3>
            <h2 style='color: #222;'>₹ {low:.2f} Cr &nbsp; - &nbsp; ₹ {high:.2f} Cr</h2>
        </div>
    """, unsafe_allow_html=True)

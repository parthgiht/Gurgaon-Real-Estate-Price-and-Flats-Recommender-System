import streamlit as st
import pandas as pd
import plotly.express as px
import pickle 
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

# Title 
def analytics_ui():
    st.markdown("""<h2 style='text-align: center; color: #4B8BBE;'> Let's Visualize Property</h2> """, unsafe_allow_html=True)

    # Dataset load with error handling
    try:
        new_df = pd.read_csv('Datasets/data_viz1.csv')
        feature_text = pickle.load(open('Datasets/feature_text.pkl', 'rb'))
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return

    # Convert necessary columns to numeric, coercing errors
    numeric_columns = ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
    for col in numeric_columns:
        new_df[col] = pd.to_numeric(new_df[col], errors='coerce')


    # GeoMAP

    # Header - 1
    st.subheader("📍Price per sqft Geomap")

    # Group by sector and take mean of numeric values
    group_df = new_df.groupby('sector')[numeric_columns].mean()


    fig = px.scatter_mapbox(group_df, lat = "latitude", lon = "longitude", color = 'price_per_sqft', 
                            size = 'built_up_area', color_continuous_scale = px.colors.sequential.Plasma,
                            zoom = 10, mapbox_style = "carto-positron", width = 1200, height = 600,
                            hover_name = group_df.index)

    st.plotly_chart(fig, use_container_width = True)



    #------------------------------------------
    # Word cloud
    #------------------------------------------

    st.subheader("🔤 Features Word Cloud")

    # sector dropdown
    sector_options = sorted(new_df['sector'].dropna().unique())
    selected_sector = st.selectbox("Select a sector", sector_options)


    # Creating Wordcloud 
    wordcloud = WordCloud(width = 600, height = 600, 
                        background_color ='white', 
                        stopwords = set(['s']),  # Any stopwords you'd like to exclude
                        min_font_size = 10).generate(feature_text)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(fig)



    #--------------------------------------
    # Area vs Price Scatter plot 
    #---------------------------------------

    st.subheader("📈 Area vs Price by Bedroom Count")

    property_type = st.selectbox("Select property type", ['flat','house'])

    if property_type == 'house':
        fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom")
        st.plotly_chart(fig1, use_container_width=True)
    else:
        fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom")
        st.plotly_chart(fig1, use_container_width=True)



    #--------------------------------------
    # BHK Pie chart
    #--------------------------------------
    st.subheader("🏘️ BHK Distribution")

    # Dropdown 
    sector_options1 = new_df['sector'].unique().tolist()
    sector_options1.insert(0, 'All Sectors')


    selected_sector1 = st.selectbox("Select sector", sector_options1)

    if selected_sector1 == 'All Sectors':
        fig2 = px.pie(new_df, names='bedRoom')
        st.plotly_chart(fig2, use_container_width=True)
    else:
        fig2 = px.pie(new_df[new_df['sector'] == selected_sector1], names='bedRoom')
        st.plotly_chart(fig2, use_container_width=True) 



    #--------------------------------------
    # Box plot of BHK price
    #--------------------------------------
    # Heading 
    st.subheader("₹ Price Range by BHK")

    fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price')
    st.plotly_chart(fig3, use_container_width=True)



    #-------------------------------------------
    # Price Distribution by KDE
    #--------------------------------------------
    # Heading 
    st.subheader("📊 Price Distribution: House vs Flat")

    fig4, ax = plt.subplots(figsize=(8, 5))

    sns.kdeplot(new_df[new_df['property_type'] == 'house']['price'], ax=ax, fill = True, label='House')
    sns.kdeplot(new_df[new_df['property_type'] == 'flat']['price'], ax=ax, fill = True, label='Flat')

    ax.set_xlabel("Price")
    ax.set_ylabel("Density")
    ax.legend()
    st.pyplot(fig4)
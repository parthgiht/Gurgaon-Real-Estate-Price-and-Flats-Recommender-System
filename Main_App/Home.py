import streamlit as st
from Pages.Price_Predictor import price_predictor_ui
from Pages.Analytics_Module import analytics_ui
from Pages.Recommend_Appartments import recommend_ui


# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Gurgaon Real Estate Recommendation App",
    page_icon="🏡",
    layout="wide"
)


# Sidebar Navigation (simple radio)
st.sidebar.title("🏠 Navigation")
page = st.sidebar.radio("Go to", ["Home", "Price Predictor", "Visual Analytics", "Apartment Recommender"])

if page == "Home":
    # Home Page
    # ------------------------------
    st.markdown("""
        <div style='text-align: center; padding-top: 10px;'>
            <h1 style='color: #4B8BBE;'>🏗️ Gurgaon Real Estate Recommendation App</h1>
            <h3 style='color: #262730;'>Unlock property insights, price predictions, and personalized recommendations</h3>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Three Feature Cards
    st.markdown("## 🔍 Explore Key Features")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("https://img.icons8.com/color/96/rupee.png", width=70)
        st.markdown("### Price Predictor")
        st.write("""
        • Predict property prices based on location, BHK, area, etc.  
        • Know expected pricing with confidence range.  
        • Useful for buyers, sellers & investors.
        """)

    with col2:
        st.image("https://img.icons8.com/color/96/combo-chart.png", width=70)
        st.markdown("### Visual Analytics")
        st.write("""
        • Interactive dashboard with real estate insights.  
        • Area vs price, BHK distribution, word clouds & more.  
        • Ideal for market researchers & curious users.
        """)

    with col3:
        st.image("https://img.icons8.com/color/96/apartment.png", width=70)
        st.markdown("### Apartment Recommender")
        st.write("""
        • Get similar property recommendations.  
        • Filter apartments by radius from location.  
        • Perfect for personalized apartment discovery.
        """)

    st.markdown("---")

    st.markdown("""
        <div style='text-align: center; padding-top: 20px;'>
            <h3 style='color: #4B8BBE;'>Ready to explore Gurgaon real estate?</h3>
            <p style='font-size: 18px;'>Use the sidebar to navigate between modules</p>
        </div>
    """, unsafe_allow_html=True)

    st.image("https://images.unsplash.com/photo-1600585154340-be6161a56a0c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80", 
             caption="Smart homes. Smarter insights.", use_container_width=True)

    st.markdown("""
        <div style='text-align: center; font-size: 14px; color: grey;'>
            Developed by <strong>Parth Patel</strong> | Powered by <strong>Python & Streamlit</strong> <br>
            <em>Last updated: July 2025</em>
        </div>
    """, unsafe_allow_html=True)

elif page == "Price Predictor":
    price_predictor_ui()

elif page == "Visual Analytics":
    analytics_ui()

elif page == "Apartment Recommender":
    recommend_ui()


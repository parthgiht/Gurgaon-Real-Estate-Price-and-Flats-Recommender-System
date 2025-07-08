import streamlit as st
import pandas as pd
import pickle
import numpy as np

# Title
def recommend_ui():
    st.markdown("""<h2 style='text-align: center; color: #4B8BBE;'> Let's Find Apartments</h2> """, unsafe_allow_html=True)

    # Pickle file read binary with error handling
    try:
        location_df = pickle.load(open('Datasets/location_distance.pkl', 'rb'))
        cosine_sim1 = pickle.load(open('Datasets/cosine_sim1.pkl', 'rb'))
        cosine_sim2 = pickle.load(open('Datasets/cosine_sim2.pkl', 'rb'))
        cosine_sim3 = pickle.load(open('Datasets/cosine_sim3.pkl', 'rb'))
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return



    def recommend_properties_with_scores(property_name, top_n = 247):

        cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
        
        # Get the similarity scores for the property using its name as the index
        sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

        # Sort properties based on the similarity scores
        sorted_scores = sorted(sim_scores, key = lambda x: x[1], reverse = True)

        # Get the indices and scores of thee top_n most similar properties 
        top_indices = [i[0] for i in sorted_scores[1: top_n + 1]]
        top_scores = [i[1] for i in sorted_scores[1: top_n + 1]]

        # Retrieve the names of the top properties using the indices 
        top_properties = location_df.index[top_indices].tolist()

        # Create a dataframe with the result 
        recommendations_df = pd.DataFrame({
            'PropertyName' : top_properties,
            'SimilarityScore' : top_scores
        })

        return recommendations_df



    # Heading 
    st.subheader("📍 Select location and radius")

    # Creating columns for layout
    col1, col2 = st.columns([3, 2])

    # Dropdown 
    with col1:
        selected_location = st.selectbox("Location", sorted(location_df.columns.to_list()))

    # Radius (area under particular location)
    with col2:
        radius = st.number_input("Radius (in km)", min_value=1.0, step=0.5)


    # ------ Filter and Display Results -------

    if st.button('Search'):
        result_ser = location_df[location_df[selected_location] < radius *1000][selected_location].sort_values()

        if not result_ser.empty:
            st.markdown(f"<h5 style='color: #4B8BBE;'>📌 Locations within {radius:.1f} km of {selected_location}:</h5>", unsafe_allow_html=True)

            for key, value in result_ser.items():
                st.markdown(f"""
                    <div style='
                        padding: 8px;
                        background-color: #f9f9f9;
                        margin-bottom: 6px;
                        border-radius: 5px;
                        font-size: 15px;
                        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
                    '>
                        🏙️ <strong>{key}</strong> — <span style='color: #4B8BBE;'>{round(value/1000)} km</span> away
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.info("No locations found within the selected radius.")
            



    # Appartment Recommendation Section
    st.subheader("🏢 Appartments")
    selected_appartment = st.selectbox("Select appartment", sorted(location_df.index.to_list()))
        
    if st.button('Recommend'):
        recommendation_df = recommend_properties_with_scores(selected_appartment).head()

        if not recommendation_df.empty:
            st.markdown("<h4 style='text-align: center; color: #4B8BBE;'> Top 5 Recommended Apartments</h4>", unsafe_allow_html=True)
            
            st.markdown(
                recommendation_df
                .style
                .hide(axis='index')
                .format({'SimilarityScore': '{:.2f}'})
                .set_properties(**{
                    'text-align': 'center',
                    'background-color': '#f9f9f9',
                    'border': '1px solid #ddd',
                    'padding': '10px',
                })
                .set_table_styles([
                    {'selector': 'th', 'props': [('background-color', '#4B8BBE'), ('color', 'white'), ('text-align', 'center')]},
                    {'selector': 'td', 'props': [('text-align', 'center')]}
                ])
                .to_html(),
                unsafe_allow_html=True
            )

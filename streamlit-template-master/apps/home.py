import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    #st.markdown(
    #    """
    #A [streamlit](https://streamlit.io) app template for geospatial applications based on [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu). 
    #To create a direct link to a pre-selected menu, add `?page=<app name>` to the URL, e.g., `?page=upload`.
    #https://share.streamlit.io/giswqs/streamlit-template?page=upload
    #"""
    #)

    #m = leafmap.Map(locate_control=True)
    #m.add_basemap("ROADMAP")
    #m.to_streamlit(height=700)

    # embed streamlit docs in a streamlit app
    st.markdown(“https://app.powerbi.com/view?r=eyJrIjoiOGVhNTA1YmMtY2VhYy00Nzk4LTk3NzQtYzI4OTA5OTczNDEzIiwidCI6IjBlMGRiMmFkLWM0MTYtNDdjNy04OGVjLWNlYWM0ZWU3Njc2NyIsImMiOjEwfQ%3D%3D&pageName=ReportSection0f765a7eda61c7c2a3c8”, unsafe_allow_html=True)
    

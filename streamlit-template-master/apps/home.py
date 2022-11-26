import streamlit as st
import leafmap.foliumap as leafmap
import streamlit.components.v1 as components


def app():
    st.title("Home")

   
    # embed streamlit docs in a streamlit app
    st.markdown(“https://app.powerbi.com/view?r=eyJrIjoiOGVhNTA1YmMtY2VhYy00Nzk4LTk3NzQtYzI4OTA5OTczNDEzIiwidCI6IjBlMGRiMmFkLWM0MTYtNDdjNy04OGVjLWNlYWM0ZWU3Njc2NyIsImMiOjEwfQ%3D%3D&pageName=ReportSection0f765a7eda61c7c2a3c8”, unsafe_allow_html=True)
    
    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)

    

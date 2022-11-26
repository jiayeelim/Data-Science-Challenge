import streamlit as st
import leafmap.foliumap as leafmap


def app():
    st.title("Home")

    st.markdown(
        """
    A [streamlit](https://streamlit.io) app template for geospatial applications based on [streamlit-option-menu](https://github.com/victoryhb/streamlit-option-menu). 
    To create a direct link to a pre-selected menu, add `?page=<app name>` to the URL, e.g., `?page=upload`.
    https://share.streamlit.io/giswqs/streamlit-template?page=upload

    """
    )

    m = leafmap.Map(locate_control=True)
    m.add_basemap("ROADMAP")
    m.to_streamlit(height=700)
    
    st.components.v1.html(https://app.powerbi.com/links/yJVtxNDlzY?ctid=0e0db2ad-c416-47c7-88ec-ceac4ee76767&pbi_source=linkShare)

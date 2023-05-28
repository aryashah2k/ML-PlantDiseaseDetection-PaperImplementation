from pages import app1, app2
import streamlit as st
# Page Settings
favicon = "images/favicon.ico"
st.set_page_config(page_title="Plant Leaf Disease Classification", page_icon=favicon)

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

PAGES = {
    "Model Demo": app2,
    "About The Project": app1
}

st.sidebar.title('Plant Leaf Disease Detection')
selection = st.sidebar.radio("Navigate To", list(PAGES.keys()))
page = PAGES[selection]
page.app()
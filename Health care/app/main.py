import streamlit as st
from home import display_home
from ai_assistant import display_ai_assistant
from report_analyzer import display_report_analyzer
from diagnose import display_diagnose
from about import display_about

# Set up page configuration
st.set_page_config(
    page_title="Ai Healthcare assistant",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={'About': "Gopinath creation"})

# Set title 
st.markdown('''<h1 style='font-family: "Arial"; color: #2196F3;'>AI Healthcare assistant 🩺 </h1>''',unsafe_allow_html=True)

# Set up columns for navigation
col1, col2, col3, col4, col5 = st.columns(5)

# Navigation buttons
with col1:
    if st.button("**Home**",use_container_width=True):
        st.session_state.page = "Home"

with col2:
    if st.button("**AI Assistant**",use_container_width=True):
        st.session_state.page = "AI Assistant"

with col3:
    if st.button("**Report Analyzer**",use_container_width=True):
        st.session_state.page = "Report Analyzer"

with col4:
    if st.button("**Diagnoser**",use_container_width=True):
        st.session_state.page = "Diagnoser"

with col5:
    if st.button("**About**",use_container_width=True):
        st.session_state.page = "About"

# Default to Home page
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Render content based on selected page
if st.session_state.page == "Home":
    display_home()
elif st.session_state.page == "AI Assistant":
    display_ai_assistant()
elif st.session_state.page == "Report Analyzer":
    display_report_analyzer()
elif st.session_state.page == "Diagnoser":
    display_diagnose()
elif st.session_state.page == "About":
    display_about()

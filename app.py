from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import home, plans, test_image

st.set_page_config(layout="wide")

# Header for the application
st.header("Bienvenido a FaceAi")

# Importing CSS for styling
st.markdown('<style>' + open('./styles.css').read() + '</style>', unsafe_allow_html=True)

# Define tab names and corresponding icons
tab_names = ['Inicio', 'Planes', 'Testea tu imagen']
icons = ['home', 'money', 'dashboard']

# Initialize the selected tab in session state if it's not already set
if 'selected_tab' not in st.session_state:
    st.session_state.selected_tab = "Inicio"

# Sidebar with dynamic tabs
with st.sidebar:
    # Use session state to keep track of the selected tab
    st.session_state.selected_tab = on_hover_tabs(tabName=tab_names, 
                                                  iconName=icons,
                                                  styles = {'navtab': {'background-color':'#111',
                                                                       'color': '#818181',
                                                                       'font-size': '18px',
                                                                       'transition': '.3s',
                                                                       'white-space': 'nowrap',
                                                                       'text-transform': 'uppercase'},
                                                            'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                                                  'cursor': 'pointer'}},
                                                            'iconStyle':{'position':'fixed',
                                                                         'left':'7.5px',
                                                                         'text-align': 'left'},
                                                            'tabStyle' : {'list-style-type': 'none',
                                                                          'margin-bottom': '30px',
                                                                          'padding-left': '30px'}},
                                                  key="1")

# Display different content based on selected tab
if st.session_state.selected_tab == "Inicio":
    home.show()
elif st.session_state.selected_tab == "Planes":
    plans.show()
elif st.session_state.selected_tab == "Testea tu imagen":
    test_image.show()

from st_on_hover_tabs import on_hover_tabs
import streamlit as st
import home, plans, test_image

st.set_page_config(layout="wide")

# Header for the application
st.header("Custom tab component for on-hover navigation bar")

# Importing CSS for styling
st.markdown('<style>' + open('./styles.css').read() + '</style>', unsafe_allow_html=True)

# Define tab names and corresponding icons
tab_names = ['Inicio', 'Planes', 'Testea tu imagen']
icons = ['home', 'money', 'dashboard']

# Sidebar with dynamic tabs
with st.sidebar:
    selected_tab = on_hover_tabs(tabName=tab_names, 
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
if selected_tab == "Inicio":
    home.show()
elif selected_tab == "Planes":
    plans.show()
elif selected_tab == "Testea tu imagen":
    test_image.show()

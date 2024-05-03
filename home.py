import streamlit as st

def show():
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    
    images = [
        './imagenes/imagen1.jpg',   
        './imagenes/imagen2.jpg',
        './imagenes/imagen3.jpg'
    ]

    image_index = st.slider('Browse images', 0, len(images) - 1, 0)

    st.image(images[image_index], use_column_width=True)

show()

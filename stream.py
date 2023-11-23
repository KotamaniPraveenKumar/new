import streamlit as st

def process_name(name):
    """Do something with the name"""
    st.write(f"Hi {name} welcome !")


def main():
    st.title("SIMPLE API")
    name = st.text_input("ENTER YOUR NAME")
    if st.button('Click'):
        if name:
            process_name(name)
        else:
            st.warning("Please enter your name!")

if __name__ == "__main__":
    main()

import streamlit as st

# Page settings
st.set_page_config(page_title="Multi-Page App", layout="wide")

# Define the pages
def page1():
    st.title("Page 1")
    st.write("This is the content of the first page.")

def page2():
    st.title("Page 2")
    st.write("Explore the content of the second page here.")

def page3():
    st.title("Page 3")
    st.write("Here's some information for the third page.")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choose a page:", ["Page 1", "Page 2", "Page 3"])

if page == "Page 1":
    page1()
elif page == "Page 2":
    page2()
elif page == "Page 3":
    page3()


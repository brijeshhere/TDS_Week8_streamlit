import streamlit as st

st.write("""
# Max of three number
""")
#Get Input

st.header('User Input Parameters')


a = st.number_input("First Number")
b= st.number_input("Second Number")
c= st.number_input("third Number")

st.header('Max of three')
st.write(max(a,b,c))

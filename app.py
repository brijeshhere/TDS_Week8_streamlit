import streamlit as st

st.write("""
# Max of three number
""")
#Get Input
input = st.empty()
st.header('User Input Parameters')


a = input.number_input("First Number")
b= input.number_input("Second Number")
c= input.number_input("third Number")

st.header('Max of three')
st.write(max(a,b,c))

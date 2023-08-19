import streamlit as st

st.write("""
# Max of three number
""")
#Get Input

st.header('User Input Parameters')


a = st.number_input("a")
b= st.number_input("b")
c= st.number_input("c")

st.write(max(a,b,c))

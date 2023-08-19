import streamlit as st

st.write("""
# Max of three number
""")
#Get Input

st.header('User Input Parameters')


a = st.number_input("a",step=1)
b= st.number_input("b",step=1)
c= st.number_input("c",step=1)

st.write(max(a,b,c))

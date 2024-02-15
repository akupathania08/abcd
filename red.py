import streamlit as st
x=st.radio('are you a student',option =['yes','no'])
if x=='yes':
    st.write('yes i am a student')
else:
    st.write('no,i am not a student')
# basic app to  test treamlit
import streamlit as st
st.title('hello word')
st.header('this is the header')
st.subheader('And here the subHeader')

st.write('Simple Test for Streamlit www.google.com')
if st.button('Baloons here'):
    st.balloons()

if st.sidebar.button('Zonage'):
    col1, col2 = st.columns([2,1])
    col1.header('Zone1')
    col1.write('Welcome to Heaven')
    col2.header('Zone2')
    col2.write('Welcome to Hell')
    

option = st.selectbox('how can we contact you?', ('phone','Email','SMS'))

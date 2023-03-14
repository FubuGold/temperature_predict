import pickle as pk
import sklearn as skl
import streamlit as st
f = open('model.pickle', 'rb')
model = pk.load(f)
number = model.predict(st.number_input('Input Temperature'))
if st.button('Predict'):
    st.success(number)


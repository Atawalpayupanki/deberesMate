from fractions import Fraction
import streamlit as st
st.title("hola chicos")
st.text("Ejercicio 42:")
numero=st.text_input("grados mayores a 360")
if numero is not None:
    st.text_area(int(numero)%360)
st.text("Ejercicio 43:")
nemero=st.text_input("numero que te da, sin el -")
if nemero is not None:
    st.text_area(360-int(numero)%360)
nmero=st.text_input("grados")
if nmero is not None:
    st.text_area(360-int(numero)%360)
    st.text_area(Fraction(int(nmero)*2,360), "π")


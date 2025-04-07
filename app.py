import streamlit as st
from fractions import Fraction

st.title("Hola chicos")

# Ejercicio 42
st.text("Ejercicio 42:")
numero = st.text_input("Grados mayores a 360")
if numero:
    try:
        numero = int(numero)
        st.write(f"Resultado: {numero % 360} grados")
    except ValueError:
        st.write("Por favor ingresa un número válido.")

# Ejercicio 43
st.text("Ejercicio 43:")
numero_sin_signo = st.text_input("Número sin el signo negativo (si es necesario)")
if numero_sin_signo:
    try:
        numero_sin_signo = int(numero_sin_signo)
        st.write(f"Resultado: {360 - (numero_sin_signo % 360)} grados")
    except ValueError:
        st.write("Por favor ingresa un número válido.")

# Ejercicio 44 (por los grados directamente)
st.text("Ejercicio 44:")
nmero = st.text_input("Grados")
if nmero:
    try:
        nmero = int(nmero)
        st.write(f"Resultado: {360 - (nmero % 360)} grados")
        # Mostrar la fracción en términos de π
        fraccion = Fraction(nmero * 2, 360)
        st.write(f"Fracción de π: {fraccion} π")
    except ValueError:
        st.write("Por favor ingresa un número válido.")


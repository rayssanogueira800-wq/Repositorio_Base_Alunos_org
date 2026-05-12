import streamlit as st

st.title("calculadora IM")
st.subheader("Feito com streamlit python ")

altura = st.number_input("Digite s sua altura", min_value = 0.0)
peso = st.number_input("Digite seu peso", min_value = 0.0)

if st.button("Calcular"):
    imc = peso / altura ** 2
    
    
    if imc < 18.5:
        st.error("Abaixo do peso")
 
    elif imc <= 24.9:
        st.error("Peso normal")

    elif imc <= 29.9: 
        st.error("sobrepeso")
        
    elif imc <= 34.9:
        st.error("obesidade I")

    elif imc <= 39.9:
        st.error("obesidade II")
        
    else:
        st.error("obesidade III")

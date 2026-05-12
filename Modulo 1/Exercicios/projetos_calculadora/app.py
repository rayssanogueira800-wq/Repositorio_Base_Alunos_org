import stramlit as st
import calculadora as calc 

st.image("https://cdn.pixabay.com/photo/2017/05/31/09/45/calculator-2359760_1280.jpg")
st.title("calculadora 📱")

numero1 = st.number_input("Digite o primeiro número: ", step=0.1,value=None)
numero2 = st.number_input("Digite o segundo número: ", step=0.1,value=None)
operacao = st.selectbox("Selecione a operação",["+","-","*","/"])

if st.button("Calcular"):
    resultado = calc.calcular(numero1, numero2, operacao)
    st.info(f"o resultado é: {resultado}")
    if resultado == 67:
        st.info("67")
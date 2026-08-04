import requests #Biblioteca mais fácil de se comunicar com APIs

import streamlit as st

cep = st.sidebar.text_input("Digite o CEP que deseja pesquisar", icon="🔎")
if st.sidebar.button("Pesquisar"): #Se clicar no button
    if len(cep) != 8:
        st.error("CEP inválido, digite sem ponto e traço e verifique os digitos")
        st.stop()

    busca = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
    if busca.status_code == 200:
        informações = busca.json()
        lat = informações.get("lat")
        lng = informações.get("lat")
        st.title(informações.get("city"))
        st.markdown(informações.get("address"))
        coluna1,coluna2 = st.columns(2)
        with coluna1: 
            st.metric("latitude", lat)
        with coluna2:
            st.metric("longitude",lng)

        st.map(latitude=lat, longitude=lng)
    # Mostrar as inforfações de endereço (variável busca)
    # Mostrar em um mapa usando a latitude e longitude (variável busca [st.mapa()])
    # Melhorar a validação do CEP
    # VOCE PRECISA SER CAPAZ DE ENTENDER TUDO O QUE A IA GERA!!!
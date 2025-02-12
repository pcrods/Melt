import pandas as pd
import streamlit as st
from io import BytesIO

st.title('Funbio')
st.subheader('Tratamento de dados')
pasta_base = st.file_uploader("Carregue o Banco de Dados (.xlsx)", type=["xlsx"])

if pasta_base:
    df = pd.read_excel(pasta_base)
    st.subheader("Dados Originais")
    st.dataframe(df)

    col1, col2= st.columns(2)

    with col1:
        button_1 = st.button('Transformar em formato GIS')

    with col2:
        button_2 = st.button('Transformar em formato GIS sem valores nulos')

    data_container = st.empty()  # Usado para exibir os dados abaixo dos botões
    st.divider()
    if button_1:
        df_long = df.melt(id_vars=["Táxon"],
                  var_name="ID_Réplica",
                  value_name="Abundância")
        
        st.subheader("Dados Transformados")
        st.dataframe(df_long)
    if button_2: 
        df_long = df.melt(id_vars=["Táxon"],
                  var_name="ID_Réplica",
                  value_name="Abundância")
        df_clean = df_long.dropna()
        st.subheader("Dados Limpos (Sem valores nulos)")
        st.dataframe(df_clean)

        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            df_clean.to_excel(writer, index=False, sheet_name="Dados Limpos")
        output.seek(0)

        st.download_button(label = "Baixar dados limpos em xlsx", data=output, file_name="dados limpos FUNBIO",)
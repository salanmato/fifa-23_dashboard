import streamlit as st
import pandas as pd
import webbrowser as web
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv('datasets/CLEAN_FIFA23_official_data.csv', index_col=0)
    df_data = df_data.sort_values('Overall', ascending=False)
    st.session_state["data"] = df_data

st.markdown('# FIFA OFFICIAL DATASET')

st.markdown(' Desenvolvido por [Asimov Academy](https://asimov.academy/) e adaptado por [Alan Matos](https://www.linkedin.com/in/salanmato/)')
btn = st.button('Acesse os dados no Kaggle')

if btn:
    web.open('https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data')
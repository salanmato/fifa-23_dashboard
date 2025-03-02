import streamlit as st
from functools import reduce
import pandas as pd

st.set_page_config(
    page_title="Teams", 
    page_icon=":soccer:", 
    layout="wide")

# Diagramação da página
col0, col1 = st.columns([1, 9])
col2, col3 = st.columns([1, 1])
col4 = st.columns([1])[0]
col5 = st.columns([1])[0]
col6 = st.columns([1])[0]
col7 = st.columns([1])[0]
col8 = st.columns([1])[0]

# ordem das posições
order = ["GK", "CB", "LB", "RB", "RWB", "LWB", "LCB", "RCB", "CDM", "CM", "CAM", "RM", "LM", "AM", "RCM", "LCM", "RDM", "ST", "SS", "CF", "LW", "RW", "SUB", "RES"]

# trabalhando com a data
df = st.session_state["data"]
df['Potencial'] = (df['Potential'] - df['Overall']) # calculando o potencial
df['Weight(kgs.)'] = (df['Weight(lbs.)'] * 0.453592).round(0) # convertendo para kg
df = df.reset_index(drop=True)

df['Position'] = pd.Categorical(df['Position'], categories=order, ordered=True)
df_data = df.sort_values('Position')

collumns = ["Flag", "Photo", "Name", "Overall","Potencial", "Position", "Age", "Height(cm.)", "Weight(kgs.)", "Nationality", "Value(£)", "Preferred Foot"]

clubes = df_data["Club"].unique()

club = st.sidebar.selectbox("Escolha um time", clubes) # seletor de clube

club_filtered = df_data[(df_data["Club"] == club)] # filtrando o dataframe

st.dataframe(club_filtered[collumns],
             column_config={
                 "Overall": st.column_config.ProgressColumn("Overall", min_value=0, max_value=100, format="%d"),
                 "Photo": st.column_config.ImageColumn("Photo", width=48),
                 "Flag": st.column_config.ImageColumn("Flag", width=48),
             })

# montando a página
col0.image(club_filtered["Club Logo"].values[0], width=48) 
col1.markdown(f"## {club}")


overall = reduce(lambda x, y: x + y, club_filtered["Overall"]) / len(club_filtered["Overall"])
col2.markdown(f"##### Overall médio do time: {round(overall, 2)}")

potencial = reduce(lambda x, y: x + y, club_filtered["Potential"]) / len(club_filtered["Potential"])
col3.markdown(f"##### Potencial médio do time: +{round(potencial - overall, 0)}")


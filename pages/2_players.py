import streamlit as st

st.set_page_config(
    page_title="Players", 
    page_icon=":soccer:", 
    layout="wide")

# Usando HTML e CSS para centralizar o conteúdo
st.markdown(
    """
    <style>
    .main .block-container {
        max-width: 800px;
        margin: auto;
        text-align: center;
    }

    .stMainBlockContainer div{
        
        display: flex !important;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center !important;

        max-width: 800px;
        width: 100%;
    }

    h3[level="3"] {
    text-align: center !important;
    }


    </style>
    """,
    unsafe_allow_html=True
)

# Diagramação da página
col0 = st.columns([1])[0]
col1 = st.columns([1])[0]
col2 = st.columns([1])[0]
col3 = st.columns([1])[0]
col4 = st.columns([1])[0]
col5 = st.columns([1])[0]
col6 = st.columns([1])[0]
col7 = st.columns([1])[0]
col8 = st.columns([1])[0]


df_data = st.session_state["data"]

df_nationalities = df_data[df_data["Nationality"].notnull()]
nations = df_nationalities["Nationality"].value_counts().index
nations_options = ["Todos"] + list(nations)
nation = st.sidebar.selectbox("Nacionalidade", nations_options, index=0) # seletor de nacionalidade

# Filtra os clubes com base na nacionalidade selecionada
if nation == "Todos":
    df_clubs = df_data[df_data["Club"].notnull()]
else:
    df_clubs = df_data[(df_data["Club"].notnull()) & (df_data["Nationality"] == nation)]

clubs = df_clubs["Club"].value_counts().index
club_options = ["Todos"] + list(clubs)  
club = st.sidebar.selectbox("Clube", club_options, index=0) #seletor de clubes


overall_range = st.sidebar.slider("Overall", min_value=20, max_value=100, value=(20, 100), step=1) # slider Overall

# Filtra os jogadores com base na nacionalidade e clube selecionados
if nation == "Todos" and club == "Todos":
    df_players_filtered = df_data  # Mostra todos os jogadores
elif nation == "Todos":
    df_players_filtered = df_data[df_data["Club"] == club]  # Filtra apenas pelo clube
elif club == "Todos":
    df_players_filtered = df_data[df_data["Nationality"] == nation]  # Filtra apenas pela nacionalidade
else:
    df_players_filtered = df_data[(df_data["Nationality"] == nation) & (df_data["Club"] == club)]  # Filtra por ambos

df_players = df_players_filtered[
    (df_players_filtered["Overall"] >= overall_range[0]) & (df_players_filtered["Overall"] <= overall_range[1])
]

players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogador", players, index=None) # seletor de jogadores






st.divider()

if player:

    player_stats = df_players[df_players["Name"] == player].iloc[0]



    col1.image(player_stats["Photo"], width=100)
    col2.header(f"{player_stats['Name']}")

    col3.markdown(f"![flag]({player_stats["Flag"]}) - ----------------------------------- - ![Club Logo]({player_stats["Club Logo"]})")

    col4.markdown(f"## £{player_stats['Value(£)']:.0f}")
    col5.markdown(f"### {player_stats['Overall']}📜 ↗️ {player_stats['Potential']}🔝")
    

    with col6:
        subcol0, subcol1 = col6.columns(2)
        subcol0.markdown(f"##### {player_stats['Height(cm.)']:.0f} cm")
        subcol1.markdown(f"##### {'{:.0f}'.format(player_stats['Weight(lbs.)'] * 0.45359237)} kg")


    with col7:
        subcol0, subcol1 = col7.columns(2)
        subcol0.markdown(f"##### {player_stats['Age']} anos")
        subcol1.markdown(f"##### Pé Preferido: {"Direito" if player_stats['Preferred Foot'] == 'Right' else 'Esquerdo'}")


else:
    col1.markdown("**Selecione um jogador**")

import configuration as config
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout="wide")

col1 = st.sidebar
col2, col3 = st.beta_columns([3, 1])
col2.title("Individual NBA Player Statistics")

with col1:
    st.subheader("User Input Features")
    selected_year = st.selectbox("Year 1 to Year", list((range(2, 9))), 3)
    SelectedPlayer = st.multiselect("Player",
                                    config.PLAYER_LIST,
                                    config.PLAYER_LIST[:5]
                                    )                              

with col2:
    @st.cache(allow_output_mutation=True)
    def load_data(url):
        html = pd.read_html(url, header=0)
        df = html[0]
        df = df[:selected_year]
        df["Years In NBA"] = range(1, selected_year+1)
        return df

    dataframes = []
    for player in SelectedPlayer:
        st.title(player)
        url = config.URL+config.URL_SUFFIX[player]
        df = load_data(url)
        df["Player Name"] = player
        dataframes.append(df)
        st.write(df)

cols = list(dataframes[0].columns[5:-2])
selected_stats = st.sidebar.multiselect('Player Stats', cols[5:-2], cols[5:10])
col1.markdown(config.GLOSSARY)

dataframes_stacked = pd.concat(dataframes, axis=0)
dataframes_stacked.to_csv('output.csv', index=False)
dataframes_stacked = pd.read_csv('output.csv')

col3.title("Player Comparison")
with col3:
    for stat in selected_stats:
        st.subheader(config.GLOSSARY2[stat])
        pivot = dataframes_stacked.pivot("Years In NBA", "Player Name", stat)
        st.write(pivot)
        with sns.axes_style("darkgrid"):
            f, ax = plt.subplots(figsize=(7, 5))
            ax = sns.lineplot(data=pivot)
            st.pyplot(f)

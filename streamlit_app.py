import configuration as config
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(layout="wide")
col1 = st.sidebar
col2, col3 = st.beta_columns([7,3])

col3.title("Individual NBA Player Statistics")

with col1:
    st.subheader("User Input Features")
    selected_year = st.selectbox("Year 1 to Year", list((range(2, 9))), 3)
    SelectedPlayer = st.multiselect("Player",
                                    config.PLAYER_LIST,
                                    config.PLAYER_LIST[:5]
                                    )           

with col3:
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

col2.title("Player Comparison")

for stat in selected_stats:
    col2.subheader(config.GLOSSARY2[stat])
    pivot = dataframes_stacked.pivot("Years In NBA", "Player Name", stat)
    col2.write(pivot)
    with sns.axes_style("darkgrid"):
        f, ax = plt.subplots(figsize=(5, 3))
        ax = sns.lineplot(data=pivot)
        plt.legend(fontsize='xx-small',
                   title_fontsize='xx-small',
                   loc='center left',
                   bbox_to_anchor=(1, 0.5))
        col2.pyplot(f)

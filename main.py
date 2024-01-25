import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px


image_tvpis = Image.open("files/tvpis.png")
image_reddit = Image.open("files/reddit.png")
width, height = 100, 100
image_reddit.thumbnail((width, height), Image.ANTIALIAS)

st.image(image_tvpis, use_column_width=True)

# tab1 = st.tabs(["Czasowninki", "Popularne", "Przykłady"])


###################
# Tab for czasowniki
###################

df = pd.read_csv("files/df_pol_5models_words.csv",
                 lineterminator='\n')

df_transposed = pd.read_csv("files/df_transposed.csv")

fig = px.bar(df_transposed,  labels={
                     "nonhate": "NoHATE",
                     "hate": "HATE",
                     "variable": "HATE?"
                 },
             title="Rozkład grup czasownikowych w HATE Trelbert", width=1000)

fig.update_layout(xaxis_title='Grupa czasowników', yaxis_title='Znormalizowana ilość')


# with tab1:

show_explicit_content = None

if show_explicit_content is None:
    if st.button("Zobacz przykładowe treści"):
        show_explicit_content = True
        st.text("Nie odpowiadamy za treści pokazywanych wpisów.")

if show_explicit_content:
    st.dataframe(df.iloc[:, 1:9].head(100))
else:
    st.image(image_reddit, use_column_width=False)


st.markdown("""---""")
st.plotly_chart(fig)
st.markdown("""---""")


df_verbs = pd.read_csv('files/czasowniki.csv', header=None)
df_verbs = df_verbs.iloc[:12]

categories = df_verbs.iloc[:, 0].unique()

selected_category = st.selectbox("Zobacz czasowniki z kategorii z powyższego wykresu:", categories)

filtered_data = df_verbs[df_verbs.iloc[:, 0] == selected_category]

if not filtered_data.empty:
    verb_list = filtered_data.iloc[:, 1].values[0]
    st.write(verb_list)
else:
    st.warning("Brak danych.")

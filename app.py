import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les données CSV
@st.cache_data
def load_data():
    return pd.read_csv("test.csv")

data = load_data()

# Titre de l'application
st.title("Test de Streamlit : Analyse des petites villes")

# Afficher les données brutes
if st.checkbox("Afficher les données brutes"):
    st.write(data)

# Sélectionner une ville
st.subheader("Données par ville")
ville = st.selectbox("Choisissez une ville :", data["ville"].unique())
ville_data = data[data["ville"] == ville]
st.write(ville_data)

# Graphiques interactifs
st.subheader("Visualisation des données")
fig, ax = plt.subplots()
sns.barplot(data=data, x="ville", y="population", ax=ax)
st.pyplot(fig)

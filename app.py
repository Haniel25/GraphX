import streamlit as st

st.title("📊 Graph X")

st.write("Bienvenue sur Graph X 🚀")

x = st.number_input("Entrer X")
y = st.number_input("Entrer Y")

st.success(f"Résultat : {x + y}")
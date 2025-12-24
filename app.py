import streamlit as st
import pandas as pd
import joblib
import numpy as np

import streamlit as st

st.sidebar.image("logoehtp.jpg", width=150)
st.sidebar.title("Mini-projet Machine Learning")
st.sidebar.write("Détection des attaques IoT")
st.sidebar.write("Nom : BELMOKHTARE Fatima Ezzahra")
st.sidebar.write("Filière : GIS – EHTP")



# Charger le modèle et le scaler
model = joblib.load("modele_final.pkl")
scaler = joblib.load("scaler.pkl")

st.title("Détection des attaques IoT")

st.write("Cette application permet de prédire le type d’attaque réseau à partir des caractéristiques du trafic.")

st.subheader("Entrer les caractéristiques")

# Champs simples (tu peux adapter selon tes features réelles)
flow_duration = st.number_input("flow_duration", value=0.0)
fwd_pkts_tot = st.number_input("fwd_pkts_tot", value=0.0)
bwd_pkts_tot = st.number_input("bwd_pkts_tot", value=0.0)
fwd_data_pkts_tot = st.number_input("fwd_data_pkts_tot", value=0.0)
bwd_data_pkts_tot = st.number_input("bwd_data_pkts_tot", value=0.0)

if st.button("Prédire"):
    X = np.array([[flow_duration, fwd_pkts_tot, bwd_pkts_tot,
                   fwd_data_pkts_tot, bwd_data_pkts_tot]])

    X_scaled = scaler.transform(X)
    prediction = model.predict(X_scaled)

    st.success(f"Attaque détectée : {prediction[0]}")

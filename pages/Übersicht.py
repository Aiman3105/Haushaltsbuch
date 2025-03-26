import streamlit as st
import json
import Funktionen

st.title("Übersicht")
col_N_Ü, col_NP_Ü, col_A_Ü, col_AP_Ü=st.columns(4)

with col_N_Ü:
    st.markdown("**Natalie**")


with col_NP_Ü:
    st.text(Funktionen.get_Punkte("Natalie"))


with col_A_Ü:
    st.markdown("**Aiman**")


with col_AP_Ü:
    st.text(Funktionen.get_Punkte("Aiman"))


st.sidebar.page_link("Haushaltsbuch.py", label="⬅️ Zurück zur Hauptseite")
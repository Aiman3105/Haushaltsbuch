import streamlit as st
import json
import Funktionen

st.title("Haushaltsbuch")


col_N, col_NP, col_A, col_AP=st.columns(4)
with col_N:
    st.markdown("**Natalie**")
    st.text_input(label="", placeholder="Aufgabe",
                  key="neue_Aufgabe")

with col_NP:
    st.text(Funktionen.get_Punkte("Natalie"))
    st.text_input(label="", placeholder="Punkte",
                  key="neue_Punkte")

with col_A:
    st.markdown("**Aiman**")
    st.text_input("", key="A_Aufgabe")

with col_AP:
    st.text(Funktionen.get_Punkte("Aiman"))
    st.text_input("", key="A_Punkte")


import streamlit as st
import json
import Funktionen

st.title("Haushaltsbuch")

def add_Natalie():
    if st.session_state["neue_Punkte_N"]:
        alt=Funktionen.get_Punkte("Natalie")
        dazu=int(st.session_state["neue_Punkte_N"])
        neu=alt+dazu
        Funktionen.update_Punkte("Natalie", neu)
        st.session_state["neue_Punkte_N"]=""


col_N, col_NP, col_A, col_AP=st.columns(4)
with col_N:
    st.markdown("**Natalie**")
    st.text_input(label="", placeholder="Aufgabe",
                  key="neue_Aufgabe_N")

with col_NP:
    st.text(Funktionen.get_Punkte("Natalie"))
    st.text_input("", placeholder="Punkte",
                  on_change=add_Natalie, key="neue_Punkte_N")

with col_A:
    st.markdown("**Aiman**")
    st.text_input("", key="A_Aufgabe")

with col_AP:
    st.text(Funktionen.get_Punkte("Aiman"))
    st.text_input("", key="A_Punkte")


st.sidebar.page_link("pages/Übersicht.py", label="Zur Übersicht ➡️")


import streamlit as st
import json
import Funktionen

st.title("Haushaltsbuch")

col_N, col_NP, col_A, col_AP=st.columns(4)

with open("Punkte_N.txt", "r") as file:
    Punkte_N = file.readlines()

with open("Aufgaben_N.txt", "r") as file:
    Aufgaben_N = file.readlines()


def add_Natalie():
    if st.session_state["neue_Punkte_N"]:
        alt=Funktionen.get_Punkte("Natalie")
        dazu=int(st.session_state["neue_Punkte_N"])
        neu=alt+dazu
        Funktionen.update_Punkte("Natalie", neu)

        with col_NP:
            Punkte_N.append(st.session_state["neue_Punkte_N"]+"\n")
            with open("Punkte_N.txt", "w") as file:
                file.writelines(Punkte_N)
        st.session_state["neue_Punkte_N"]=""

    if st.session_state["neue_Aufgabe_N"]:
        with col_N:
            Aufgaben_N.append(st.session_state["neue_Aufgabe_N"]+"\n")
            with open("Aufgaben_N.txt", "w") as file:
                file.writelines(Aufgaben_N)
        st.session_state["neue_Aufgabe_N"]=""




with col_N:
    st.markdown("**Natalie**")
    st.text_input(label="", placeholder="Aufgabe",
                  on_change=add_Natalie,
                  key="neue_Aufgabe_N")

    for Aufgabe in Aufgaben_N:
        st.text(Aufgabe)

with col_NP:
    st.text(Funktionen.get_Punkte("Natalie"))
    st.text_input("", placeholder="Punkte",
                  on_change=add_Natalie, key="neue_Punkte_N")

    for Punkte in Punkte_N:
        st.text(Punkte)

with col_A:
    st.markdown("**Aiman**")
    st.text_input("", key="A_Aufgabe")

with col_AP:
    st.text(Funktionen.get_Punkte("Aiman"))
    st.text_input("", key="A_Punkte")


if "spalte_geloescht" not in st.session_state:
    st.session_state.spalte_geloescht = False
if st.button("refresh"):
    st.session_state.spalte_geloescht = True
    with open("Aufgaben_N.txt", "w") as file:
        Aufgaben_N=[]
        file.writelines(Aufgaben_N)
    with open("Punkte_N.txt", "w") as file:
        Punkte_N=[]
        file.writelines(Punkte_N)



st.sidebar.page_link("pages/Übersicht.py", label="Zur Übersicht ➡️")


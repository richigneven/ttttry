import streamlit as st

# Titel und Einleitung
st.title("Meine erste Kneipen-Webapp 🐍")
st.write("Dies ist eine einfache Demo! Du kannst Text eingeben und speichern (erstmal lokal im Speicher).")

# Einfache lokale Datenbank (nur zur Demo)
if "daten" not in st.session_state:
    st.session_state.daten = []

# Eingabefeld und Button
ingabe = st.text_input("Gib einen Text ein:")
if st.button("Hinzufügen"):
    if eingabe:
        st.session_state.daten.append(eingabe)
        st.success(f"'{eingabe}' wurde gespeichert!")

# Anzeige gespeicherter Daten
if st.session_state.daten:
    st.subheader("Bisher eingegebene Daten:")
    for eintrag in st.session_state.daten:
        st.write("•", eintrag)
else:
    st.info("Noch keine Daten gespeichert.")

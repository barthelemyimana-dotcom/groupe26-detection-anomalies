import hashlib
import streamlit as st
import pandas as pd
import random
from sklearn.ensemble import IsolationForest

st.set_page_config(
    page_title="Groupe 26 - Détection réseau",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Détection intelligente des anomalies réseau")
st.subheader("Groupe 26 — Cybersécurité et intelligence artificielle")

st.write(
    "Cette application analyse des données fictives de trafic réseau "
    "et utilise l'intelligence artificielle pour repérer des comportements inhabituels."
)

st.info("Mode démonstration : aucune donnée réelle du réseau n'est collectée.")

if st.button("Analyser le trafic réseau de démonstration"):

    donnees = []

    for i in range(100):
        paquets = random.randint(10, 1000)
        duree = random.randint(1, 120)

        # Quelques valeurs extrêmes pour simuler des anomalies
        if i in [12, 37, 76]:
            paquets = random.randint(3000, 5000)
            duree = random.randint(1, 3)

        donnees.append({
            "Flux réseau": i + 1,
            "Paquets": paquets,
            "Durée (s)": duree,
            "Port": random.choice([80, 443, 22, 53, 8080])
        })

    df = pd.DataFrame(donnees)

    modele = IsolationForest(
        contamination=0.05,
        random_state=42
    )

    caracteristiques = df[["Paquets", "Durée (s)"]]
    predictions = modele.fit_predict(caracteristiques)

    df["Résultat IA"] = [
        "Anomalie potentielle" if resultat == -1 else "Normal"
        for resultat in predictions
    ]

    nombre_anomalies = (df["Résultat IA"] == "Anomalie potentielle").sum()
    # Calcul de l'empreinte SHA-256 des résultats
    contenu = df.to_csv(index=False).encode("utf-8")
    empreinte = hashlib.sha256(contenu).hexdigest()

    st.subheader("Vérification de l'intégrité des résultats")
    st.write("Empreinte SHA-256 :")
    st.code(empreinte)
    st.caption(
        "Cette empreinte permet de comparer les résultats "
        "et de repérer une éventuelle modification des données."
    )
    st.success("Analyse terminée.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Flux analysés", len(df))
    col2.metric("Anomalies potentielles", int(nombre_anomalies))
    col3.metric("Flux normaux", len(df) - int(nombre_anomalies))

    st.subheader("Résultats de l'analyse")
    st.dataframe(df, use_container_width=True)

    st.subheader("Nombre de paquets par flux")
    st.bar_chart(df.set_index("Flux réseau")["Paquets"])

    
    st.subheader("Flux signalés par l'intelligence artificielle")
    anomalies = df[df["Résultat IA"] == "Anomalie potentielle"]

    if anomalies.empty:
        st.info("Aucune anomalie potentielle détectée.")
    else:
        st.warning(
            f"{len(anomalies)} flux présentent des caractéristiques inhabituelles."
        )

        st.dataframe(anomalies, use_container_width=True)

        st.subheader("Explication des alertes")

        for _, ligne in anomalies.iterrows():
            raisons = []

            if ligne["Paquets"] > 2000:
                raisons.append("nombre de paquets exceptionnellement élevé")

            if ligne["Durée (s)"] <= 3:
                raisons.append("durée très courte")

            if not raisons:
                raisons.append(
                    "combinaison inhabituelle du nombre de paquets et de la durée"
                )

            st.write(
                f"**Flux {int(ligne['Flux réseau'])} :** "
                + ", ".join(raisons)
                + "."
            )

    st.caption(
        "Les alertes sont expérimentales et reposent sur des données fictives. "
        "Une anomalie potentielle ne prouve pas qu'une attaque a eu lieu."
    )


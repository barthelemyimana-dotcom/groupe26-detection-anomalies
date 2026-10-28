# 🛡️ Groupe 26 — Détection intelligente des anomalies réseau

## 1. Présentation du projet

Ce projet consiste à développer une application web capable d'analyser des données fictives de trafic réseau et d'identifier automatiquement des comportements inhabituels à l'aide de techniques d'intelligence artificielle.

L'application utilise Python, Streamlit, Pandas et l'algorithme Isolation Forest de Scikit-learn.

 2. Membres du groupe

- BASEMBE IMANA BARTHÉLÉMY
- MANDEKA ZANGA ESTHER
- NZUNGU KASWAKA GLODI
- MALUMONA LENDO ZAFI

 3. Objectifs

- Simuler des flux de trafic réseau.
- Détecter des anomalies potentielles grâce à l'intelligence artificielle.
- Afficher les résultats dans un tableau de bord interactif.
- Sensibiliser à la surveillance et à la sécurité des réseaux informatiques.

 4. Technologies utilisées

- Python : langage de programmation.
- Streamlit : interface web interactive.
- Pandas : traitement des données.
- Scikit-learn : détection d'anomalies avec Isolation Forest.
- Git et GitHub : gestion et hébergement du code source.
- HTTPS/TLS : sécurisation de l'accès à l'application déployée.

 5. Fonctionnement

1. L'utilisateur lance l'analyse depuis le tableau de bord.
2. L'application génère 100 flux réseau fictifs.
3. Chaque flux est caractérisé notamment par son nombre de paquets et sa durée.
4. Le modèle Isolation Forest recherche les comportements inhabituels.
5. L'application affiche le nombre de flux analysés, les anomalies potentielles, les flux normaux et les résultats détaillés.

 6. Architecture

L'application suit le fonctionnement suivant :

Utilisateur → Interface Streamlit → Génération de données fictives → Modèle Isolation Forest → Résultats et visualisations

 7. Sécurité et limites

- Les données utilisées pour la démonstration sont fictives.
- L'application ne collecte pas directement le trafic réel d'un réseau.
- Une anomalie potentielle ne prouve pas qu'une attaque a eu lieu.
- HTTPS/TLS protège les communications entre le navigateur et l'application hébergée.
- Cette version constitue un prototype pédagogique. Les mécanismes de sécurité supplémentaires et les tests devront être documentés selon leur mise en œuvre effective.
### Vérification de l'intégrité avec SHA-256

L'application calcule une empreinte cryptographique SHA-256 à partir des résultats de l'analyse au format CSV.

Cette empreinte permet de comparer deux versions des résultats et de détecter une modification lorsque le contenu comparé change.

**Limite :** l'empreinte affichée n'est pas une signature numérique et ne garantit pas, à elle seule, l'authenticité des résultats.
 8. Installation locale

Prérequis : Python installé sur l'ordinateur.

Cloner le dépôt :

bash
git clone https://github.com/barthelemyimana-dotcom/groupe26-detection-anomalies.git
cd groupe26-detection-anomalies


Installer les dépendances :

bash
pip install -r requirements.txt


Lancer l'application :

bash
streamlit run app.py


 9. Démonstration en ligne

Application web : https://groupe26-detection-anomalies-nppan5mknswpvdxdxtbp9db.streamlit.app/

 10. Conclusion

Ce projet montre comment l'intelligence artificielle peut contribuer à l'identification de comportements inhabituels dans des données de trafic réseau simulées. Il constitue une base pour des améliorations futures en matière de cybersécurité et de détection d'anomalies.

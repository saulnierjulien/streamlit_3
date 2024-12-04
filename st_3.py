import streamlit as st
from streamlit_authenticator import Authenticate
from PIL import Image

# Données utilisateurs
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0,
   'logged_in': False,
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0,
   'logged_in': False,
   'role': 'administrateur'}}}

# Configuration de l'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30
)

# Appel à la méthode de connexion
authenticator.login()

# Fonction d'accueil
def accueil():
    st.title("Bienvenue sur la page de JUJU")

# Vérification de l'authentification
if st.session_state.get("authentication_status"):
    accueil()
    authenticator.logout("Déconnexion")

    # Création du menu dans la barre latérale avec des boutons
    st.sidebar.title("Menu")
    menu_selection = st.sidebar.radio("Choisissez une option", ["Accueil", "Photos"], horizontal=True)

    # Affichage en fonction du choix
    if menu_selection == "Accueil":
        st.write("Bienvenue sur la page d'accueil !")
                # Charger et afficher image
        image1 = Image.open("manhattan.jpeg")
        
        # Affichage image avec use_container_width
        st.image(image1, use_container_width=True)

    elif menu_selection == "Photos":
        st.write("Bienvenue sur mon album photo !")

        # Charger et afficher plusieurs images
        image2 = Image.open("brooklyn.jpeg")
        image3 = Image.open("queens.jpeg")
        image4 = Image.open("bronx.jpeg")
        
        # Diviser la page en 3 colonnes pour afficher les images côte à côte
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image(image2, use_container_width=True)
        with col2:
            st.image(image3, use_container_width=True)
        with col3:
            st.image(image4, use_container_width=True)

else:
    # Gérer les erreurs
    if st.session_state.get("authentication_status") is False:
        st.error("L'username ou le mot de passe est incorrect")
    elif st.session_state.get("authentication_status") is None:
        st.warning("Les champs username et mot de passe doivent être remplis")
import streamlit as st
from streamlit_authenticator import Authenticate
from PIL import Image
from streamlit_option_menu import option_menu  # Import du module

# Installation des dépendances si nécessaire :
# !pip install streamlit-option-menu

# Données utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# Configuration de l'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,
    "cookie_name",
    "cookie_key",
    30
)

# Appel à la méthode de connexion
authenticator.login()

# Fonction pour l'onglet "Accueil"
def accueil():
    st.title("Bienvenue sur la page de JUJU")
    st.write("Ceci est la page d'accueil où vous trouverez toutes les informations importantes.")
    try:
        image1 = Image.open("manhattan.jpeg")
        st.image(image1, use_container_width=True)
    except Exception as e:
        st.error(f"Erreur lors du chargement de l'image : {e}")

# Fonction pour l'onglet "Photos"
def photos():
    st.title("Bienvenue sur mon album photo !")
    try:
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
    except Exception as e:
        st.error(f"Erreur lors du chargement des images : {e}")

# Vérification de l'authentification
if st.session_state.get("authentication_status"):

    # Menu principal avec streamlit-option-menu
    with st.sidebar:
        menu_selection = option_menu(
            menu_title="Menu Principal",  # Titre du menu
            options=["Accueil", "Photos"],  # Options du menu
            icons=["house", "camera"],  # Icônes (FontAwesome ou Bootstrap)
            menu_icon="cast",  # Icône principale du menu
            default_index=0,  # Option sélectionnée par défaut
        )

    # Affichage en fonction du choix du menu
    if menu_selection == "Accueil":
        accueil()
    elif menu_selection == "Photos":
        photos()

    # Bouton pour se déconnecter
    authenticator.logout("Déconnexion", "sidebar")

else:
    # Gérer les erreurs d'authentification
    if st.session_state.get("authentication_status") is False:
        st.error("L'username ou le mot de passe est incorrect")
    elif st.session_state.get("authentication_status") is None:
        st.warning("Les champs username et mot de passe doivent être remplis")

import streamlit as st
import datetime

# Configuration de la page
st.set_page_config(
    page_title="Test AWS - Simple App",
    page_icon="🚀",
    layout="centered"
)

# Initialisation du state pour stocker les messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Titre de l'application
st.title("🚀 Application Test AWS")
st.write("Application simple pour tester le déploiement sur AWS")

# Zone de saisie avec formulaire
st.subheader("Envoyez votre message :")

with st.form("test_form", clear_on_submit=True):
    user_input = st.text_area(
        "Tapez votre message ici...", 
        height=100,
        placeholder="Entrez votre texte pour tester..."
    )
    submitted = st.form_submit_button("📤 Envoyer", type="primary")
    
    if submitted:
        if user_input.strip():
            # Ajouter timestamp et message
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message_data = {
                "timestamp": timestamp,
                "message": user_input.strip()
            }
            
            # Stocker le message
            st.session_state.messages.append(message_data)
            
            # Confirmer la réception
            st.success(f"✅ Message reçu à {timestamp}")
            
            # Afficher le message pour vérification
            st.info(f"**Contenu reçu :** {user_input.strip()}")
            
        else:
            st.error("❌ Veuillez entrer un message avant d'envoyer.")

# Séparateur
st.divider()

# Affichage des messages reçus
st.subheader("Messages reçus :")

if st.session_state.messages:
    st.write(f"**Total des messages :** {len(st.session_state.messages)}")
    
    # Afficher les 5 derniers messages
    recent_messages = st.session_state.messages[-5:]
    
    for i, msg_data in enumerate(reversed(recent_messages), 1):
        with st.container():
            st.write(f"**Message #{len(st.session_state.messages) - i + 1}**")
            st.write(f"🕒 {msg_data['timestamp']}")
            st.write(f"💬 {msg_data['message']}")
            st.write("---")
    
    # Bouton pour voir tous les messages
    if len(st.session_state.messages) > 5:
        with st.expander(f"Voir tous les {len(st.session_state.messages)} messages"):
            for i, msg_data in enumerate(reversed(st.session_state.messages), 1):
                st.write(f"**#{len(st.session_state.messages) - i + 1}** - {msg_data['timestamp']}")
                st.write(f"💬 {msg_data['message']}")
                st.write("---")
    
    # Bouton pour vider l'historique
    if st.button("🗑️ Vider l'historique", type="secondary"):
        st.session_state.messages = []
        st.rerun()
        
else:
    st.info("Aucun message reçu. Envoyez votre premier message de test !")

# Informations techniques pour debugging AWS
st.divider()
with st.expander("ℹ️ Informations techniques"):
    st.write("**Informations pour le debugging AWS :**")
    st.json({
        "total_messages": len(st.session_state.messages),
        "session_state_keys": list(st.session_state.keys()),
        "last_message_time": st.session_state.messages[-1]["timestamp"] if st.session_state.messages else "Aucun message",
        "app_status": "✅ Fonctionnel"
    })

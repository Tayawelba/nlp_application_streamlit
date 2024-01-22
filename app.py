import streamlit as st
import requests
import time
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import os



TOKEN_API = os.environ.get("HF_TOKEN2")

#changement du logo et du titre de mon application en anglais
st.set_page_config(page_title="NLP Outro", page_icon=":brain:", layout="centered", menu_items=None)



# Créer trois colonnes de largeur égale
col1, col2, col3 = st.columns(3)

# Laisser la première et la troisième colonne vides
with col1:
  st.write("")

# Afficher le logo dans la deuxième colonne
with col2:
  st.image("img/logo2.png", use_column_width=None)

with col3:
    st.write("")

selected = option_menu(
            menu_title=None,  # required
            options=["Accueil", "Traduction", "Résumer", "Chatbot"],  # required
            icons=["house", "translate","journal-text", "chat-dots"],  # optional
            menu_icon="cast",  # optional
            default_index=0,  # optional
            orientation="horizontal",
        )

if selected == "Accueil":
    st.title(f"{selected}")

    # Display home page with app description and logo
    st.header('Bienvenue sur l\'application qui est un outil polyvalent qui combine trois fonctionnalités principales : la traduction, le résumé et le chatbot.')
    st.image('img/image1.jpg', caption='Large Language Model')
    #st.title('Bienvenue sur l\'application de classification d\'images de radiographies pulmonaires')
    #st.markdown("<h1 style='text-align: center;'>Bienvenue sur l'application de classification d'images de radiographies pulmonaires</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify;'><b>La traduction</b> permet de convertir du texte entre cinq langues : l’anglais, l’allemand, le français, le chinois et l’espagnol. Elle utilise les modèles de Helsinki-NLP, qui sont des modèles de traduction automatique neuronale basés sur le Transformer. Ces modèles sont rapides, précis et capables de gérer des langues morphologiquement riches.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify;'><b>Le résumé</b> permet de condenser un texte long en un texte court qui en conserve les informations essentielles. Il utilise le modèle facebook/bart-large-cnn , qui est une variante du modèle T56 adaptée et affinée pour la tâche de résumé de texte. Ce modèle est entraîné sur un ensemble diversifié de documents et de résumés humains, ce qui lui permet de générer des résumés concis et cohérents.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify;'><b>Le chatbot</b> permet de dialoguer avec l’application en utilisant un langage naturel. Il utilise le modèle /tiiuae/falcon-7b-instruct, qui est un modèle de génération de texte causal basé sur Falcon-7B et affiné sur un mélange de données de chat et d’instruction. Ce modèle est capable de répondre à des requêtes variées, de suivre des instructions et de créer du contenu imaginatif.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify;'>Mon application utilise l’Inference API de Hugging Face pour accéder aux modèles et les exécuter via des requêtes HTTP simples. L’Inference API est un service gratuit et rapide qui permet de tester et d’évaluer plus de 150 000 modèles de machine learning accessibles au public, ou vos propres modèles privés, sur l’infrastructure partagée de Hugging Face.</h5>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: justify;'>Mon application est donc un outil puissant et innovant qui exploite les dernières avancées de l’intelligence artificielle pour offrir des services de traduction, de résumé et de chatbot de haute qualité.</h5>", unsafe_allow_html=True)


    components.html(
    """
        <div style="position: fixed; bottom: 0; left: 0; right: 0; text-align: center; font-size: 15px; color: gray;">
        Tous droits réservés © Décembre 2023 Tayawelba Dawaï Hesed
        </div>
        """,
        height=50 
    )

if selected == "Traduction":
    # CODE TRANSLATE
    st.title(f"{selected}")
    st.markdown("Cette partie vous offre la possibilité de traduire vos **paragraphes** et vos **phrases**.")

    headers = {"Authorization": TOKEN_API}

    # Choose the translation language from Hugging Face
    translation_languages = {
        "English to German": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-de",
        "German to English": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-de-en",
        "English to French": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr",
        "French to English": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-en",
        "English to Spanish": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-es",
        "Spanish to English": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-es-en",
        "English to Chinese": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-zh",
        "Chinese to English": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-zh-en",
        # Add more language pairs as needed
    }

    selected_translation = st.selectbox("Sélectionner les langues", list(translation_languages.keys()))


    # Load the translation pipeline
    API_TRANSLATE=translation_languages[selected_translation]

    # User input for translation
    translate_input = st.text_area("Entrer le texte à traduire:", "")

    # Display loading indicator
    if st.button("Traduire"):
        with st.spinner("traduction..."):
            # Simulate translation delay for demonstration
            time.sleep(2)
            if translate_input:
                # Perform translation
                def main_translate(payload):
                    response = requests.post(API_TRANSLATE, headers=headers, json=payload)
                    return response.json()
                    
                output_translate = main_translate({
                    "inputs": translate_input
                })
                
                if not output_translate[0]["translation_text"]:
                    error_message = output_translate[0]["error"]
                    st.error(f"Le texte n'a pas pu être traduit: {error_message}")
                else:
                    translated_text = output_translate[0]["translation_text"]
                    st.success(f"Le texte tratuit: {translated_text}")
                
                #st.write("**TRADUCTION** is : {}".format(output[0]["translation_text"]))

                
            else:
                st.warning("Veuillez saisir le texte à traduire.")


    # Clear button to reset input and result
    if st.button("Nettoyer"):
        translate_input = ""
        st.success("Le champ est nettoyé.")
        st.empty()  # Clear previous results if any

    #END FOR TRANSLATE CODE
if selected == "Résumer":
    #CODE SUMMARIZE
    st.title(f"{selected}")

    st.markdown("Cette partie vous offre la possibilité de **Résumer** vos **paragraphes** et vos **phrases**.")

    headers = {"Authorization": TOKEN_API}

    # Load the 
    API_SUMMARY = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

    # User input for translation
    summary_input = st.text_area("Entrer le texte à Résumer:", "")
    if st.button("Résumer"):
        with st.spinner("Résume..."):
            # Simulate translation delay for demonstration
            time.sleep(2)
            if summary_input:
                def main1(payload):
                    response = requests.post(API_SUMMARY, headers=headers, json=payload)
                    return response.json()
                            
                output_summary = main1({"inputs": summary_input})
                summary_text = output_summary[0]["summary_text"]
                st.success(f"Résumé: {summary_text}")
            else:
                st.warning("Veuillez saisir le texte à résumer.")
    # Clear button to reset input and result
    if st.button("Nettoyer"):
        summary_input = ""
        st.success("Le champ est nettoyé.")
        st.empty()  # Clear previous results if any


    #END CODE SUMMARIZE
if selected == "Chatbot":
    # CODE TRANSLATE
    st.title(f"{selected}")
    st.markdown("Cette partie vous offre la possibilité de me poser vos **questions**.")

    headers = {"Authorization": TOKEN_API}

    # Choose the translation language from Hugging Face
    translation_models = {
        "English": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr",
        "French": "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-en",
    }
    selected_translation = st.selectbox("Sélectionner une langue", list(translation_models.keys()))
    # Load the 
    API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

    # User input for translation
    user_input = st.text_area("Pose se moi une question :", "")

    if (selected_translation=="French"):
        API_URL_1 = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-fr-en"
        API_URL_2 = "https://api-inference.huggingface.co/models/Helsinki-NLP/opus-mt-en-fr"
        # Display loading indicator
        if st.button("Recherche"):
            with st.spinner("Rechercher..."):
                # Simulate translation delay for demonstration
                time.sleep(2)
                if user_input:
                    def main(payload):
                        response = requests.post(API_URL_1, headers=headers, json=payload)
                        return response.json()
                        
                    output = main({"inputs": user_input})
                    text2 = output[0]["translation_text"]

                    if text2:
                        def main1(payload):
                            response = requests.post(API_URL, headers=headers, json=payload)
                            return response.json()
                            
                        output = main1({"inputs": text2})
                        text3 = output[0]["generated_text"]

                        if text3:
                            def main(payload):
                                response = requests.post(API_URL_2, headers=headers, json=payload)
                                return response.json()
                                
                            output = main({"inputs": text3})
                            generated_text = output[0]["translation_text"]
                    st.success(f"Réponse: {generated_text}")
                else:
                    st.warning("Veuillez saisir une question.")

    else :
        # Display loading indicator
        if st.button("Research"):
            with st.spinner("Researching..."):
                # Simulate translation delay for demonstration
                time.sleep(2)
                if user_input:
                    # Perform translation
                    def main(payload):
                        response = requests.post(API_URL, headers=headers, json=payload)
                        return response.json()
                        
                    output = main({
                        "inputs": user_input
                    })
                    generated_text = output[0]["generated_text"]
                    st.success(f"Response: {generated_text}")
                else:
                    st.warning("Please enter a question.")

    # Clear button to reset input and result
    if st.button("Nettoyer"):
        user_input = ""
        st.success("Le champ est nettoyé.")
        st.empty()  # Clear previous results if any

    # END CODE TRANSLATE
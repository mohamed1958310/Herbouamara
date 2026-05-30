import streamlit as st
import os
import json
from datetime import datetime
import base64

# Configuration de la page
st.set_page_config(
    page_title="Herbouamara - Pharmacopee Naturelle",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Gestion du theme ---
if "theme" not in st.session_state:
    st.session_state.theme = "clair"

def toggle_theme():
    st.session_state.theme = "sombre" if st.session_state.theme == "clair" else "clair"

# --- Gestion des commentaires ---
COMMENTS_FILE = "comments.json"

def load_comments():
    if os.path.exists(COMMENTS_FILE):
        with open(COMMENTS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_comments(comments):
    with open(COMMENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(comments, f, ensure_ascii=False, indent=2)

if "comments" not in st.session_state:
    st.session_state.comments = load_comments()

# --- Definition des couleurs selon le theme ---
if st.session_state.theme == "clair":
    bg_color = "#f0f2f6"
    card_bg = "#ffffff"
    text_color = "#1a1a1a"
    border_color = "#2d5a27"
    sidebar_bg = "#e8f0e8"
    input_bg = "#ffffff"
else:
    bg_color = "#1e1e1e"
    card_bg = "#2d2d2d"
    text_color = "#e0e0e0"
    border_color = "#5aae4f"
    sidebar_bg = "#252525"
    input_bg = "#3a3a3a"

# --- Fonction pour charger et afficher le logo ---
def afficher_logo():
    # Vérifier si le fichier logo existe
    logo_paths = ["logo-Herbouamara.jpg", "logo_Herbouamara.jpg", "logo.jpg"]
    logo_trouve = None
    for path in logo_paths:
        if os.path.exists(path):
            logo_trouve = path
            break
    
    if logo_trouve:
        st.image(logo_trouve, width=120)
    else:
        # Logo par défaut si fichier non trouvé
        st.image("https://cdn-icons.pnpng.flaticon.com/512/1995/1995573.png", width=100)
    
    # Texte du logo en arabe/français
    st.markdown("""
    <div style='text-align:center;'>
        <h2 style='color:#2d5a27; margin-bottom:0;'>🌿 بوعمارة</h2>
        <p style='font-size:14px; color:#5aae4f; margin-top:0;'>للاعشاب والتوابل</p>
        <p style='font-size:12px;'>Herbouamara - Herboristerie & Epices</p>
    </div>
    """, unsafe_allow_html=True)

# --- Fonction pour definir l'arriere-plan ---
def set_background(image_file):
    """Définit une image d'arrière-plan pour l'application"""
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            img_data = f.read()
        b64 = base64.b64encode(img_data).decode()
        bg_css = f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{b64}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
            background-repeat: no-repeat;
        }}
        /* Rendre le contenu lisible sur l'image de fond */
        [data-testid="stSidebar"] {{
            background-color: {sidebar_bg}CC;
        }}
        .stMarkdown, p, h1, h2, h3, h4 {{
            text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
        }}
        </style>
        """
        st.markdown(bg_css, unsafe_allow_html=True)

# --- Appliquer l'arriere-plan (si le fichier existe) ---
background_paths = ["background.jpg", "arriere-plan.jpg", "fond.jpg", "Herbouamara.jpg"]
for path in background_paths:
    if os.path.exists(path):
        set_background(path)
        break

# --- CSS personnalise ---
st.markdown(f"""
<style>
    /* Barre laterale */
    [data-testid="stSidebar"] {{
        background: linear-gradient(135deg, {sidebar_bg}, {border_color}20);
        border-right: 2px solid {border_color}40;
    }}
    
    /* Titre principal */
    .main-title {{
        color: {border_color};
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        padding: 20px;
        background: linear-gradient(135deg, {border_color}20, {bg_color}80);
        border-radius: 15px;
        backdrop-filter: blur(5px);
    }}
    
    /* Carte fiche plante */
    .fiche-card {{
        background-color: {card_bg}DD;
        backdrop-filter: blur(3px);
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid {border_color};
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        color: {text_color};
    }}
    
    /* Carte fonctionnalite */
    .feature-card {{
        background-color: {card_bg}DD;
        backdrop-filter: blur(3px);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin: 10px;
        color: {text_color};
        transition: transform 0.3s;
    }}
    .feature-card:hover {{
        transform: translateY(-5px);
    }}
    
    /* Carte commentaire */
    .comment-card {{
        background-color: {card_bg}DD;
        backdrop-filter: blur(3px);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 3px solid {border_color};
        color: {text_color};
    }}
    
    /* Pied de page */
    .footer {{
        text-align: center;
        padding: 20px;
        margin-top: 50px;
        border-top: 1px solid {border_color}40;
        font-size: 12px;
        color: {text_color}80;
        background-color: {bg_color}80;
        backdrop-filter: blur(5px);
        border-radius: 10px;
    }}
    
    /* Cadre localisation */
    .location-card {{
        background-color: {card_bg}DD;
        backdrop-filter: blur(3px);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin: 10px;
        color: {text_color};
    }}
    
    h1, h2, h3, h4 {{
        color: {border_color};
    }}
    
    p, li, .stMarkdown {{
        color: {text_color};
    }}
    
    input, textarea {{
        background-color: {input_bg};
        color: {text_color};
    }}
    
    /* Style pour les boutons */
    .stButton > button {{
        background-color: {border_color};
        color: white;
        border-radius: 20px;
        transition: 0.3s;
    }}
    .stButton > button:hover {{
        background-color: {border_color}CC;
        transform: scale(1.02);
    }}
</style>
""", unsafe_allow_html=True)

# --- Barre laterale avec logo ---
with st.sidebar:
    afficher_logo()
    st.markdown("---")
    
    # Menu de navigation
    menu = st.radio(
        "📚 Navigation",
        ["🏠 Accueil", "🌱 Catalogue", "🔍 Recherche", "💬 Commentaires", "📍 Localisation", "ℹ️ A propos", "📧 Contact"]
    )
    
    st.markdown("---")
    
    # Bouton theme
    if st.button("🌓 Changer de theme", use_container_width=True):
        toggle_theme()
        st.rerun()
    
    st.markdown("---")
    
    # Contact rapide
    st.markdown("### 📞 Contact")
    st.markdown("📧 bati2152@gmail.com")
    st.markdown("📱 +212 6 2321 2236")
    st.markdown("📍 Arroui, Nador, Maroc")
    
    st.markdown("---")
    
    # Statistiques
    nb_plantes = 154  # À remplacer par len(BASE_PLANTES) après définition
    st.metric("🌿 Plantes enregistrees", nb_plantes)

# --- Base de donnees des plantes ---
BASE_PLANTES = {
    "abricotier": {"partie": "noyaux", "proprietes": "Usage traditionnel des amandons, à manipuler avec précaution."},
    "acacia_senegal": {"partie": "gomme", "proprietes": "Émolliente, adoucissante, texturante (gomme arabique)."},
    "ail": {"partie": "poudre", "proprietes": "Antiseptique, hypotenseur, soutien circulatoire."},
    "ajwain": {"partie": "graines", "proprietes": "Carminatif puissant, digestif, antispasmodique."},
    "alchemille": {"partie": "feuilles", "proprietes": "Astringente, hémostatique, tonique utérin (bien-être féminin)."},
    "aloe_vera": {"partie": "resine", "proprietes": "Laxatif puissant, stimulant digestif (usage ponctuel)."},
    "amande_de_terre": {"partie": "tubercules", "proprietes": "Nutritif, énergétique, reminéralisant (souchet)."},
    "ammoniaque": {"partie": "résine", "proprietes": "Gomme-résine (Gomme ammoniaque) historiquement antispasmodique."},
    "anabasis": {"partie": "graines", "proprietes": "Plante saharienne, usages traditionnels spécifiques."},
    "aneth": {"partie": "graines", "proprietes": "Stimulant digestif, carminatif, favorise la lactation."},
    "anis_doux": {"partie": "graines", "proprietes": "Digestif, galactogène, expectorant léger."},
    "anis_vert": {"partie": "graines", "proprietes": "Antispasmodique, soulage les ballonnements, saveur douce."},
    "arroche_marine": {"partie": "feuilles", "proprietes": "Plante halophyte, riche en minéraux, laxative légère."},
    "asafoetida": {"partie": "résine", "proprietes": "Antispasmodique puissant, carminatif, odeur soufrée marquée."},
    "aurone": {"partie": "feuilles", "proprietes": "Tonique, emménagogue, vermifuge (proche de l'absinthe)."},
    "avoine": {"partie": "son", "proprietes": "Riche en fibres solubles, régulateur du transit et de la glycémie."},
    "badiane": {"partie": "Graines", "proprietes": "Anis étoilé. Antispasmodique, carminatif, antiviral (acide shikimique)."},
    "baobab": {"partie": "pulpe", "proprietes": "Très riche en vitamine C, antioxydante, anti-fatigue, prébiotique."},
    "benjoin": {"partie": "résine", "proprietes": "Antiseptique pulmonaire, cicatrisant, utilisé en fumigation."},
    "brocoli": {"partie": "graines", "proprietes": "Riche en glucoraphanine, détoxifiant hépatique, antioxydant."},
    "bruyere": {"partie": "sommités fleuries", "proprietes": "Antiseptique urinaire puissant, diurétique, sédative."},
    "bryone_dioïque": {"partie": "racines tuberculées", "proprietes": "Purgatif drastique, toxique, à manipuler avec extrême prudence."},
    "bunium_persicum": {"partie": "graines", "proprietes": "Souvent confondu avec la nigelle, stimule fortement l'immunité."},
    "cafe_vert": {"partie": "graines", "proprietes": "Brûle-graisse, stimulant physique et mental, antioxydant."},
    "camomille": {"partie": "fleurs", "proprietes": "Calmante, anti-inflammatoire, antispasmodique, digestive."},
    "camphre": {"partie": "cristaux", "proprietes": "Analgésique local, stimulant respiratoire, antiseptique."},
    "caneficier": {"partie": "fruits", "proprietes": "Casse officinale. Laxatif doux, rafraîchissant."},
    "cannelle": {"partie": "batons", "proprietes": "Stimulante générale, antiseptique, régulatrice de la glycémie."},
    "caprier": {"partie": "graines", "proprietes": "Usage traditionnel, tonique amer, protecteur hépatique."},
    "cardamome": {"partie": "graines", "proprietes": "Digestive, carminative, anti-acide, rafraîchit l'haleine."},
    "carline": {"partie": "rhizome", "proprietes": "Sudorifique, digestive, autrefois utilisée comme tonique amer."},
    "carotte": {"partie": "graines", "proprietes": "Régénératrice hépatique, tonique cutanée, détoxifiante."},
    "carthame": {"partie": "pétales", "proprietes": "Faux safran. Émollient, purgatif léger, stimule la circulation."},
    "carvi": {"partie": "graines", "proprietes": "Le plus puissant des carminatifs, active la digestion, anti-gaz."},
    "celeri": {"partie": "graines", "proprietes": "Diurétique puissant, draineur de l'acide urique (goutte)."},
    "chamaecrista_absus": {"partie": "graines et feuilles", "proprietes": "Plante traditionnelle (Chasme), usages ophtalmiques traditionnels."},
    "champignon_noir": {"partie": "séchés", "proprietes": "Fluidifiant sanguin léger, nutritif, immunomodulateur."},
    "chanvre": {"partie": "graines", "proprietes": "Chènevis. Riche en oméga-3 et protéines équilibrées."},
    "chardon_marie": {"partie": "graines", "proprietes": "Hépatoprotecteur majeur (silymarine), régénère le foie."},
    "chataigne_de_terre": {"partie": "tubercules", "proprietes": "Tubercules comestibles (châtaigne de terre), tonique digestif."},
    "chia": {"partie": "graines", "proprietes": "Mucilagineuse, laxative de lest, riche en acides gras essentiels."},
    "coloquinte_vraie": {"partie": "fruit", "proprietes": "Purgatif violent, toxique à forte dose, usage très restreint."},
    "cordyceps": {"partie": "champignon", "proprietes": "Adaptogène, augmente l'énergie physique, l'oxygénation et la libido."},
    "coriande": {"partie": "graines", "proprietes": "Digestive, chélateur léger des métaux lourds, carminative."},
    "cressonette": {"partie": "graines", "proprietes": "Alénois. Dépurative, stimulante, riche en composés soufrés."},
    "criniere_du_lion": {"partie": "Champignon", "proprietes": "Hericium. Stimule le système nerveux, mémoire, neuroprotecteur."},
    "cubebe": {"partie": "graines", "proprietes": "Poivre à queue. Antiseptique urinaire et respiratoire, digestif."},
    "cumin": {"partie": "graines", "proprietes": "Digestif, réchauffant, réduit les fermentations intestinales."},
    "cumin_laine": {"partie": "graines", "proprietes": "Cumin du Maroc. Spécifique des troubles digestifs et des spasmes."},
    "curcuma": {"partie": "rhizomes", "proprietes": "Anti-inflammatoire puissant, antioxydant, protecteur hépatique."},
    "cyperus": {"partie": "tubercules", "proprietes": "Souchet / Nagarmotha. Encre-anti-inflammatoire, régulateur du cycle."},
    "daghmous": {"partie": "miel", "proprietes": "Miel d'euphorbe. Réchauffant, actif contre les maux de gorge et kystes."},
    "dauphinelle": {"partie": "graines", "proprietes": "Staphisaigre. Usage externe uniquement (anti-poux), très toxique."},
    "djansang": {"partie": "graines", "proprietes": "Akpi. Graines oléagineuses, nutritives, fortifiantes."},
    "entada_pursaetha": {"partie": "graines", "proprietes": "Graine de rêve. Usage traditionnel pour le sommeil et les douleurs."},
    "ephedra": {"partie": "tiges", "proprietes": "Stimulant cardiaque et respiratoire puissant (éphédrine). Réglementé."},
    "epimedium": {"partie": "feuilles", "proprietes": "Herbe au bouc capricieux. Aphrodisiaque, tonique de l'énergie rein."},
    "epine_vinette": {"partie": "écorces", "proprietes": "Contient de la berbérine. Tonique amer, draineur hépato-biliaire."},
    "euphorbe_a_cornes_en_faucille": {"partie": "feuilles", "proprietes": "Usage traditionnel très ciblé, latex irritant."},
    "fabagelle": {"partie": "feuilles", "proprietes": "Faux-caprier. Utilisée traditionnellement pour les troubles articulaires."},
    "fenouil": {"partie": "graines", "proprietes": "Antispasmodique, soulage les coliques, favorise la montée de lait."},
    "fenugrec": {"partie": "graines", "proprietes": "Apéritif (ouvre l'appétit), anabolisant naturel, régule l'insuline."},
    "fenugrec_rouge": {"partie": "graines", "proprietes": "Variété spécifique, fortifiante et stimulante métabolique."},
    "frene": {"partie": "graines", "proprietes": "Diurétique, anti-inflammatoire (rhumatismes, gou-te)."},
    "galanga": {"partie": "rhizome", "proprietes": "Tonique général, aphrodisiaque, digestif, anti-nausée."},
    "garance": {"partie": "racines", "proprietes": "Colorant naturel, historiquement diurétique et lithontriptique."},
    "gattilier": {"partie": "graines", "proprietes": "Régulateur hormonal féminin (progestérone-like), syndrome prémenstruel."},
    "gelee_royale": {"partie": "Gelée", "proprietes": "Revitalisant majeur, immunostimulant, concentré nutritif."},
    "genievre": {"partie": "feuilles", "proprietes": "Rameaux/feuilles diurétiques et antiseptiques urinaires."},
    "germandree": {"partie": "feuilles", "proprietes": "Tonique amer, digestive, à utiliser avec modération (foie)."},
    "gingembre": {"partie": "rhizome", "proprietes": "Anti-nauséeux, dynamisant, anti-inflammatoire, réchauffant."},
    "ginkgo": {"partie": "feuilles", "proprietes": "Activateur de la circulation cérébrale et périphérique, mémoire."},
    "ginseng": {"partie": "rhizome", "proprietes": "Adaptogène majeur, tonique vital (Qi), résistance au stress."},
    "giroflier": {"partie": "clous", "proprietes": "Antiseptique et antibactérien puissant, antalgique dentaire majeur."},
    "goji": {"partie": "baies", "proprietes": "Antioxydant puissant, protecteur oculaire, fortifiant général."},
    "gombo": {"partie": "graines", "proprietes": "Riches en protéines, régulatrices de la glycémie."},
    "goyavier": {"partie": "feuilles", "proprietes": "Anti-diarrhéique puissant, astringent, antiseptique buccal."},
    "griffe_de_chat": {"partie": "feuilles", "proprietes": "Uncaria tomentosa. Immunostimulante, anti-inflammatoire articulaire."},
    "guarana": {"partie": "graines", "proprietes": "Riche en caféine à libération lente, brûle-graisse, anti-fatigue."},
    "herniaire": {"partie": "feuilles", "proprietes": "Herbe à la rupture. Diurétique, prévient les calculs rénaux."},
    "jojoba": {"partie": "graines", "proprietes": "Donne une cire liquide hautement protectrice pour la peau et les cheveux."},
    "karkade": {"partie": "fleurs", "proprietes": "Hibiscus. Rafraîchissant, hypotenseur léger, riche en antioxydants."},
    "laitue": {"partie": "graines", "proprietes": "Calmantes, sédatives légères, réduisent l'anxiété."},
    "laurier": {"partie": "feuilles", "proprietes": "Antiseptique, digestif, antirhumatismal (en friction)."},
    "lavande": {"partie": "sommités fleuries", "proprietes": "Calmante nerveuse, cicatrisante, antispasmodique."},
    "lentille_batarde": {"partie": "graines", "proprietes": "Usage nutritionnel et traditionnel spécifique."},
    "lentille_rouge": {"partie": "graines", "proprietes": "Très digeste, riche en fer et en protéines végétales."},
    "lentisque_pistachier": {"partie": "résine/feuilles", "proprietes": "Décongestionnant veineux et lymphatique majeur."},
    "lin": {"partie": "graines", "proprietes": "Mucilage laxatif (si trempées), source majeure d'Oméga-3."},
    "lupin": {"partie": "graines", "proprietes": "Riche en protéines, hypoglycémiant léger."},
    "maca": {"partie": "tubercules", "proprietes": "Ginseng péruvien. Énergétique, fertilité, équilibre hormonal."},
    "macis": {"partie": "arille", "proprietes": "Enveloppe de la muscade. Stimulant digestif, carminatif fin."},
    "mahaleb": {"partie": "noyaux", "proprietes": "Bois de Sainte-Lucie. Aromatique, calmant traditionnel."},
    "maniguette": {"partie": "graines", "proprietes": "Graine de paradis. Stimulante, réchauffante, digestive."},
    "marjolaine": {"partie": "feuilles", "proprietes": "Calmante du système nerveux, régulatrice cardiaque, digestive."},
    "marrube_blanc": {"partie": "feuilles", "proprietes": "Expectorant majeur, fluidifiant bronchique, tonique amer."},
    "menthe": {"partie": "feuilles", "proprietes": "Digestive, rafraîchissante, anti-spasmodique, anti-nausée."},
    "millepertuis": {"partie": "sommités", "proprietes": "Antidépresseur naturel (troubles légers à modérés), cicatrisant."},
    "millet": {"partie": "graines", "proprietes": "Reminéralisant, excellent pour la beauté des cheveux et des ongles."},
    "moringa": {"partie": "graines et feuilles", "proprietes": "Arbre de vie. Super-aliment, hautement nutritif, antianémique."},
    "moutarde": {"partie": "graines", "proprietes": "Rubéfiante (en cataplasme/synapisme) pour décongestionner les bronches."},
    "murier": {"partie": "feuilles", "proprietes": "Hypoglycémiant majeur (limite l'absorption des sucres)."},
    "myrrhe": {"partie": "résine", "proprietes": "Antiseptique puissant des muqueuses (bouche/gorge), cicatrisante."},
    "myrte ": {"partie": "feuilles", "proprietes": "Antiseptique respiratoire et urinaire, tonique cutané."},
    "navet": {"partie": "graines", "proprietes": "Usage traditionnel, draineur pulmonaire léger."},
    "nerprun_alaterne": {"partie": "feuilles", "proprietes": "Laxatif, draineur hépato-biliaire (à utiliser avec parcimonie)."},
    "nigelle": {"partie": "graines", "proprietes": "Habba sawda. Immunostimulante, antihistaminique (anti-allergie)."},
    "noix_de_muscade": {"partie": "noix", "proprietes": "Analgésique nerveuse, digestive, narcotique à forte dose."},
    "oignon": {"partie": "poudre et graines", "proprietes": "Antibactérien, protecteur cardiovasculaire, hypoglycémiant."},
    "oliban": {"partie": "résines", "proprietes": "Encens. Anti-inflammatoire puissant (Boswellia), calme l'esprit."},
    "ortie": {"partie": "feuilles et graines", "proprietes": "Reminéralisante majeure (feuilles), anti-prostatique (racines/graines)."},
    "paprika": {"partie": "poudre", "proprietes": "Riche en vitamine C, stimulant circulatoire et digestif."},
    "passiflore": {"partie": "feuilles", "proprietes": "Anxiolytique, inducteur du sommeil, calme la rumination mentale."},
    "pegane": {"partie": "graines", "proprietes": "Harmal. Plante sacrée/médicinale, contient des alcaloïdes (IMAO). Attention."},
    "peppermint": {"partie": "feuilles", "proprietes": "Menthe poivrée. Tonique, anti-migraineuse, digestive rapide."},
    "persil": {"partie": "graines", "proprietes": "Diurétique puissant, emménagogue (stimule les règles)."},
    "pippali": {"partie": "graines", "proprietes": "Poivre long. Réchauffant, augmente la biodisponibilité des plantes."},
    "poivre_noire": {"partie": "graines", "proprietes": "Stimulant digestif, anti-inflammatoire (associé au curcuma)."},
    "pollen": {"partie": "graines", "proprietes": "Éléments reproducteurs. Fortifiant, protecteur de la prostate."},
    "propolis": {"partie": "resines", "proprietes": "Antibiotique et antifongique naturel produit par les abeilles."},
    "psyllium": {"partie": "graines et son", "proprietes": "Laxatif de lest idéal (régule constipation ET diarrhée)."},
    "pyrethre_d'afrique": {"partie": "racines", "proprietes": "Sialagogue (fait saliver), stimule les nerfs faciaux, névralgies."},
    "quinoa": {"partie": "graines", "proprietes": "Pseudo-céréale sans gluten, hautement protéinée et digeste."},
    "radis": {"partie": "graines", "proprietes": "Draineur hépatique et rénal, aide à éliminer les toxines."},
    "ratanhia": {"partie": "racines", "proprietes": "Astringent ultra-puissant, hémostatique, idéal pour les gencives."},
    "reglisse": {"partie": "racines et poudre ", "proprietes": "Anti-ulcéreuse gastrique, anti-inflammatoire, hypertensive."},
    "reishi": {"partie": "poudre", "proprietes": "Champignon de longue vie. Adaptogène, modulateur de l'immunité."},
    "rhubarbe": {"partie": "feuilles", "proprietes": "Attention : les feuilles sont toxiques (acide oxalique). Seule la racine s'utilise."},
    "romarin": {"partie": "feuilles", "proprietes": "Protecteur du foie, tonique du matin, antioxydant majeur."},
    "roquette": {"partie": "graines", "proprietes": "Stimulante, aphrodisiaque traditionnelle, tonique capillaire."},
    "rose": {"partie": "boutons", "proprietes": "Adoucissante, astringente légère, réconfortante émotionnelle."},
    "rose_de_jericho": {"partie": "plante", "proprietes": "Chajarat Maryam. Utilisée pour faciliter l'accouchement et la fertilité."},
    "rue": {"partie": "feuilles", "proprietes": "Emménagogue puissante, abortive à forte dose. À manier avec recul."},
    "safed_musli": {"partie": "racines", "proprietes": "Plante ayurvédique. Tonique sexuel, adaptogène, fortifiant vital."},
    "safrane": {"partie": "stigmates", "proprietes": "Safran. Régulateur de l'humeur (sérotonine-like), antidépresseur."},
    "sarrasin": {"partie": "graines", "proprietes": "Riche en rutine (protecteur des capillaires sanguins), sans gluten."},
    "sauge": {"partie": "feuilles", "proprietes": "Estrogen-like, régule la transpiration et les bouffées de chaleur."},
    "sene": {"partie": "feuilles", "proprietes": "Laxatif stimulant puissant (anthraquinones). Usage court uniquement."},
    "sesame": {"partie": "graines", "proprietes": "Riche en calcium et magnésium, émollient, nutritif nerveux."},
    "shilajit": {"partie": "poix minérale", "proprietes": "Concentré d'acide fulvique et minéraux, revitalisant universel."},
    "soja": {"partie": "graines", "proprietes": "Riche en isoflavones (phytoestrogènes), trouble de la ménopause."},
    "spiruline": {"partie": "poudre", "proprietes": "Cyanobactérie. Super-aliment, riche en fer, protéines et phycocyanine."},
    "sumac": {"partie": "graines", "proprietes": "Antioxidant, digestif, acidulé, régulateur de la glycémie."},
    "telephium_d'imperato": {"partie": "racines", "proprietes": "Usage traditionnel rare, vulnéraire (cicatrisant)."},
    "tetraclinis": {"partie": "feuilles et resines", "proprietes": "Sandaraque. Résine pour fumigations antiseptiques et vernis."},
    "thym": {"partie": "feuilles", "proprietes": "Anti-infectieux majeur, antiviral, expectorant, immunostimulant."},
    "thymelaea": {"partie": "feuilles", "proprietes": "Mithnan. Plante médicinale traditionnelle, purgative drastique."},
    "tilleul": {"partie": "feuilles", "proprietes": "Calmant, sédatif léger, fébrifuge (provoque la sueur en cas de fièvre)."},
    "tongkat_ali": {"partie": "racines", "proprietes": "Stimulant de la testostérone libre, tonique masculin, vigueur."},
    "tragacath": {"partie": "gomme", "proprietes": "Gomme adragante. Émolliente, gélifiante naturelle, protectrice."},
    "tribule_terrestre": {"partie": "graines", "proprietes": "Tribulus. Augmente l'endurance, stimule la libido (hommes/femmes)."},
    "valeriane": {"partie": "racines", "proprietes": "Valium naturel. Calme l'anxiété, favorise un sommeil profond."},
    "verveine": {"partie": "feuilles", "proprietes": "Digestive, sédative légère, anti-stress après le repas."},
    "vinaigre_de_cidre": {"partie": "vinaigre", "proprietes": "Régulateur d'acidité gastrique, draineur, aide à la perte de poids."}
}

# Dossier des photos
DOSSIER_PHOTOS = "photos"
if not os.path.exists(DOSSIER_PHOTOS):
    os.makedirs(DOSSIER_PHOTOS)

def trouver_photo(nom_plante):
    extensions = ['.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG']
    for ext in extensions:
        chemin = os.path.join(DOSSIER_PHOTOS, nom_plante + ext)
        if os.path.exists(chemin):
            return chemin
        chemin = os.path.join(DOSSIER_PHOTOS, nom_plante.lower() + ext)
        if os.path.exists(chemin):
            return chemin
    return None

# ========== PAGES ==========

# --- PAGE ACCUEIL ---
if menu == "🏠 Accueil":
    st.markdown('<div class="main-title">🌿 Herbouamara - Pharmacopee Naturelle</div>', unsafe_allow_html=True)
    
    st.markdown("""
    <div style='text-align:center; margin-bottom:40px;'>
        <p style='font-size:20px; font-weight:bold;'>بوعمارة - للاعشاب والتوابل</p>
        <p style='font-size:18px;'>Bienvenue dans Herbouamara, votre encyclopedie naturelle des plantes medicinales.</p>
        <p>Decouvrez les proprietes, usages et vertus des plantes pour votre bien-etre.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    for col, title, desc in zip([col1, col2, col3, col4],
                                 ["150+ Plantes", "Fiches detaillees", "Recherche avancee", "Galerie photos"],
                                 ["Base complete des plantes", "Proprietes et usages", "Trouvez rapidement", "Visualisez en image"]):
        with col:
            st.markdown(f"<div class='feature-card'><h3>🌿</h3><h4>{title}</h4><p>{desc}</p></div>", unsafe_allow_html=True)

# --- PAGE CATALOGUE ---
elif menu == "🌱 Catalogue":
    st.markdown('<div class="main-title">🌱 Catalogue des plantes</div>', unsafe_allow_html=True)
    for plante in sorted(BASE_PLANTES.keys()):
        with st.expander(f"🌿 {plante.capitalize()}"):
            info = BASE_PLANTES[plante]
            st.markdown(f"**Partie utilisee :** {info['partie']}")
            st.markdown(f"**Proprietes :** {info['proprietes']}")
            photo = trouver_photo(plante)
            if photo:
                st.image(photo, width=200)

# --- PAGE RECHERCHE ---
elif menu == "🔍 Recherche":
    st.markdown('<div class="main-title">🔍 Recherche avancee</div>', unsafe_allow_html=True)
    recherche = st.text_input("Rechercher par nom, propriete ou usage :")
    if recherche:
        resultats = [p for p, info in BASE_PLANTES.items() 
                    if recherche.lower() in p.lower() or recherche.lower() in info["proprietes"].lower()]
        if resultats:
            for plante in resultats:
                st.markdown(f"### 🌿 {plante.capitalize()}")
                st.markdown(f"**{BASE_PLANTES[plante]['proprietes']}**")
        else:
            st.warning("Aucun resultat")

# --- PAGE COMMENTAIRES ---
elif menu == "💬 Commentaires":
    st.markdown('<div class="main-title">💬 Espace commentaires</div>', unsafe_allow_html=True)
    
    with st.form("comment_form"):
        nom = st.text_input("Votre nom")
        commentaire = st.text_area("Votre commentaire", height=100)
        note = st.slider("Note (1-5)", 1, 5, 5)
        submitted = st.form_submit_button("Publier")
        if submitted and nom and commentaire:
            nouveau_comment = {
                "nom": nom,
                "commentaire": commentaire,
                "note": note,
                "date": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "avatar": "🌿"
            }
            st.session_state.comments.insert(0, nouveau_comment)
            save_comments(st.session_state.comments)
            st.success("Commentaire ajoute !")
            st.rerun()
    
    st.markdown("### 📝 Commentaires des visiteurs")
    for c in st.session_state.comments:
        st.markdown(f"""
        <div class='comment-card'>
            <b>{c['avatar']} {c['nom']}</b> 
            <span style='font-size:12px; color:gray;'>{c['date']}</span>
            <br>{'⭐' * c['note']}
            <p>{c['commentaire']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    if not st.session_state.comments:
        st.info("Soyez le premier a laisser un commentaire !")

# --- PAGE LOCALISATION ---
elif menu == "📍 Localisation":
    st.markdown('<div class="main-title">📍 Notre localisation</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class='location-card'>
            <h3>🏠 Adresse</h3>
            <p><b>Herbouamara - بوعمارة</b></p>
            <p>Arroui, Nador</p>
            <p>Maroc</p>
            <hr>
            <h3>📞 Contact</h3>
            <p>📧 bati2152@gmail.com</p>
            <p>📱 +212 6 2321 2236</p>
            <hr>
            <h3>🕒 Horaires</h3>
            <p>Lundi - Vendredi: 9h - 18h</p>
            <p>Samedi: 10h - 14h</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='location-card'>
            <h3>🗺️ Plan d'acces</h3>
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d25888.51193080067!2d-2.9469701!3d35.0894161!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0xd0c7d4f5b6b6b6b%3A0x0!2sNador!5e0!3m2!1sfr!2sma!4v1700000000000!5m2!1sfr!2sma" 
                width="100%" 
                height="300" 
                style="border:0; border-radius:10px;" 
                allowfullscreen="" 
                loading="lazy">
            </iframe>
            <p style='margin-top:10px;'><i>Arroui, Nador - Province de Nador, Maroc</i></p>
        </div>
        """, unsafe_allow_html=True)

# --- PAGE A PROPOS ---
elif menu == "ℹ️ A propos":
    st.markdown('<div class="main-title">ℹ️ A propos de Herbouamara</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class='fiche-card'>
        <h3>🌿 Notre mission</h3>
        <p><b>Herbouamara - بوعمارة</b> est une plateforme dediee a la valorisation du patrimoine naturel et medicinal.</p>
        
        <h3>📚 Ce que nous offrons :</h3>
        <ul>
            <li>Base de donnees de plantes medicinales</li>
            <li>Fiches detaillees sur les proprietes et usages</li>
            <li>Illustrations pour chaque plante</li>
            <li>Espace d'echange et commentaires</li>
        </ul>
        
        <h3>🌍 Sources :</h3>
        <ul>
            <li>Pharmacopee traditionnelle</li>
            <li>Recherches scientifiques</li>
            <li>Ethnobotanique marocaine</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- PAGE CONTACT ---
elif menu == "📧 Contact":
    st.markdown('<div class="main-title">📧 Contactez Herbouamara</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        with st.form("contact_form"):
            nom = st.text_input("Votre nom")
            email = st.text_input("Votre email")
            message = st.text_area("Message", height=150)
            if st.form_submit_button("Envoyer"):
                st.success("Message envoye ! Nous vous repondrons rapidement.")
    
    with col2:
        st.markdown("""
        <div class='location-card'>
            <h3>📱 Nous contacter</h3>
            <p><b>Herbouamara - بوعمارة</b></p>
            <p><b>Email :</b> bati2152@gmail.com</p>
            <p><b>Telephone :</b> +212 6 2321 2236</p>
            <p><b>Adresse :</b> Arroui, Nador, Maroc</p>
        </div>
        """, unsafe_allow_html=True)

# --- Pied de page ---
st.markdown(f"""
<div class='footer'>
    <p>🌿 Herbouamara - بوعمارة | للاعشاب والتوابل © 2024</p>
    <p>📍 Arroui, Nador, Maroc | 📧 bati2152@gmail.com | 📱 +212 6 2321 2236</p>
    <p>Mise a jour : {datetime.now().strftime('%d/%m/%Y')}</p>
</div>
""", unsafe_allow_html=True)
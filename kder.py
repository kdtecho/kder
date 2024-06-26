import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

# Set page config with a new icon related to IT
st.set_page_config(page_title="Kader Belem", page_icon="💻", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://lottie.host/d4b66f91-c56e-4055-8ab3-c74f425fcf51/w8r6sCmQyU.json")
lottie_web_dev = load_lottieurl("https://lottie.host/f0baeaa2-40b1-4638-8911-85ef66e3336b/c7GYPkIOlK.json")  # Web Development
lottie_marketing = load_lottieurl("https://lottie.host/4bde2a2e-2590-4583-8038-7650c6e836e4/pjp9A6QeRy.json")  # Marketing
lottie_business_dev = load_lottieurl("https://lottie.host/d0218bcf-ea2f-44d0-9c56-f7c52d4ecbed/5rzSlHpzTR.json")  # Business Development

# Check if animations loaded correctly
if lottie_coding is None:
    st.error("Failed to load coding animation.")
if lottie_web_dev is None:
    st.error("Failed to load web development animation.")
if lottie_marketing is None:
    st.error("Failed to load marketing animation.")
if lottie_business_dev is None:
    st.error("Failed to load business development animation.")

img_contact_form = Image.open("images/calculatrice.png")
img_lottie_animation = Image.open("images/librairie.png")
img_third_image = Image.open("images/jdv.png")  # Load the third image

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hello, Je suis Kader Belem 💻")
    st.title("Etudiant,")
    st.write(
        """
        Kader Belem est un étudiant ............................................................., 
        .......................................................................................... 
        .............................................................................................................. 
        .............................................................................................................. 
        ........................................................................................., 
        ........................................................................
        """
    )
    st.write("[Plus d'informations >][Linkedin >](https://www.linkedin.com/in/vicky-percy-63a666209?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)")

# ---- COMPETENCES ACQUISES ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Compétences acquises")
        st.write("##")
        st.write(
            """
            Compétences acquises:
            - ............................................................................................
            - ............................................................................................
            
            ..............................................................................................

            .............................................................................................. 
            ..............................................................................................
            """
        )
        st.write("[Linkedin >](https://www.linkedin.com/in/vicky-percy-63a666209?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app)")
    with right_column:
        if lottie_coding:
            st_lottie(lottie_coding, height=300, key="coding")

# ---- CE QUE JE FAIS ----
with st.container():
    st.write("---")
    st.header("Veille informatique")
    st.write("##")
    st.write(
        """
        Voici quelques-uns des services que je propose:
        - .....................................................................................
        - .....................................................................................
        - .....................................................................................

        .......................................................................................
        """
    )
    left_column, right_column = st.columns(2)
    with left_column:
        if lottie_web_dev:
            st_lottie(lottie_web_dev, height=300, key="web_dev")
    with right_column:
        if lottie_marketing:
            st_lottie(lottie_marketing, height=300, key="marketing")

# ---- MES PROJETS ----
with st.container():
    st.write("---")
    st.header("Mes Projets")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Contatez moi")
        st.write(
            """
            Si vous avez besoin de mes services, n'hésitez pas à me contacter.!
            Je suis disponible pour discuter de vos projets et trouver des solutions adaptées à vos besoins.
            Sur ce site, Vous verrez nos service et prestations, vous pouvez demandez un devis gratuit
            """
        )
        st.markdown("[Devis gratuit...](https://aubeproprete-services.fr/demande-de-devis/)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Demandez un devis gratuit pour vos projets de nettoyage")
        st.write(
            """
            Si vous avez besoin d'un devis de nettoyage pour tout type de projet, 
            n'hésitez pas à me contacter. Je suis à votre disposition pour vous fournir des solutions sur mesure adaptées à vos besoins..
            """
        )
        st.markdown("[Devis gratuit...](https://www.aubenet.fr/contactez-nous)")

# ---- THIRD IMAGE SECTION ----
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_third_image)  # Display the third image
    with text_column:
        st.subheader("Third Image Title")
        st.write(
            """
            Description for the third image. 
            Provide information or context related to the image.
            """
        )
        st.markdown("[Link related to the third image](https://example.com)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Contactez-moi!")
    st.write("##")

    # Documentation: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mickaelvp8@GMAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        if lottie_business_dev:
            st_lottie(lottie_business_dev, height=300, key="business_dev")

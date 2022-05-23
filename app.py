import streamlit as st
from slugify import slugify
import png
import pyqrcode
from pyqrcode import QRCode
from PIL import Image
from time import sleep
st.title('Campaign QR')

url_de = st.sidebar.text_input("German URL", value="vitreo.me", placeholder="vitreo.me")
url_en = st.sidebar.text_input("English URL", value="vitreo.me/en", placeholder="vitreo.me/en")

source = slugify(st.sidebar.text_input("Source", value="tradefair", placeholder="Ex: tradefair, directcontact, linkedin, salesmail, mailchip -- main source"))
medium = slugify(st.sidebar.text_input("Medium", value="postcard", placeholder="postcard, flyer, email, businesscard, display, social -- Where is this URL going to be used?"))
name = slugify(st.sidebar.text_input("Name", value="prowein2022", placeholder="prowein2022, chemspec -- Name of the campaign"))

qr_size = st.sidebar.slider('QR Code Size', min_value = 6, max_value = 12, value = 10)

full_url_de = url_de + "?utm_source=" + source + "&utm_medium=" + medium + "&utm_campaign=" + name
full_url_en = url_en + "?utm_source=" + source + "&utm_medium=" + medium + "&utm_campaign=" + name




# Generate QR code
qr_de = pyqrcode.create(full_url_de)
qr_en = pyqrcode.create(full_url_en)

qr_fname_en = 'en_vit-'+source+'_'+medium+'_'+name+'.png'
qr_fname_de = 'de_vit-'+source+'_'+medium+'_'+name+'.png'

#st.write(qr_fname_en)
#st.write(qr_fname_de)

qr_de.png(qr_fname_de, scale = qr_size)
qr_en.png(qr_fname_en, scale = qr_size)

sleep(1)
image_en = Image.open(qr_fname_de)
image_de = Image.open(qr_fname_en)
 
st.markdown("**Campaign QR Code**")
st.markdown('Streamlit is **_really_ cool**.')
st.text("Campaign URL for english site:")
st.write(full_url_en)
st.image(image_en,caption="Right Click and then Save Image As...")

st.text("Campaign URL for German site:")
st.write(full_url_de)
st.image(image_de,caption="Right Click and then Save Image As...")

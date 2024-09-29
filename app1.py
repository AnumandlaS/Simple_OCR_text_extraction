import streamlit as st
import cv2
from preprocessing import grayscale, noise_removal, thick_font, deskew
from pytesseract import image_to_string
from PIL import Image
import numpy as np
import re
from preprocessing import extract_text

def highlight_text(text, search_term):
    highlighted = re.sub(f'({re.escape(search_term)})', r'<span style="background-color: yellow;">\1</span>', text, flags=re.IGNORECASE)
    return highlighted

# Streamlit UI
st.title("OCR Text Extractor")

# Language selection
language = st.selectbox("Select Language", ["English", "Hindi"])

# File upload
uploaded_file = st.file_uploader("Upload an image for OCR", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Load the image
    image = Image.open(uploaded_file)
    

    # Convert the image to RGB format if it is in grayscale or other modes
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    image_path = "temp/uploaded_image.png"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    image = np.array(image)
    # Extract text based on selected language
    # Call your extract_text function
    # Extract text based on selected language
    
    extracted_text = extract_text(image_path, language)


    # Preprocess the image
    # gray_image = grayscale(image)
    # no_noise_image = noise_removal(gray_image)
    # thickened_image = thick_font(no_noise_image)
    #deskewed_image = deskew(thickened_image)

    # Extract text using Tesseract
    #extracted_text = image_to_string(image)

    # Display the extracted text
    st.subheader("Extracted Text:")
    st.text(extracted_text)
# Search option
    search_term = st.text_input("Search for a word:")

    if search_term:
        highlighted_text = highlight_text(extracted_text, search_term)
        st.markdown(highlighted_text, unsafe_allow_html=True)
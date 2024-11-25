import streamlit as st
from PIL import Image
import io
import os

# Cache the uploaded PDFs
@st.cache_data
def cache_uploaded_pdfs(pdf1, pdf2, pdf3):
    return pdf1, pdf2, pdf3

# Function to display PDFs side by side
def display_pdfs(pdf1, pdf2, pdf3):
    # Open the PDFs using PIL
    img1 = Image.open(io.BytesIO(pdf1))
    img2 = Image.open(io.BytesIO(pdf2))
    img3 = Image.open(io.BytesIO(pdf3))

    # Resize the images to fit side by side
    max_width = 800
    max_height = 600
    img1 = img1.resize((max_width//3, max_height))
    img2 = img2.resize((max_width//3, max_height))
    img3 = img3.resize((max_width//3, max_height))

    # Display the images side by side
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(img1)
    with col2:
        st.image(img2)
    with col3:
        st.image(img3)

# Main app
st.title("PDF Viewer")

# Upload PDFs
uploaded_pdf1 = st.file_uploader("Upload PDF 1", type=["pdf"])
uploaded_pdf2 = st.file_uploader("Upload PDF 2", type=["pdf"])
uploaded_pdf3 = st.file_uploader("Upload PDF 3", type=["pdf"])

# Cache the uploaded PDFs
if uploaded_pdf1 and uploaded_pdf2 and uploaded_pdf3:
    pdf1, pdf2, pdf3 = cache_uploaded_pdfs(uploaded_pdf1.read(), uploaded_pdf2.read(), uploaded_pdf3.read())
    display_pdfs(pdf1, pdf2, pdf3)
else:
    st.write("Please upload all three PDFs")
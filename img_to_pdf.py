import streamlit as st
from PIL import Image
from PyPDF2 import PdfMerger
from io import BytesIO
import time

# Set page title and description
st.set_page_config(page_title="Image to PDF Generator", layout="centered")

# Function to convert images to PDF
def convert_images_to_pdf(images):
    merger = PdfMerger()
    temp_files = []

    for img in images:
        img_bytes = img.read()  # Read the BytesIO object
        image = Image.open(BytesIO(img_bytes))

        pdf_bytes = BytesIO()
        image.save(pdf_bytes, format="PDF")
        pdf_bytes.seek(0)

        temp_files.append(pdf_bytes)

        merger.append(pdf_bytes)

    output_pdf = BytesIO()
    merger.write(output_pdf)

    for temp_file in temp_files:
        temp_file.close()

    return output_pdf

# Main function for the Streamlit app
def main():
    st.title("Image to PDF Generator")

    uploaded_files = st.file_uploader("Upload images to generate PDF. Youcan select multiple images.", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

    if uploaded_files is not None:
        st.write("Images uploaded successfully!")
        st.write("Generating PDF...")

        pdf_file = convert_images_to_pdf(uploaded_files)

        # Create a download link for the generated PDF file
        st.download_button(
            label="Download PDF File",
            data=pdf_file,
            file_name="generated_pdf.pdf",
            mime="application/pdf",
        )

if __name__ == "__main__":
    main()

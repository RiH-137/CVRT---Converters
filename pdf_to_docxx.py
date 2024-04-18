import streamlit as st
from pdf2docx import Converter
from io import BytesIO

st.title("PDF to DOCX Converter")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    with st.spinner('Converting PDF to DOCX...'):
        # Convert PDF to DOCX
        pdf_data = uploaded_file.read()
        pdf_stream = BytesIO(pdf_data)
        docx_stream = BytesIO()
        cv = Converter(pdf_stream)
        cv.convert(docx_stream, start=0, end=None)
        cv.close()

        # Offer the DOCX file for download
        st.download_button(
            label="Download DOCX file",
            data=docx_stream.getvalue(),
            file_name=f"{uploaded_file.name.replace('.pdf', '')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        )

        st.success("Conversion complete!")

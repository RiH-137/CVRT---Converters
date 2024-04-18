import streamlit as st
import subprocess
from io import BytesIO
import tempfile
import os

def convert_docx_to_pdf(docx_file):
    # save DOCX file to a temporary file
    temp_docx = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    temp_docx.write(docx_file.read())
    temp_docx.close()

    # get the path for the temporary DOCX and PDF files
    temp_docx_path = temp_docx.name
    pdf_path = os.path.splitext(temp_docx_path)[0] + ".pdf"

    # use subprocess to call the docx2pdf CLI tool
    subprocess.run(["docx2pdf", temp_docx_path])

    return pdf_path

# streamlit app 
st.title("DOCX to PDF Converter")

# upload DOCX file with clear guidance
docx_file = st.file_uploader("Upload a DOCX file to convert to PDF", type=['docx'])

if docx_file is not None:
    # perform conversion when DOCX file is uploaded
    pdf_path = convert_docx_to_pdf(docx_file)

    # provide download link for the converted PDF file
    st.markdown("### Download Converted File")
    st.download_button(label="Download PDF", data=open(pdf_path, 'rb'), file_name="converted_document.pdf", mime="application/pdf")

else:
    st.info("Please upload a DOCX file for conversion.")

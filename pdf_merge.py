import streamlit as st
from PyPDF2 import PdfMerger
from io import BytesIO

# set page title and description
st.set_page_config(page_title="PDF Merger", layout="centered")

# fnction to merge PDF files
def merge_pdfs(pdfs):
    merger = PdfMerger()

    for pdf in pdfs:
        merger.append(pdf)

    merged_pdf = BytesIO()
    merger.write(merged_pdf)
    merged_pdf.seek(0)
    return merged_pdf

# main function for the Streamlit app
def main():
    st.title("PDF Merger")

    uploaded_files = st.file_uploader("Upload PDF files to merge. (Note:- You can select multiple PDFs for merging.)", type=["pdf"], accept_multiple_files=True)

    if uploaded_files is not None:
        st.write("PDF files uploaded successfully!")
        st.write("Merging PDF files...")

        merged_pdf = merge_pdfs(uploaded_files)

        # create a download link for the merged PDF file
        st.download_button(
            label="Download Merged PDF",
            data=merged_pdf,
            file_name="merged_pdf.pdf",
            mime="application/pdf",
        )

if __name__ == "__main__":
    main()

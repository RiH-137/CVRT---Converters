import streamlit as st
from PIL import Image
from io import BytesIO

# setting page title and description
st.set_page_config(page_title="PNG to JPEG Converter", layout="centered")

#  convert PNG to JPEG
def convert_png_to_jpeg(png_file):
    image = Image.open(png_file)
    jpeg_file = BytesIO()
    image.convert("RGB").save(jpeg_file, format="JPEG")
    jpeg_file.seek(0)
    return jpeg_file

# Streamlit app
def main():
    st.title("PNG to JPEG Converter")

    uploaded_file = st.file_uploader("Upload a PNG file", type=["png"])

    if uploaded_file is not None:
        st.write("PNG file uploaded successfully!")
        st.write("Converting PNG to JPEG...")

        jpeg_file = convert_png_to_jpeg(uploaded_file)

        # sisplay the converted JPEG image
        st.image(jpeg_file, caption="Converted JPEG Image")

        # create a download link for the converted JPEG file
        st.download_button(
            label="Download JPEG File",
            data=jpeg_file,
            file_name=uploaded_file.name.split(".")[0] + ".jpg",
            mime="image/jpeg",
        )

if __name__ == "__main__":
    main()

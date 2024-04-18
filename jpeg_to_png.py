import streamlit as st
from PIL import Image
from io import BytesIO

# set page title and description
st.set_page_config(page_title="JPEG to PNG Converter", layout="centered")

#  convert JPEG to PNG
def convert_jpeg_to_png(jpeg_file):
    image = Image.open(jpeg_file)
    png_file = BytesIO()
    image.save(png_file, format="PNG")
    png_file.seek(0)
    return png_file

# miin function for the Streamlit app
def main():
    st.title("JPEG to PNG Converter")

    uploaded_file = st.file_uploader("Upload a JPEG file", type=["jpg", "jpeg"])

    if uploaded_file is not None:
        st.write("JPEG file uploaded successfully!")
        st.write("Converting JPEG to PNG...")

        png_file = convert_jpeg_to_png(uploaded_file)

        # Ddsplay the converted PNG images
        st.image(png_file, caption="Converted PNG Image")

        # create a download link for the converted PNG file
        st.download_button(
            label="Download PNG File",
            data=png_file,
            file_name=uploaded_file.name.split(".")[0] + ".png",
            mime="image/png",
        )

if __name__ == "__main__":
    main()

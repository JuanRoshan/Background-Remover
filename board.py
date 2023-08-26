import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64
import streamlit as st
from streamlit_image_comparison import image_comparison


st.set_page_config(layout="wide", page_title="Background Buster")

st.write("## BACKGROUND BUSTER")
st.write(
    "Welcome to the ultimate solution for hassle🆓 background removal. Are you tired of spending countless hours⏳ manually editing your photos to remove backgrounds?🖥️ Look no further!😃 Our cutting-edge AI technology👩‍💻 is here to revolutionize your image editing experience😎."
)
st.sidebar.write("## Upload and download :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

video_file = open('Untitled 3C.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)







# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Original Image :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Fixed Image :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Download fixed image", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])




if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("The uploaded file is too large. Please upload an image smaller than 5MB.")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./Veyron_SS.jpg")


image_comparison(
    img1="Veyron_SS.jpg",
    img2="fixed (1).png",
    label1="Original image",
    label2="Fixed image"
)

st.image("rmg.png", caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")




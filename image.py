import streamlit as st
from streamlit_image_comparison import image_comparison

# set page config
st.set_page_config(page_title="James Webb Space Telescope vs Hubble Telescope Images", layout="centered")

st.title("James Webb vs Hubble Telescope Pictures")

st.markdown("# Southern Nebula")

# render image-comparison
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/southern_nebula_700.jpg",
    img2="https://www.webbcompare.com/img/webb/southern_nebula_700.jpg",
    label1="original image",
    label2="edited image"
)


st.markdown("# Galaxy Cluster SMACS 0723")

# render image-comparison
image_comparison(
    img1="https://www.webbcompare.com/img/hubble/deep_field_700.jpg",
    img2="https://www.webbcompare.com/img/webb/deep_field_700.jpg",
    label1="Hubble",
    label2="Webb"
)
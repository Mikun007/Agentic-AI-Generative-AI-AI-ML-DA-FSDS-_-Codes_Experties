import streamlit as st
import numpy as np
import cv2
from PIL import Image


def main():
    st.title("Image Processing with OpenCV and Streamlit")

    # Upload image
    uploaded_file = st.file_uploader(label="File Upload", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_container_width=True)

        # Convert to numpy array
        img_array = np.array(image)

        # Display grayscale image
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            # Convert to grayscale using OpenCV
            gray_image = cv2.cvtColor(img_array, cv2.COLOR_BGR2GRAY)
            st.image(gray_image, caption='Grayscale Image', use_container_width=True, channels="GRAY")
        with col2:
            # convert hsv_image
            hsv_image = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
            st.image(hsv_image, caption='HSV Image', use_container_width=True, channels="RGB")
        with col3:
            # convert BGR to RGB
            bgr_rgb = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGRA)
            st.image(bgr_rgb, caption='BGR Image', use_container_width=True)
        with col4:
            crt = cv2.cvtColor(img_array, cv2.COLOR_RGB2YCrCb)
            st.image(crt, caption='YCrC', use_container_width=True)

        col5, col6, col7, col8 = st.columns(4)
        with col5:
            bgr_lab = cv2.cvtColor(img_array, cv2.COLOR_RGB2Lab)
            st.image(bgr_lab, caption="RGB LAB", use_container_width=True)

        with col6:
            rgb_xyz = cv2.cvtColor(img_array, cv2.COLOR_RGB2XYZ)
            st.image(rgb_xyz, caption='RGB XYZ', use_container_width=True)
        with col7:
            rgb_hls = cv2.cvtColor(img_array, cv2.COLOR_RGB2HLS)
            st.image(rgb_hls, caption="HLS", use_container_width=True)


if __name__ == "__main__":
    main()
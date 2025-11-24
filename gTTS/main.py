import streamlit as st
from gtts import gTTS

st.title(" Text To speech Project with Google's Text to Speech (gTTS) library")


txt = st.text_area("Enter Your Text")

if st.button("Submit", type="primary", width=250):
    if txt.strip():
        result = gTTS(text=txt, lang='en', slow=False)
        result.save("text_to_speach.mp3")
        st.success("Text Successfully Submitted")
        st.audio("text_to_speach.mp3")
    else:
        st.warning("Please Enter a Text To Submit")



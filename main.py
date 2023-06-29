import os
import streamlit as st
os.environ["OPENAI_API_KEY"] = st.secrets["openai_api_key"]

from embedchain import App

YTbot = App()


st.set_page_config(layout="centered", page_title="YT QnA")

st.header("YT QnA Bot 🤖")
state = st.session_state
site = st.text_input("Enter your URL here")
if st.button("Build Model"):
  if site is None:
    st.info(f"""Enter YT to Build QnA Bot""")
  elif site:
    st.write(str(site) + " starting to crawl..")
    try:
      YTbot.add("youtube_video", site)
      st.session_state['crawling'] = True
if site and ("crawling" in state):
      st.header("Ask your data")
      user_q = st.text_input("Enter your questions here")
      if st.button("Get Response"):
        try:
          with st.spinner("Model is working on it..."):
            result = YTbot.query(user_q)
            st.subheader('Your response:')
            st.write(result)
        except Exception as e:
          st.error(f"An error occurred: {e}")
          st.error('Oops, the GPT response resulted in an error :( Please try again with a different question.')    

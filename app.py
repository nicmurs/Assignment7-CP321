import streamlit as st
import os

PORT = int(os.environ.get("PORT", 10000)) 

st.title("My Deployed Streamlit App")
st.write("Hello, this is my web app!")

if __name__ == "__main__":
    st.run(port=PORT, address="0.0.0.0")
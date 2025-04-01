import streamlit as st
import os

# Force Streamlit to use the correct port
PORT = int(os.environ.get("PORT", 10000))  

st.set_page_config(page_title="My App")

st.title("My Deployed Streamlit App")
st.write("Hello, this is my web app!")

if __name__ == "__main__":
    # Run Streamlit with explicit config
    import subprocess
    subprocess.run(["streamlit", "run", "app.py", "--server.port", str(PORT), "--server.address", "0.0.0.0"])
import streamlit as st
import subprocess
import os
import time

# Force Streamlit to use the correct port
PORT = int(os.environ.get("PORT", 10000))  

st.set_page_config(page_title="My App")

st.title("My Deployed Streamlit App")

# Convert the notebook to HTML
subprocess.run(["python3", "-m", "jupyter", "nbconvert", "--to", "html", "Assignment7.ipynb"])

# Read the converted HTML file
with open("Assignment7.html", "r", encoding="utf-8") as f:
    notebook_html = f.read()

# Display the HTML in Streamlit
st.components.v1.html(notebook_html, height=800, scrolling=True)

# Start Dash in the background
def start_dash():
    subprocess.Popen(["python3", "dash_app.py"])  # Runs Dash in a separate process
    time.sleep(3)  # Give it time to start

# Run Dash when Streamlit starts
start_dash()

# Streamlit UI
#st.markdown("### Embedded Dash App:")
#DASH_APP_URL = "http://localhost:8050/dash"  # Use local Dash URL

# Embed Dash inside Streamlit
#st.components.v1.iframe(DASH_APP_URL, height=600, scrolling=True)

if __name__ == "__main__":
    # Run Streamlit with explicit config
    import subprocess
    subprocess.run(["streamlit", "run", "app.py", "--server.port", str(PORT), "--server.address", "0.0.0.0"])




import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Initialize Dash app
dash_app = dash.Dash(__name__, server=True, routes_pathname_prefix="/dash/")

# Sample Data
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# Layout
dash_app.layout = html.Div([
    html.H1("Dash App Inside Streamlit"),
    dcc.Graph(figure=fig)
])

# Expose Dash server
server = dash_app.server

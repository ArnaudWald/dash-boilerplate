# -*- coding: utf-8 -*-
"""Main Dash App."""
import dash

external_stylesheets = ['assets/bWLwgP.css']

app = dash.Dash(__name__,
                external_stylesheets=external_stylesheets,
                suppress_callback_exceptions=True)

app.title = "My Dash app"

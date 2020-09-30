# -*- coding: utf-8 -*-
"""Basic dashboard."""

import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import plotly.express as px
import pandas as pd

from main_app import app


df = pd.read_csv('data/gapminderDataFiveYear.csv')


layout = html.Div([
    dcc.Graph(id='graph-with-slider-dashboard3'),
    dcc.Slider(
        id='year-slider-dashboard3',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])


@app.callback(
    Output('graph-with-slider-dashboard3', 'figure'),
    [Input('year-slider-dashboard3', 'value')])
def update_dashboard3_figure(selected_year):
    """Update figure on callback trigger."""
    filtered_df = df[df.year == selected_year]

    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp",
                     size="pop", color="continent", hover_name="country",
                     log_x=True, size_max=55)

    fig.update_layout(transition_duration=500)

    return fig

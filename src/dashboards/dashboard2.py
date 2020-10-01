# -*- coding: utf-8 -*-
"""Basic dashboard with Table."""

import dash_html_components as html
import pandas as pd

from dashboards.graph_utils import generate_table


df = pd.read_csv('data/gapminderDataFiveYear.csv')


layout = html.Div(children=[
    html.Div(children=[
        html.Br(),
        html.P("Data:"),
        generate_table(df)
    ])
])

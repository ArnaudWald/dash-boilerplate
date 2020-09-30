# -*- coding: utf-8 -*-
"""Provide the basic layout of the app."""
import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html

from main_app import app
from dashboards import dashboard1, dashboard2, dashboard3, not_found


tabs_styles = {
    'height': '70px',
    'fontSize': '22px',
}

tab_style = {}

tab_selected_style = {
    'fontWeight': 'bold',
}


layout = html.Div([
    html.H1('Welcome to my Dash app!'),
    dcc.Tabs(
        id='tabs-selector',
        children=[
            dcc.Tab(label='Tab 1', value='tab-1', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Tab 2', value='tab-2', style=tab_style, selected_style=tab_selected_style),
            dcc.Tab(label='Tab 3', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        ],
        value='tab-1',
        style=tabs_styles,
        persistence=True,
        persistence_type="session",
    ),
    html.Div(id='tabs-content')
])


@app.callback(Output('tabs-content', 'children'),
              [Input('tabs-selector', 'value')])
def render_content(tab):
    """Organize tabs."""
    switcher = {
        'tab-1': dashboard1,
        'tab-2': dashboard2,
        'tab-3': dashboard3,
     }

    return switcher.get(tab, not_found).layout

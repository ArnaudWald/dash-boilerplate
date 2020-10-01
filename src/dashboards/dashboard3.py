# -*- coding: utf-8 -*-
"""Basic dashboard with placeholder graphs."""

import dash_core_components as dcc
from dash.dependencies import Input, Output
import dash_html_components as html
import pandas as pd

from main_app import app
from dashboards.graph_utils import make_empty_graphs, DEFAULT_COLORS as colors

LAYOUT_COLUMNS = ['Subset 1', 'Subset 2', 'Subset 3', 'Subset 4']
LAYOUT_ROWS = ['Row 1', 'Row 2', 'Row 3']


layout = html.Div(
    style={'backgroundColor': colors['background']},
    children=[
        html.Div(id='dashboard-3-main-page'),
        dcc.Interval(id='dashboard-3-interval',
                     interval=5*60*1000,  # 5 minutes (in milliseconds)
                     # interval=1*1000,  # in milliseconds
                     n_intervals=0)
    ]
)


def load_data_make_graphs():
    """Load the CSV dataframes for plotting."""
    figures = {}
    for col_name in LAYOUT_COLUMNS:
        figures[col_name] = {}

        for row_name in LAYOUT_ROWS:
            try:
                df = pd.read_csv(f"data/{col_name}/{row_name}.csv", index_col=0)
                # figures[col_name][row_name] = make_default_graph(df, title=title)
            except FileNotFoundError:
                # print("Error loading CSV data for the %s %s data. Returning empty graph..." % (col_name, row_name))
                figures[col_name][row_name] = make_empty_graphs(n=1, height_pixels=300)

    return figures


def make_sub_plot(figures, col_name):
    """Avoid copy-pasting and errors."""
    id_name = col_name.lower().replace(' ', '-')

    div_contents = [html.H2(col_name)]

    for row_name in LAYOUT_ROWS:
        row_id = id_name + '-' + row_name.lower().replace(' ', '-')
        div_contents.append(
            dcc.Graph(id=row_id, figure=figures[col_name][row_name])
        )

    subset_layout = html.Div(
        className="column",
        id=id_name,
        children=div_contents,
        style={}
    )

    return subset_layout


@app.callback(Output('dashboard-3-main-page', 'children'),
              [Input('dashboard-3-interval', 'n_intervals')])
def dashboard_3_update_graphs(n_intervals):
    """Update all the graphs."""
    figures = load_data_make_graphs()

    main_page_layout = html.Div(children=[
        html.Div(className='row', children=[
            make_sub_plot(figures, LAYOUT_COLUMNS[0]),
            make_sub_plot(figures, LAYOUT_COLUMNS[1]),
        ]),

        html.Div(className='row', children=[
            make_sub_plot(figures, LAYOUT_COLUMNS[2]),
            make_sub_plot(figures, LAYOUT_COLUMNS[3]),
        ]),
    ])
    return main_page_layout

# -*- coding: utf-8 -*-
"""Utility functions for the dashboards."""
from dash_table import DataTable
import plotly.graph_objs as go


DEFAULT_COLORS = {
    'background': '#FFFFFF',
    'text': '#000000'
}


def generate_table(df, page_size=10):
    """Generate a formatted table from a DataFrame."""
    table = DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        page_size=page_size,
        style_cell={
            'textAlign': 'left',
            'color': "#000000"
        },
        style_cell_conditional=[
            {
                'if': {'column_id': 'count'},
                'textAlign': 'right'
            }
        ],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        }
    )
    return table


def make_empty_graphs(
    n=1,
    height_pixels=500,
    colors=DEFAULT_COLORS
):
    """Make n placeholder graphs."""
    fig = go.Figure()
    fig_layout = go.Layout(
        paper_bgcolor=colors['background'],
        font=dict(color=colors['text']),
        height=height_pixels,
    )
    fig.update_layout(fig_layout)

    if n > 1:
        figs = []
        for i in range(n):
            figs.append(fig)
        return figs
    else:
        return fig

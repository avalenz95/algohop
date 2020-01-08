import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import networkx as nx

from time import sleep
from random import randint, seed


# For the documentation to always render the same values
seed(0)

app = dash.Dash(__name__)


#Creates a table for node input
def graph_table():
        #Column Names
        params = [
        'Nodes', 'Edges', 'PosX', 'PosY'
        ]
        
        return dash_table.DataTable(
                id='table-editing-simple',
                columns=(
                    [{'id': p, 'name': p} for p in params]
                ),
                data=[],
                editable=True
            )


#Layout of the dash app
app.layout = html.Div([

    html.Br(),

    graph_table(),

])

if __name__ == '__main__':
    app.run_server(debug=True)

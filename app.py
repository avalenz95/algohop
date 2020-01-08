import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
import plotly
import plotly.graph_objs as go
import networkx as nx
import dash_cytoscape as cyto



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


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


#Displays graph of nodes
def graph_nodes():

    return cyto.Cytoscape(
        id='cytoscape-two-nodes',
        layout={'name': 'preset'},
        style={'width': '100%', 'height': '400px'},
        elements=[
            {'data': {'id': 'one', 'label': 'Node 1'}, 'position': {'x': 75, 'y': 75}},
            {'data': {'id': 'two', 'label': 'Node 2'}, 'position': {'x': 200, 'y': 200}},
            {'data': {'source': 'one', 'target': 'two'}}
        ]
    )


def navbar():
    return dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Page 1", href="#")),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More pages", header=True),
                    dbc.DropdownMenuItem("Page 2", href="#"),
                    dbc.DropdownMenuItem("Page 3", href="#"),
                ],
                nav=True,
                in_navbar=True,
                label="More",
            ),
        ],
        brand="NavbarSimple",
        brand_href="#",
        color="primary",
        dark=True,
    )


#Layout of the dash app
def layout():
    return html.Div(
        id='app-body',
        className='application-body',
        children=[
            navbar(), 
            html.Div(
                id='info-table',
                className='info-table',
                children=[
                    dcc.Tabs(id='info-tabs', value='Test Main Tab', children=[
                        dcc.Tab(
                            label='Tab 1',
                            value='Test Value 1',
                            children=html.Div(className='control-tab', children=[
                                html.H4(className='what-is', children='Information Test'),
                                dcc.Markdown('''Test''')
                            ])
                        ),
                        dcc.Tab(
                            label='Tab 2',
                            value='Test Value 2',
                            children=html.Div(className='control-tab', children=[
                                html.H4(className='what-is', children='Information Test 2'),
                                dcc.Markdown('''Test 2''')
                            ])
                        )
                    ])
                ]
            ),
        graph_table(),

        graph_nodes(),

    ])

app.layout = layout()

if __name__ == '__main__':
    app.run_server(debug=True)

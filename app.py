import os
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import plotly
import plotly.graph_objs as go
import networkx as nx
import dash_cytoscape as cyto



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])


#Creates a table for node input
def graph_table():
    #TODO: Incorporate live dataframes
    table_header = [
        html.Thead(html.Tr([html.Th("Node"), html.Th("Edges"), html.Th("PosX"), html.Th("PosY")]))
    ]
    row1= html.Tr([html.Th(0), html.Th("(0,0)"), html.Th("0"), html.Th("0")])

    table_body = [html.Tbody([row1])]

    return dbc.Table(table_header + table_body,
        bordered=True,
        dark=True,
        hover=True,
        responsive=True,
        striped=True
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
    return dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Navbar", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="https://www.notion.so/ablades/1c0cc15bc0b74ecc8dac31c9276d61b0",
            ),
            dbc.NavbarToggler(id="navbar-toggler"),
        ],
        color="dark",
        dark=True,
    )

def info_tabs():
    #First Tab Content
    tab1_content = dbc.Card(
        dbc.CardBody(
            [
                html.P("Tab 1 Content", className="tab-text"),
                dbc.Button("Test Button", color="success"),
            ]
        ),
        className="info-tab"
    )

    #Second Tab Content
    tab2_content = dbc.Card(
        dbc.CardBody(
            [
                html.P("Tab 2 Content", className="tab-text"),
                dbc.Button("Test Button", color="success"),
            ]
        ),
        className="info-tab"
    )

    #Third Tab Content
    tab3_content = dbc.Card(
        dbc.CardBody(
            [
                html.P("Tab 3 Content", className="tab-text"),
                dbc.Button("Test Button", color="success"),
            ]
        ),
        className="info-tab"
    )

    #Builds Tab Table

    return dbc.Tabs(
        [
            dbc.Tab(tab1_content, label="Tab 1"),
            dbc.Tab(tab2_content, label="Tab 2"),
            dbc.Tab(tab3_content, label="Tab 3"),
        ]
    )




def body():
    return dbc.Container(
        [
            dbc.Row(
                [
                    #Info Table Column
                    dbc.Col(
                        [
                            html.H2("Info Tabs"),
                            info_tabs()
                        ],
                        width=4
                    ),
                    #Visualizaton Column
                    dbc.Col(
                        [
                            html.H2("Visualization"),
                            graph_nodes()
                        ]
                    )
                ]
            ),
            dbc.Row(
                [
                    #Node Input Table
                    dbc.Col(
                        [
                            html.H2("Node Table"),
                            graph_table()
                        ]
                    )
                ]
            )
        ],
        fluid=True
    )

#Dash app layout
app.layout = html.Div([navbar(), body()])


if __name__ == '__main__':
    app.run_server(debug=True)

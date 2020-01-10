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
import pandas as pd



app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LUX])
app.title = 'AlgoHop'
server = app.server

#Defines the input properties for node and edge colors
def color_input():
    edge_color_input = html.Div(style={'width': '50%', 'display': 'inline'},
        children=[
            dbc.Label("Edge Color"),
            dbc.Input(id="edge-color", placeholder="green", type="text"),
        ]
    )

    node_color_input = html.Div(style={'width': '50%', 'display': 'inline'},
        children=[
            dbc.Label("Node Color"),
            dbc.Input(id="node-color", placeholder="green", type="text"),
        ]
    )

    return html.Div([node_color_input, edge_color_input])

def node_table():
    col_names = ['Node', 'Edges']

    return dash_table.DataTable(
        id='node-table',
        columns=([{'id': name, 'name': name} for name in col_names]),
        data=[
            {'Node': 0, 'Edges': (0,1)},
            {'Node': 1, 'Edges': (0,1)},
            {'Node': 2, 'Edges': (0,2)}
        ],
        editable=True
    )
    

#Displays graph of nodes
def node_graph():
    default_stylesheet = [
        {
            'selector': 'node',
            'style': {
                'background-color': '#BFD7B5',
                'label': 'data(label)'
            }
        },
        {
            'selector': 'edge',
            'style': {
                'line-color': '#A3C4BC'
            }
        }
    ]

    return cyto.Cytoscape(
        id='node-display',
        layout={'name': 'circle'},
        style={'width': '100%', 'height': '900px'},
        stylesheet= default_stylesheet,
        elements=[]
    )


def navbar():
    return dbc.Navbar(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="", height="30px")),
                        dbc.Col(dbc.NavbarBrand("Algorithm Hop", className="ml-2")),
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

    info_text = "Algorithm Hop is a step-by-step way of visualizing how algorithms work. Right now the site is limited to just one but as I become more familar with dash and learn more algorithms in class I hope to provide ways to visualize them here so stay tuned!"
    #First Tab Content
    tab1_content = dbc.Card(
        dbc.CardBody(
            [
                html.P(info_text, className="tab-text"),
                dbc.Button("Test Button", color="success"),
            ]
        ),
        className="info-tab"
    )

    #Second Tab Content
    tab2_content = dbc.Card(
        dbc.CardBody(
            [
                html.P("Graph Properties", className="tab-text"),
                color_input(),
                dbc.Button("Test Button", color="success"),
            ]
        ),
        className="info-tab"
    )

    #Third Tab Content
    tab3_content = dbc.Card(
        dbc.CardBody(
            [
                node_table(),
                html.P("Tab 3 Content", className="tab-text"),
                dbc.Button("Test Button", color="success"),
            ]
        ),
        className="info-tab"
    )

    #Builds Tab Table

    return dbc.Tabs(
        [
            dbc.Tab(tab1_content, label="About", tabClassName="tab-head"),
            dbc.Tab(tab2_content, label="Graph Properties", tabClassName="tab-head"),
            dbc.Tab(tab3_content, label="Table Properties", tabClassName="tab-head"),
        ],
    )




def body():
    return dbc.Container(
        [
            dbc.Row(
                [
                    #Info Table Column
                    dbc.Col(
                        [
                            #html.H2("Info Tabs"),
                            info_tabs()
                        ],
                        width=4
                    ),
                    #Visualizaton Column
                    dbc.Col(
                        [
                            #html.H2("Visualization"),
                            node_graph()
                        ]
                    )
                ]
            )
        ],
        fluid=True,
        style={"background-color": "#f6f6f6"}
    )

#Dash app layout
app.layout = html.Div([navbar(), body()])


#Set up node display
@app.callback(
    Output('node-display', 'elements'),
    [Input('node-table', 'data'),
     Input('node-table', 'columns')],
     [State('node-display', 'elements')])
def update_nodes(rows, columns, elements):
    #set up data frame
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    
    node_list = list()

    #Create all nodes
    for index, row in df.iterrows():
        node_list.append({'data': {'id': f'{row["Node"]}', 'label': f'Node {row["Node"]}'}})

    #Create all edges
    for index, row in df.iterrows():
        edge = row['Edges']
        node_list.append({'data': {'source': f'{edge[0]}', 'target': f'{edge[1]}', 'label': f'Node {edge[0]} to {edge[1]}'}})

    print(node_list)
    # #Visualization object
    return node_list


@app.callback(Output('node-display', 'stylesheet'),
          [Input('edge-color', 'value'),
           Input('node-color', 'value')],
           [State('node-display', 'stylesheet')])
def update_stylesheet(edge_color, node_color, stylesheet):
    if edge_color is None:
        edge_color = 'green'

    if node_color is None:
        node_color = 'green'

    new_colors = [
        {
            'selector': 'node',
            'style': {
                'background-color': node_color
            }
        },
        {
            'selector': 'edge',
            'style': {
                'line-color': edge_color
            }
        }
    ]

    return stylesheet + new_colors


if __name__ == '__main__':
    app.run_server(debug=True)

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
        dbc.NavItem(dbc.NavLink("Link", href="#")),
        dbc.DropdownMenu(
            nav=True,
            in_navbar=True,
            label="Menu",
            children=[
                dbc.DropdownMenuItem("Entry 1"),
                dbc.DropdownMenuItem("Entry 2"),
                dbc.DropdownMenuItem(divider=True),
                dbc.DropdownMenuItem("Entry 3"),
            ],
        ),
    ],
    brand="Demo",
    brand_href="#",
    sticky="top",
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
                    dbc.Col(
                        [
                            html.H2("Input Table"),
                            graph_table()
                        ]
                    )
                ]
            )
        ]
    )

app.layout = html.Div([navbar(), body()])

#Layout of the dash app
def layout():
    return html.Div(
        [
            dbc.Row
        ]
    )
    # return html.Div(
    #     id='app-body',
    #     className='application-body',
    #     children=[
    #         navbar(), 
    #         html.Div(
    #             id='info-table',
    #             className='info-table',
    #             children=[
    #                 dcc.Tabs(id='info-tabs', value='Test Main Tab', children=[
    #                     dcc.Tab(
    #                         label='Tab 1',
    #                         value='Test Value 1',
    #                         children=html.Div(className='control-tab', children=[
    #                             html.H4(className='what-is', children='Information Test'),
    #                             dcc.Markdown('''Test''')
    #                         ])
    #                     ),
    #                     dcc.Tab(
    #                         label='Tab 2',
    #                         value='Test Value 2',
    #                         children=html.Div(className='control-tab', children=[
    #                             html.H4(className='what-is', children='Information Test 2'),
    #                             dcc.Markdown('''Test 2''')
    #                         ])
    #                     )
    #                 ])
    #             ]
    #         ),
    #     graph_table(),

    #     graph_nodes(),

    # ])

#app.layout = layout()

if __name__ == '__main__':
    app.run_server(debug=True)

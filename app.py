from flask import Flask, render_template
import plotly.graph_objects as go
import networkx as nx
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():

    #Creates empty graph
    G = nx.Graph()
    #Test add nodes
    G.add_nodes_from([2, 3])

    #Test add edges
    G.add_edges_from([(1, 2), (1, 3)])

    #provides number of nodes
    print(f"# Nodes: {G.number_of_nodes()}")

    #provides number of edges
    print(f"# Edges: {G.number_of_edges()}")

    #Sets postions of nodes
    pos = nx.circular_layout(G)
    nx.set_node_attributes(G, pos, 'pos')

    #Update edges with positions
    edge_xpos = []
    edge_ypos = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        edge_xpos.extend([x0, x1, None])
        edge_ypos.extend([y0, y1, None])
        print(f"edge: {edge}")

    #Edge Styling
    edge_trace = go.Scatter(
        x=edge_xpos, 
        y=edge_ypos,
        line=dict(width=4, color='#888'),
        hoverinfo='none',
        mode='lines')

    #Update node positions
    node_xpos = []
    node_ypos = []
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        node_xpos.append(x)
        node_ypos.append(y)
        print(f"node: {node}")

    #Node Styling
    node_trace = go.Scatter(
        x=node_xpos, 
        y=node_ypos,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            color=[],
            #handles size of nodes
            size=30,
            #handles width of nodes
            line_width=5))

    #Adjaceny Hover Text
    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append('# of connections: '+str(len(adjacencies[1])))

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text


    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='',

                titlefont_size=16,

                showlegend=False,

                hovermode='closest',

                margin=dict(b=20,l=5,r=5,t=40),

                #Play Animation Button
                updatemenus=[dict(
                    type="buttons",
                        buttons=[dict(
                            label="Play Animation",
                            method="animate",
                            args=[])]
                )],
                #Bottom of graph annotations
                annotations=[ dict(
                    text="",

                    showarrow=False,

                    xref="paper", yref="paper",

                    x=0.005, y=-0.002 ) ],

                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
    figure = fig.show()



    return render_template('index.html', figure=figure)

if __name__ == "__main__":
    app.run(debug=True)
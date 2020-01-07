from flask import Flask, render_template
import plotly.graph_objects as go
import networkx as nx

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
    G.number_of_nodes()

    #provides number of edges
    G.number_of_edges()

    edge_x = []
    edge_y = []
    for edge in G.edges():
        print(f"edge: {edge}")
        # x0, y0 = G.nodes[edge[0]]
        # x1, y1 = G.nodes[edge[1]]
        # edge_x.append(x0)
        # edge_x.append(x1)
        # edge_x.append(None)
        # edge_y.append(y0)
        # edge_y.append(y1)
        # edge_y.append(None)

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=4, color='#888'),
        hoverinfo='none',
        mode='lines')

    node_x = []
    node_y = []
    for node in G.nodes():
        print(f"node: {node}")
        # x, y = G.nodes[node]['pos']
        # node_x.append(x)
        # node_y.append(y)

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            # colorscale options
            #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
            #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
            #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=30,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
            line_width=5))

    node_adjacencies = []
    node_text = []
    for node, adjacencies in enumerate(G.adjacency()):
        node_adjacencies.append(len(adjacencies[1]))
        node_text.append('# of connections: '+str(len(adjacencies[1])))

    node_trace.marker.color = node_adjacencies
    node_trace.text = node_text

    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title='<br>Network graph made with Python',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[ dict(
                    text="Python code: <a href='https://plot.ly/ipython-notebooks/network-graphs/'> https://plot.ly/ipython-notebooks/network-graphs/</a>",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002 ) ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )
    figure = fig.show()


    return render_template('index.html',figure=figure)

if __name__ == "__main__":
    app.run_server(debug=True)